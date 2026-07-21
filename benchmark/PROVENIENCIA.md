# Proveniência e seleção do corpus — trilho honesto + metodologia para o paper

*Este documento rastreia de ONDE veio cada projeto e PORQUÊ, distingue o que foi
feito do que é defensável num paper, e propõe a metodologia reprodutível a
adotar. Escrito porque a proveniência é um requisito de revisão (MSR Data
Showcase exige reprodutibilidade da seleção).*

## 1. Trilho real (como as 12 gems chegaram aqui)

| gem | veio de | quando |
|---|---|---|
| money | plano original do utilizador (§1) + 1ª validação (sondagem 1) | 1º lote |
| addressable, ruby-jwt, httparty, i18n, rubyzip | levantamento de 20 gems populares (sondagem 4), medidas via API do GitHub | 1º lote |
| faker | identificada no SWE-bench Multilingual (sondagem 4) **e** no levantamento | 1º lote |
| liquid, kramdown, hashie, public_suffix, chronic | escolhidas **por característica de código** para preencher lacunas de diversidade | 2º lote |
| ~~mustermann~~ | idem, mas excluída (monorepo, sem `lib/` na raiz) | 2º lote |

## 2. ⚠️ A fraqueza metodológica (a ser honesto)

**A seleção foi por juízo de especialista (conhecimento de gems Ruby conhecidas),
NÃO a partir de um universo de amostragem sistemático e reprodutível.** Mesmo o
"levantamento de 20 gems" da sondagem 4 era uma lista escrita à mão. Um revisor
perguntaria, com razão: *"qual foi o universo de amostragem? porque estas e não
outras? como as encontraram?"* — e a resposta atual ("eu conhecia-as") não chega.

## 3. O que SALVA isto: as 12 são objetivamente do topo

Downloads no RubyGems.org (2026-07-19) — **todas entre 129M e 1,4 mil milhões**:

| gem | downloads | | gem | downloads |
|---|---:|---|---|---:|
| i18n | 1 391 M | | httparty | 469 M |
| addressable | 1 225 M | | faker | 333 M |
| public_suffix | 1 197 M | | kramdown | 245 M |
| jwt | 786 M | | liquid | 134 M |
| rubyzip | 763 M | | chronic | 132 M |
| hashie | 471 M | | money | 129 M |

Ou seja: qualquer universo de amostragem objetivo baseado em popularidade
**incluiria estas gems**. A seleção *ad-hoc* calhou a acertar no que uma
seleção sistemática também escolheria — o que permite **retroajustar** a
metodologia sem trocar o corpus.

## 4. Metodologia reprodutível a ADOTAR (para o paper)

Reescrever a seleção como um processo reprodutível que produz (aproximadamente)
este corpus:

1. **Universo de amostragem** (objetivo, citável): gems mais descarregadas do
   RubyGems.org (ou ranking do bestgems.org / Ruby Toolbox). Fixar data e top-N.
2. **Critérios de inclusão** (aplicados e registados, reprodutíveis):
   - é uma *library gem* (não app Rails, não CLI-only);
   - tem suite de testes (RSpec ou Minitest) — para o baseline de comparação humano;
   - instala sem extensões nativas pesadas (`bundle install` limpo);
   - o código parseia sem erros (0 erros de parse — verificado nas 12);
   - commit fixado (pinning) para reprodutibilidade.
3. **Amostragem estratificada por diversidade:** dentro das incluídas, selecionar
   para cobrir o espectro das métricas de `RESULTADOS_diversidade.md` (tamanho,
   metaprogramação, singleton/instância, mixins, duck-typing). Isto justifica
   *quantitativamente* porque estas 12 e não 12 aleatórias.

**Ameaças à validade a declarar no paper:**
- Amostragem enviesada para gems populares (não representa código Ruby "médio").
- Só gems (bibliotecas); apps Rails ficam de fora (instalação pesada — decisão
  explícita, ver sondagem 4).
- ~metade do ecossistema usa Minitest; medir suites humanas exige suporte aos dois.

## 5. Verificação do universo (FEITO — `benchmark/sampling_frame.py`)

Executado a 2026-07-19. Universo objetivo = popularidade no RubyGems (rank de
downloads via bestgems.org + contagem via RubyGems.org). **Todas as 12 gems caem
dentro** (limiar: ≥100M downloads).

| gem | rank (downloads totais) | downloads |
|---|---:|---:|
| i18n | **#6** | 1 391 M |
| addressable | #16 | 1 225 M |
| public_suffix | #19 | 1 197 M |
| jwt | #42 | 786 M |
| rubyzip | #47 | 763 M |
| hashie | #103 | 471 M |
| httparty | #106 | 469 M |
| faker | #152 | 333 M |
| kramdown | #212 | 245 M |
| liquid | #384 | 134 M |
| chronic | #385 | 132 M |
| money | #399 | 129 M |

**Amplitude: #6–#399** de todas as gems Ruby. Critério mais limpo para o paper =
**limiar de downloads (≥100M)**, não top-N estrito (evita o número arbitrário; a
`money`, #399, é o piso a 129M, confortavelmente acima de 100M).

**Redação defensável para o paper:**
> "Partimos das gems Ruby com ≥100M downloads totais no RubyGems.org (data X),
> aplicámos os critérios de inclusão [library gem, suite RSpec/Minitest,
> instalação sem extensões nativas pesadas, 0 erros de parse, commit fixado], e
> selecionámos 12 estratificando pela diversidade de código (Tabela Y)."

## 6. Gap remanescente (honesto)
Verificámos **corpus ⊆ universo**. Para provar 100% ausência de cherry-picking,
faltaria **enumerar TODAS** as gems do universo (≥100M downloads) e mostrar que
lhes aplicámos os critérios — mas o RubyGems/bestgems não expõe a lista top-N
completa por API (só rank por-gem). Mitigação: usar uma lista publicada/snapshot
(ex.: Ruby Toolbox, awesome-ruby) como ponto de partida citável, ou assumir
amostragem intencional (*purposive*) com a diversidade quantificada como
justificação — ambos aceitáveis num Data Showcase se declarados.
