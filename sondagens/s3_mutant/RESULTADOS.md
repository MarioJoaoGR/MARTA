# Sondagem 3 — mutant (mutation testing Ruby) na prática

**Data:** 2026-07-22 · **Veredicto: ✅ FUNCIONA — mutation score real obtido; fricções mapeadas**

## O que é (vs mutmut)
O **mutant** é para Ruby o que o **mutmut** é para Python na MARTA: a ferramenta
de *mutation testing* que dá a métrica **mutation score**. Introduz alterações
pequenas no código (mutantes) e verifica se a suite as apanha ("mata") — mede a
*qualidade real* dos testes, para além da cobertura. Mesmo papel, ecossistema
diferente.

## Resultado do teste real (money, subject `Money#hash`)
```
Subjects: 1 · Mutations: 12 · Kills: 11 · Alive: 1
Coverage (mutation score): 91.66% · Runtime: 0.27s (+1.67s killtime)
```
Instalação **isolada** (GEM_HOME próprio, nada no sistema), a correr contra a
suite RSpec humana da money (499 testes, 496 selecionados para o subject).

## Licença
`--usage opensource` **aceite sem conta e sem erro de rede** (mutant 0.16.3,
comercial-com-free-tier-opensource). ⚠️ Confirmar no login node do Deucalion
antes do run (o comportamento offline do nó de computação fica por provar).

## Fricções encontradas (para o harness de métricas)
1. **Locale**: sem `LANG/LC_ALL` UTF-8, o parser rebenta com
   `EncodingError: invalid byte sequence in US-ASCII` (a money tem `€` no
   código). Nos jobs SLURM, exportar `LC_ALL=en_US.UTF-8`.
2. **Integração rspec**: instalado fora do bundle do projeto, o
   `mutant-rspec` não é encontrado pelo require normal — resolve-se com
   `RUBYOPT=-I<mutant_home>/gems/mutant-rspec-X/lib` (ou correndo dentro de um
   bundle sandbox). Documentado o comando exato abaixo.
3. Warning benigno do `parser` gem (ruby 3.4.10 vs 3.4.0-dev) — ignorável.
4. O binário é `mutant-ruby` (o wrapper `mutant` re-executa).

## Comando reproduzível
```bash
GEM_HOME=$MH gem install mutant mutant-rspec --no-document
cd <projeto>
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
GEM_HOME=$MH GEM_PATH="$MH:$(ruby -e 'puts Gem.default_dir')" \
RUBYOPT="-I$MH/gems/mutant-rspec-0.16.3/lib" \
$MH/bin/mutant-ruby run --usage opensource \
  --include lib --require <gem> --integration rspec -- '<Classe#metodo>'
```

## Implicação para o benchmark
Mutation score dos **specs gerados** exige apontar o mutant à *nossa* suite
(marta_specs) em vez da humana — mesmo mecanismo, `--require` + integração rspec
com os nossos ficheiros. A fazer no harness de métricas (pós-geração), por
subject ou por classe (custo: ~44 mutações/s neste exemplo — viável).

## Lições do lado Python (commits do mutmut, jul 2026) — aplicar no harness de mutação Ruby
Não são código portável (mutmut≠mutant), mas são armadilhas já pagas:
1. **Validar o baseline com o comando EXATO do runner** (`bbafc97a`): se a suite
   não estiver verde com *o mesmo comando* que a ferramenta de mutação usa, esta
   aborta e devolve 0 mutantes. → validar `marta_specs` com o comando exato antes.
2. **Distinguir "0 mutantes" de "falhou"** (`a933c30c`): capturar o erro quando o
   total é 0, senão a falha passa por sucesso silencioso.
3. **Flag para limitar a um tool/subject** (`291a3ff2`): permite paralelizar e
   fazer sanity-checks rápidos.
