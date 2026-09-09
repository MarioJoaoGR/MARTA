# Testa se cada modulo carrega, DEPOIS da porta de entrada da gem estar aberta.
#
#   ruby carrega.rb <raiz> <entrada> <caminhos de carregamento...> < lista
#
# Um `require` seco do modulo nao e o teste certo: a maioria dos ficheiros de
# uma gem nao foi feita para ser carregada isolada (o `lib/foo/bar.rb` conta com
# constantes que o `lib/foo.rb` ja definiu). O que um spec faz e carregar a
# biblioteca e depois usar a classe — e e isso que se reproduz aqui.
#
# Cada modulo vai num processo filho: um que rebente nao contamina o seguinte, e
# carregar o A nao faz o B passar por tabela.
require "json"

raiz, entrada = ARGV[0], ARGV[1]
# As pastas de carregamento vem de fora: nos monorepos ha uma lib por sub-gem
# (fastlane/lib, spaceship/lib, ...) e adivinha-las aqui era fragil.
caminhos = ARGV[2..] || []
lista = $stdin.read.split("\n").reject(&:empty?)
$LOAD_PATH.unshift(*caminhos.select { |d| File.directory?(d) })
$LOAD_PATH.unshift(raiz)

# 1. A porta de entrada. Ha gems sem porta unica (a `addressable` nao tem
#    lib/addressable.rb): nesse caso vai-se directo aos modulos.
porta = { "ok" => true, "erro" => nil }
if entrada.nil? || entrada.empty?
  porta["sem_porta"] = true
else
  begin
    require entrada
  rescue Exception => e
    porta = { "ok" => false, "erro" => "#{e.class}: #{e.message.to_s[0, 300]}" }
  end
end
puts JSON.generate({ "tipo" => "porta", "entrada" => entrada.to_s }.merge(porta))
$stdout.flush

# 2. Cada modulo, isolado.
lista.each do |rel|
  alvo = rel.sub(/\.rb\z/, "")
  caminhos.each do |c|
    pref = c.sub(/\A#{Regexp.escape(raiz)}\/?/, "")
    next if pref.empty?
    if alvo.start_with?(pref + "/")
      alvo = alvo[(pref.length + 1)..]
      break
    end
  end

  ler, escrever = IO.pipe
  # Canal so para o stderr do filho: ha codigo que escreve a razao e chama
  # `exit!`, que salta ate os at_exit (a `brakeman` faz isso com o ruby2ruby).
  # Sem isto ficavam 65 modulos com "processo morreu (255)" e razao nenhuma.
  err_ler, err_escrever = IO.pipe
  pid = fork do
    ler.close
    err_ler.close
    $stderr.reopen(err_escrever)
    respondido = false
    responde = lambda do |res|
      next if respondido
      respondido = true
      escrever.write(JSON.generate(res))
      escrever.close
    end
    begin
      require alvo
      responde.call({ "ok" => true, "erro" => nil })
    rescue Exception => e
      responde.call({ "ok" => false, "erro" => "#{e.class}: #{e.message.to_s[0, 300]}" })
    end
    exit!(0)
  end
  escrever.close
  err_escrever.close

  # Tempo limite POR MODULO: ha ficheiros que abrem sockets ou ciclos de eventos
  # ao serem carregados e ficam pendurados. Sem isto, um so deles pendurava a
  # gem inteira (foram 41 modulos do eventmachine a sair sem explicacao).
  limite, morto = Time.now + 20, nil
  loop do
    got, st = Process.waitpid2(pid, Process::WNOHANG)
    if got
      morto = st
      break
    end
    if Time.now > limite
      Process.kill("KILL", pid) rescue nil
      Process.waitpid(pid) rescue nil
      morto = :timeout
      break
    end
    sleep 0.05
  end
  saida = (morto == :timeout) ? "" : ler.read
  ler.close
  erro_stderr = err_ler.read.to_s.strip.split("\n").reject(&:empty?).last.to_s[0, 250]
  err_ler.close

  res = if morto == :timeout
          { "ok" => false, "erro" => "timeout: pendurou-se a carregar (20s)" }
        else
          begin
            JSON.parse(saida)
          rescue StandardError
            razao = erro_stderr.empty? ? "sem mensagem" : erro_stderr
            { "ok" => false, "erro" => "saida abrupta: #{razao}" }
          end
        end
  puts JSON.generate({ "tipo" => "modulo", "ficheiro" => rel, "require" => alvo }.merge(res))
  $stdout.flush
end
