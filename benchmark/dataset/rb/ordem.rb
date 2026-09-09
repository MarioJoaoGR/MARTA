# O modulo falha por si, ou so porque foi carregado antes dos irmaos?
#
#   ruby ordem.rb <raiz> <entrada> <caminhos...> < lista
#
# Carrega a biblioteca INTEIRA em varias passagens (ignorando falhas) e depois
# diz, para cada modulo, se ficou carregado. Se ficou, o que falhou antes foi a
# ORDEM do nosso teste e nao o modulo.
#
# Medido numa amostra de 10 gems: 109 de 199 NameError (55%) eram desta rigidez.
require "json"

raiz, entrada = ARGV[0], ARGV[1]
caminhos = ARGV[2..] || []
lista = $stdin.read.split("\n").reject(&:empty?)
$LOAD_PATH.unshift(*caminhos.select { |d| File.directory?(d) })
$LOAD_PATH.unshift(raiz)

begin
  require entrada unless entrada.to_s.empty?
rescue Exception
end

def alvo_de(rel, raiz, caminhos)
  a = rel.sub(/\.rb\z/, "")
  caminhos.each do |c|
    pref = c.sub(/\A#{Regexp.escape(raiz)}\/?/, "")
    next if pref.empty?
    return a[(pref.length + 1)..] if a.start_with?(pref + "/")
  end
  a
end

alvos = lista.map { |rel| [rel, alvo_de(rel, raiz, caminhos)] }

# Tres passagens: quem falha na primeira pode passar na segunda, depois de os
# irmaos terem definido as constantes que lhe faltavam.
3.times do
  alvos.each do |_rel, a|
    begin
      require a
    rescue Exception
    end
  end
end

alvos.each do |rel, a|
  carregado = $LOADED_FEATURES.any? { |f| f.end_with?("/" + a + ".rb") }
  puts JSON.generate({ "ficheiro" => rel, "carregado" => carregado })
end
