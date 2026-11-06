# A5, segunda etapa — ambiente por projeto e execução numa cópia opcional

Entrega de 6 de novembro de 2026, posterior ao isolamento de respostas e métricas
por pedido (`6e5179632`). **A geração continua sequencial.** Esta entrega prepara
as fronteiras dos processos Ruby; não acrescenta workers nem mede aceleração.

Atualização: a entrega seguinte acrescenta [workers opcionais e coordenação](RUBY_GENERATION_WORKERS.md). O texto abaixo descreve o âmbito desta segunda etapa.

## Ambiente por projeto, por omissão

O backend Ruby nativo recebe uma cópia imutável das variáveis de ambiente. Sem
configuração explícita, o projeto captura-as na primeira descoberta. Alterar
`os.environ` posteriormente não troca o Ruby, RSpec, gems ou variáveis da aplicação
que esse projeto usa. Para mudar de ambiente, criar outro `RubyProject`.

Também se pode fornecer `subprocess_env=dict(os.environ, GEM_HOME=..., ...)` na
API. É um ambiente **completo**, não um conjunto de overrides: o chamador deve
incluir os caminhos/variáveis necessários. O mapping fornecido é copiado e exige
chaves/valores string. No CLI, o JSON de `--environment` pode conter a propriedade
`subprocess_env`, além de `load_paths`, `preload`, etc.

Prism, verificação sintática, RSpec, cobertura e descoberta de dependências usam
esse ambiente explícito, sem limpar/alterar `os.environ` nem chamar `os.chdir`.
O probe de dependências continua a retirar `RUBYOPT` apenas da sua própria cópia,
como antes, para não carregar Bundler ao analisar fontes de outras dependências.
O `BUNDLE_GEMFILE` relativo é resolvido a partir da raiz do projeto.

Cada projeto possui a configuração do seu backend nativo, mesmo que o chamador
lhe tenha entregue uma instância partilhada. A descoberta limpa o índice de
dependências anterior. O pequeno `biblioteca.rb` só é reescrito quando muda e a
substituição é atómica; deixa de ser reescrito a cada método.

As funções standalone conservam a compatibilidade: sem `env=...`, herdam o
ambiente do processo. Subclasses/backends customizados mantêm o seu contrato e
não recebem uma promessa de isolamento automático.

A pós-avaliação nativa opcional mantém igualmente o ambiente do projeto, remapeia
os caminhos locais nas suas cópias e passa o ambiente aos processos Mutant e à
sua validação RSpec. Não se altera o avaliador específico do XRepoTest.

## Workspace separado, opt-in

`RubyProject(..., isolate_execution=True)` ou `--isolate_execution` ativa a cópia
para o **RubyBackend nativo**. Sem essa opção, mantém-se a execução no projeto
original e não se copia o repositório.

O fluxo com a opção é:

1. O coordenador conserva fontes/contexto, sumários, grafo, RAG, recorder e
   checkpoints. Não se volta a analisar, gerar sumários ou carregar outro modelo.
2. Quando há trabalho Ruby a executar, cria uma única cópia temporária do
   repositório. Essa cópia serve todos os métodos e rondas dessa invocação.
3. Planner/Dev mantêm os mesmos construtores de prompts, parâmetros e limites.
   Os candidatos são escritos/verificados apenas na cópia. Exceções/cancelamentos
   arquivam o candidato disponível em `rejected_specs`, nunca como spec aceite.
4. Um candidato aprovado é comparado com o conteúdo validado e publicado
   atomicamente no destino habitual de `marta_specs`. Conteúdo alterado pelo
   próprio teste ou um caminho de publicação por symlink é recusado.
5. O coordenador prepara os specs retidos na cópia e valida a **suite acumulada**
   num único processo. Mantém o rollback arquivado de novos specs incompatíveis.
   Só depois é certificado o checkpoint da ronda.
6. Confere os hashes das fontes e declarações de dependências na origem/cópia
   antes/depois da validação. Uma alteração impede certificar a ronda. Os
   outputs ainda não certificados conservam a política anterior de arquivo na
   retoma; não se transformam silenciosamente em resultados aceites.
7. A cópia é removida ao sair normalmente ou por exceção/cancelamento Python.

A API simples `generate_all` também usa a cópia quando pedida e partilha o lock
de escritor dos outputs. Continua a ser a API de uma passagem, sem o protocolo
de checkpoints/validação acumulada de `generate_rounds`.

