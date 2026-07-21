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

## 5. Ação pendente
Executar o passo 1-2 a sério: puxar o ranking de downloads do RubyGems, aplicar
os critérios programaticamente, e confirmar que o corpus cai dentro do top-N.
Assim a frase do paper passa a "selecionámos de entre as N gems mais
descarregadas que cumprem [critérios], estratificando por [métricas]", com
script reprodutível — em vez de "escolhemos estas".
