# Condutor em lote do parser: le caminhos do stdin (um por linha) e emite um
# JSON por linha.
#
# Usa a MESMA MartaParse.analyze da ferramenta, para nao haver divergencia entre
# o que se mede aqui e o que a ferramenta faz. Existe porque o `parse_file` do
# fluxo normal abre um processo Ruby POR FICHEIRO: para os ~12 mil ficheiros do
# universo isso seriam 12 mil processos.
require "json"
require_relative "../../../marta/ruby_backend/rb/marta_parse"

$stdin.each_line do |line|
  path = line.chomp
  next if path.empty?
  begin
    src = File.read(path, encoding: "UTF-8")
    src = src.scrub("?") unless src.valid_encoding?
    puts JSON.generate(MartaParse.analyze(src, path))
  rescue => e
    puts JSON.generate({ "path" => path, "fatal" => "#{e.class}: #{e.message}" })
  end
  $stdout.flush
end