O workspace é lazy: sem specs a validar nem métodos a gerar, não há cópia. Uma
retoma com specs já certificados continua a necessitar de uma cópia para os
**revalidar**, mesmo que não faça novos pedidos LLM.

## Limites explícitos

- Esta primeira versão exige um projeto relocatável e sem symlinks nas entradas
  copiadas. Falha antes de pedir geração se detetar esses casos. Não segue links
  para árvores externas nem usa hardlinks que permitam alterar as fontes originais.
- Exclui `.git`, outputs/caches MARTA e o `output_root` quando fica dentro do
  projeto. Conserva os restantes recursos do projeto; a cópia pode ser grande.
  Não funciona para código que exige `.git` ou caminhos absolutos da origem.
- Caminhos absolutos internos do ambiente, load paths e preloads são remapeados.
  Helpers explícitos externos podem ser copiados uma vez; diretórios de carga
  externos exigem um ambiente relocatável. `RUBYOPT` que referencia a origem é
  recusado. Não se reescreve arbitrariamente código ou variáveis da aplicação.
- O Ruby e gems já instalados fora do projeto permanecem externos. Não se instala
  nem descarrega nada e não se certifica a imutabilidade dessas instalações.
- É isolamento de diretórios/ambiente dos subprocessos, **não uma sandbox do SO**.
  Código Ruby pode aceder a caminhos absolutos, HOME, rede ou serviços externos.
  Recursos mutáveis que sobrevivam entre execuções precisam de gestão própria.
- Ficheiros de dados não analisados não recebem uma prova de imutabilidade.
  O teste que modifica uma fonte analisada é detetado antes de certificar a ronda.
- SIGKILL/falha de máquina pode deixar uma pasta `marta-generation-*` no diretório
  temporário. Essa pasta nunca é usada como checkpoint. A limpeza manual exige
  confirmar que já não há um processo ativo a utilizá-la.
- Backends customizados, incluindo XRepoTest, são recusados com esta opção.
  O XRepoTest tem o seu próprio staging/ambiente e continua sequencial; o seu
  context manager global não passa a ser seguro para workers por esta alteração.

## Custo, proveniência e próximos passos

| Alteração | Benefício | Custo adicional |
|---|---|---|
| Ambiente fixado | Impede trocar o runtime de um projeto por alterações globais de outro | Uma cópia pequena do mapping por projeto; sem histórico/modelos adicionais |
| Preload atómico se mudou | Evita reescritas e leituras de um ficheiro incompleto | Comparação do pequeno helper |
| Workspace opcional | Separa candidatos, scratch files e suite executada | Uma cópia por invocação, staging dos specs por validação e hashes nos limites das rondas |
| Publicação/lock | Evita aceitar candidatos alterados e dois escritores nos mesmos outputs | Comparação do candidato e substituição atómica |

A receita de geração identifica modo de execução e variáveis Ruby numa whitelist;
a fingerprint de análise identifica o ambiente Ruby declarado. O ambiente completo
não é serializado: variáveis secretas arbitrárias não entram no manifesto. As
variáveis LLM continuam separadas, ligadas ao cliente/configuração de pedidos.
Caminhos temporários do workspace não entram na receita. As receitas antigas
não são migradas automaticamente; não se reatribuem resultados dos papers.

Faltam em A5 timers/contadores por worker, uma visão definida dos exemplos
consultáveis, ordenação/coordenação de resultados e commits. Só depois faz sentido
ativar e medir concorrência limitada 1/2/4. A cópia opcional representa um custo de
isolamento, não um ganho de velocidade já demonstrado.

## Verificação offline

`test_execution_isolation.py` exercita ambientes distintos com alterações globais
intercaladas, Prism/sintaxe/RSpec/cobertura, dependências, publicação, alterações de
fontes/candidatos, cancelamento, staging acumulado, rollback, exclusão de outputs,
limpeza e reutilização de uma cópia entre rondas. Usa respostas scriptadas e o
Ruby/RSpec existentes. Não faz inferência, downloads ou instalações.

Validação final: **901 testes locais aprovados**, sete ignorados no host;
**16 testes aprovados no container existente**, incluindo quatro dos ignorados.
Total: **917 aprovados; três permanecem ignorados**. Os avisos de depreciação
Pydantic/Chroma preexistentes não exigiram atualizar pacotes.
