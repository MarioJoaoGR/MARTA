# Dependências do projeto e outputs separados

Entrega de 6 de novembro de 2026. Corrige o âmbito do snapshot de dependências
usado na retoma, nos workspaces nativos e na avaliação pós-geração.

## Problemas reproduzidos

O scanner de `Gemfile`, `Gemfile.lock` e `*.gemspec` já evitava várias árvores
irrelevantes, mas entrava em `run_results` e num `output_root` interno com nome
customizado. Um `Gemfile.lock` de uma cópia arquivada podia passar a constar como
uma dependência do projeto.

Isso tinha duas consequências:

- Adicionar/alterar arquivos de resultados podia mudar a receita de geração e
  provocar arquivo/reinício desnecessário em vez de retomar a execução concluída.
- A execução isolada excluía o output da cópia, mas o seu snapshot podia exigir
  encontrar ali o lockfile arquivado. Um controlo reproduziu a falha
  `Workspace input changed during execution: artifacts/old-copy/Gemfile.lock`
  antes de qualquer pedido ao modelo.

## Âmbito implementado

`dependency_files(root, output_root=...)` poda as árvores excluídas **antes de
as percorrer**, em vez de ler todos os ficheiros e só depois filtrar resultados.

1. Conserva as exclusões anteriores: diretórios ocultos, `vendor`, `node_modules`,
   `marta_specs`, `rejected_specs` e symlinks para diretórios não são percorridos.
2. Exclui os diretórios de outputs MARTA na raiz, incluindo `run_results`.
3. Exclui um `output_root` explícito quando é uma pasta distinta dentro do projeto.
   A comparação é pelo caminho exato: excluir `out/current` não exclui
   `out/current_extra`.
4. Um output igual à raiz, externo ou ancestral não faz excluir o projeto inteiro.
5. Conserva declarações de subprojetos normais. Por exemplo,
   `component/run_results/Gemfile.lock` continua a contar quando não está sob um
   output explicitamente reservado nem uma das exclusões anteriores.

O scanner mantém a forma relativa/absoluta dos caminhos devolvidos ao chamador.
A identificação do output também foi verificada com a raiz acessível por symlink;
isto não remove as restrições próprias dos workspaces isolados sobre symlinks.

Geração, snapshots da execução isolada e avaliação fornecem o mesmo output à
recolha de declarações. `MARTA_OUTPUT_DIRS` partilha os nomes reservados da raiz
entre scanner e cópias. A cópia de avaliação deixa de remover recursos de um
subprojeto só porque uma pasta interna se chama `run_results`/`marta_specs` e
passa a excluir os `rejected_specs` da raiz, como o workspace de geração.

A avaliação continua a preparar explicitamente os testes gerados depois da
cópia: excluí-los da árvore original não os retira da suite avaliada.

## Retoma e validade

Um teste de integração gera uma ronda, adiciona um lockfile dentro de um arquivo
de resultados e retoma sem novos pedidos ao modelo. Outro confirma que alterar
um lockfile real de um componente continua a mudar a receita. Assim, não se
resolve a falha ignorando todas as declarações de dependências.

A política `project-declarations-v2` fica identificada na receita de geração,
no evento de workspace e no manifesto da avaliação. A implementação do scanner
entra também no manifesto da avaliação. O formato dos checkpoints de rondas e
as fórmulas das métricas mantêm-se; não se migram receitas históricas. Para
experiências independentes ou resultados dos papers, conservar o código/output
original e usar um output novo com esta implementação.

## Custo e limites

Não há instalações, resolução de dependências, embeddings ou novos pedidos LLM.
O scanner faz comparações adicionais de âmbito e deixa de visitar as árvores de
output excluídas. Um controlo regista os diretórios efetivamente visitados e
confirma a poda antes da descida. Não foi medido um ganho global de tempo.

`output_root` deve designar outputs, não uma árvore de dependências de produção.
Fontes e ficheiros de biblioteca explicitamente fornecidos continuam a receber
os seus próprios checks; esta correção não elimina essas entradas só por estarem
num caminho de output. Configurações contraditórias podem continuar a falhar na
cópia/validação, em vez de serem aceites silenciosamente.

O snapshot cobre as declarações encontradas segundo este âmbito. Não é uma
atestação de todas as gems instaladas, ficheiros de configuração externos ou
dependências carregadas dinamicamente em runtime. As exclusões anteriores não
foram convertidas num resolver universal de Bundler.

## Verificação

Fixtures cobrem arquivos de resultados, outputs internos, limites de prefixo,
outputs iguais/externos/ancestrais, subprojetos, raízes relativas e por symlink,
retoma sem novos pedidos, alterações reais de lockfiles, cópia de recursos e
âmbito registado no manifesto de avaliação. Os dois casos iniciais falharam
antes da correção e passaram depois; não são medições de qualidade no benchmark.

Validação final: **1131 testes locais aprovados**, seis ignorados no host;
**16 aprovados no contentor existente**, incluindo quatro daqueles ignorados.
Total: **1147 aprovados; dois permanecem ignorados**. Sem chamadas a modelos,
downloads, instalações ou jobs no cluster.
