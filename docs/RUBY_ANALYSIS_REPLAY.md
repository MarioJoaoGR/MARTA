# Retoma explícita de análise por prefixo

Entrega de 6 de novembro de 2026. Evita repetir pedidos de análise já aceites
quando uma análise nativa termina incompleta. Não altera o protocolo de retoma
de rondas de geração ou o executor XRepoTest.

## Uso e benefício

Na CLI Ruby nativa, repetir a configuração original e acrescentar:

```text
--resume_analysis /caminho/do/output/run_results/analysis_runs/analysis_<id>
```

Também aceita `--resume-analysis`. Na API:

```python
await project.analyze_summaries(ask=ask, resume_analysis=archive_path)
```

`project.last_analysis_archive` identifica o arquivo da última tentativa, mesmo
quando falha. Na CLI, os arquivos/manifestos ficam em `run_results/analysis_runs`
do output respetivo. Escolher explicitamente o arquivo incompleto pretendido;
a ferramenta não procura automaticamente um arquivo nem escolhe respostas.

Uma análise que já concluiu 100 pedidos e falhou no seguinte pode reutilizar os
100 sem invocar novamente o cliente LLM, se todos os controlos coincidirem.
O pedido sem resposta aceite é executado normalmente na nova tentativa. Isto
não acrescenta retries internos nem muda limites/tokens/configuração para obter
uma resposta melhor.

## Que arquivos e respostas podem entrar

Só journals novos `analysis-journal-v2`, de análises com cache habilitada e estado
`failed`, `interrupted` ou `running` **sem escritor ativo**. Um status running pode
ficar de um processo morto; o lock POSIX, não apenas esse texto, verifica se há
um escritor. Arquivos antigos ou de análises completas não servem de fonte.
Bundles completos continuam a ter o mecanismo normal de cache.

Antes de reutilizar, exige a mesma proveniência/configuração, fontes, README,
modelo/parâmetros declarados, braço do grafo e ordem das identidades de análise.
Uma referência explícita à primeira passagem, quando usada, também tem de manter
o caminho/hash registados. Não atesta pesos ocultos nem comportamento não declarado
de callbacks: conserva os limites de proveniência já existentes.

Depois exige o **mesmo prefixo de pedidos**, pela ordem:

- Hash das mensagens sistema/utilizador.
- Fase e contexto registado.
- Sequência contígua e hash da resposta aceite.
- Resposta string não vazia, sem erro do pedido, segundo o contrato nativo atual.

Esse último controlo não é uma prova de correção semântica do sumário. Não se
acrescentou um judge ou um critério de qualidade para escolher respostas.
Pedidos repetidos com mensagens iguais conservam as suas ocorrências/respostas
separadas, em vez de colapsarem numa cache por hash.

O primeiro pedido falhado/inválido não é reutilizado. Uma última linha incompleta
pode ser descartada após uma interrupção; linhas completas corrompidas, buracos
ou respostas depois de uma falha são recusados. Estes hashes detetam alterações
acidentais e ligam a auditoria aos bytes lidos; não são assinatura/autoria digital.

Se um pedido divergir, a retoma para antes de delegar esse pedido ao modelo.
Não salta para outra resposta do arquivo e não publica um bundle incompleto.
Um arquivo de retoma recusada não se torna uma nova fonte para contornar essa
recusa.

## Interrupção de uma retoma

Cada tentativa cria um arquivo independente. O original é lido sem sobrescrita;
o novo journal regista as respostas reutilizadas com arquivo/posição de origem.
Depois de consumir todo o prefixo antigo, pode acrescentar novos pedidos normais.
Se voltar a falhar nessa fase, o novo arquivo pode servir de fonte e conserva o
prefixo lógico inteiro, incluindo o que veio da tentativa anterior.

Se a interrupção ocorrer **antes de preservar todo o prefixo herdado**, o arquivo
novo não pode encurtar esse histórico para voltar a gerar o resto. A ferramenta
recusa-o e indica que se deve retomar o arquivo original intacto. Não há leitura
recursiva automática de cadeias de arquivos.

Antes de publicar o bundle/cache, verifica que o prefixo foi totalmente consumido,
além dos checks de fontes/proveniência existentes. A opção explícita não troca
silenciosamente para um bundle completo encontrado entretanto.

## Custos e compatibilidade

`requests` no manifesto conta novas tentativas delegadas pelo fluxo; respostas
reutilizadas ficam em `replayed_requests` e em eventos `analysis_request_reused`.
Não entram como novas chamadas/tokens LLM no recorder. O custo original permanece
nos artefactos da tentativa de origem; o relatório da nova tentativa não representa
sozinho o custo acumulado de todas as tentativas. Providers com caching/retries
próprios conservam os limites da sua telemetria.

Por omissão não se lê nenhum arquivo de recuperação. Os journals normais ganham
sequência, marca de aceitação, hash da resposta e um lock de escritor. Não há
novo modelo, embedding, processo de fundo ou instalação. A recuperação opcional
lê o journal para validar o prefixo e mantém respostas pendentes em memória,
libertando-as da fila à medida que as consome. Acrescenta IO/validação; evita os
pedidos aceites repetidos. Não se promete uma aceleração global medida.

`--no_cache`/`use_cache=False` é incompatível com recuperação explícita e continua
a recalcular sem ler bundles ou referências da primeira passagem. Arquivos dessa
configuração também não são fonte de recuperação. `--evaluate_only` não aceita
a flag. O reaproveitamento já existente da primeira passagem pode compor-se com
a retoma quando a referência corresponde exatamente.

Não se migram arquivos antigos nem resultados congelados. O adapter XRepoTest
mantém os checkpoints próprios; a nova flag não foi ligada aos seus launchers ou
usada para retomar experiências dos papers.

## Verificação

Fixtures com clientes simulados cobrem redução de chamadas, contagem separada,
arquivo original intacto, falha de transporte e resposta vazia, cache completa,
alterações de inputs/modelo/ordem, journal corrompido ou truncado, escritor ativo,
retomas encadeadas, falha ao gravar bundle, referência de primeira passagem,
`--no_cache` e encaminhamento pela CLI. Não houve inferência real.

Validação final: **1164 testes locais aprovados**, seis ignorados no host;
**16 aprovados no contentor existente**, incluindo quatro daqueles ignorados.
Total: **1180 aprovados; dois permanecem ignorados**. Sem chamadas a modelos,
downloads, instalações ou jobs no cluster.
