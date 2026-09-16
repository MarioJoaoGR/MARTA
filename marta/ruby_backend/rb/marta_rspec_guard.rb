# frozen_string_literal: true

# Proteção do relatório JSON do RSpec. Carregado com `rspec -r` antes de cada spec.
#
# Há gems que carregam `active_support/core_ext/object/json`, que substitui o
# `to_json` de todos os objetos por um que chama `ActiveSupport::JSON.encode`,
# mas sem carregar o `active_support/json` onde esse módulo vive. O módulo sob
# teste carrega e o spec passa; o que rebenta é o RSpec, no fim, ao serializar o
# relatório: `uninitialized constant ActiveSupport::JSON`. O resultado era lido
# como falha de carregamento. Visto na ransack.
#
# O `after(:suite)` corre antes de o formatador escrever o relatório. Só atua
# quando o `to_json` foi mesmo substituído sem o encoder: nas outras gems não faz
# nada.
RSpec.configure do |config|
  config.after(:suite) do
    if defined?(ActiveSupport::ToJsonWithActiveSupportEncoder) && !defined?(ActiveSupport::JSON)
      begin
        require "active_support/json"
      rescue LoadError
        nil
      end
    end
  end
end
