"""Camada 7: seleccao do corpus, com grupos ligados e diversidade.

O problema que esta camada resolve, e que so se viu depois de medir: a MARTA
constroi contexto ENTRE modulos (a 2a passagem dos sumarios anexa o `done_what`
dos metodos chamados, e o `what_todo` propaga-se do chamador para o chamado),
mas esse enriquecimento so funciona quando o chamado TAMBEM e alvo.

Uma seleccao puramente por diversidade escolhe os modulos mais afastados uns dos
outros, ou seja os que menos se chamam. Medido no corpus anterior, de 500
modulos escolhidos so por diversidade:

    49,9% das arestas ficavam dentro do mesmo modulo
     5,1% chegavam a outro modulo do corpus     <- o unico caso que enriquece
    45,0% apontavam para fora do corpus         <- perdidas

Ou seja, a avaliacao desligava metade daquilo que distingue a ferramenta. E nao
e simetrico: uma ferramenta de busca (Pynguin) gera por modulo e nao perde nada
com modulos dispersos.

A correccao NAO e fazer dois corpora, o que tornaria a comparacao confundida.
E fazer UM corpus em dois passos, e etiquetar cada modulo:

    passo 1   OS X MELHORES: o ranking de diversidade (farthest-first) sobre a
              populacao inteira. A ordem de escolha e o ranking: primeiro o que
              mais acrescenta a cobertura das oito caracteristicas.
    passo 2   GRUPOS LIGADOS NO LUGAR DOS PIORES: componentes de 3 a 20 modulos
              com chamadas GARANTIDAS entre si, ordenadas tambem por diversidade.
              Cada grupo entra inteiro, acrescenta so os membros que ainda nao
              estao no corpus, e sai o mesmo numero de modulos do fim do ranking.
              Para quando os modulos de grupos chegam a FATIA_GRUPOS.

"Chamada garantida": recetor certo (sem recetor, self, constante, self.class),
nome resolvido sem adivinhar (ver IndiceEstrito) e o chamado e um metodo-alvo.
As chamadas por duck typing dizem que PODE chamar, e nao contam.

Cada modulo leva `origem` (grupo ou diversidade), `posicao_ranking`,
`relacionado` e `vizinhos_no_corpus` (modulos do corpus com chamada garantida),
para a cobertura poder ser repartida no fim e responder com dados a "o contexto
entre modulos ajuda?".

Antes de tudo, a populacao fica so com codigo do projeto (dentro das pastas de
codigo da gem: lib/, src/, app/, <sub>/lib) e perde os modulos que falham pelo
RSpec da ferramenta (6_carregamento/falham_rspec.csv, ver porta_rspec.py).

O tamanho e a fatia sao decisao do utilizador: MARTA_ORCAMENTO e
MARTA_FATIA_GRUPOS estudam alternativas sem mexer nas constantes.

    python -m benchmark.dataset.camada7_selecao
"""
from __future__ import annotations

import csv
import gzip
import json
import math
import os
import sys
from collections import defaultdict
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, RAIZ)

from marta.ruby_backend.call_graph import StaticCallGraph        # noqa: E402
from marta.ruby_backend.param_types import ProjectTypeIndex      # noqa: E402
from marta.ruby_backend.ruby_ast import _from_json               # noqa: E402


# ------------------------------------------------------- relacoes GARANTIDAS
# O grafo da ferramenta tem arestas de dois tipos. Com recetor certo (sem
# recetor, self, uma constante, self.class) a chamada aponta para UM metodo.
# Com duck typing (variavel local, variavel de instancia, getter) o resolver
# escolhe candidatos pelos metodos usados, ate 5: a aresta diz que PODE chamar.
# Para o corpus, "relacionado" tem de ser garantido, nao possivel.
CERTOS = {"none", "self", "const", "selfclass"}


class IndiceEstrito(ProjectTypeIndex):
    """O indice de tipos da ferramenta, mas sem adivinhar.

    O `_resolve` original, quando o nome nao e exato, fica com a PRIMEIRA classe
    que tenha o mesmo nome curto: numa gem com dois `Base`, `Base.foo` liga a um
    deles a sorte. E o mesmo `_resolve` segue superclasses e mixins, por isso ate
    uma chamada sobre `self` pode apontar para o metodo errado se a heranca passar
    por um nome ambiguo. Aqui um nome so se resolve se for exato ou se o nome
    curto for UNICO na gem; na duvida nao ha aresta.
    """

    def _resolve(self, name):
        if not name:
            return None
        if name in self.classes:
            return name
        if getattr(self, "_curtos", None) is None:
            self._curtos = defaultdict(list)
            for qn in self.classes:
                self._curtos[qn.split("::")[-1]].append(qn)
        cands = self._curtos.get(name.split("::")[-1], [])
        return cands[0] if len(cands) == 1 else None

# MARTA_DATASET_DIR desvia os artefactos para outra pasta. Serve para verificar
# se uma camada reproduz o seu artefacto sem escrever por cima do que esta no
# repositorio (uma verificacao assim ja apanhou ficheiros por engano num commit).
D = os.environ.get("MARTA_DATASET_DIR") or \
    os.path.join(RAIZ, "apresentacao", "demo_dataset")
OUT = os.path.join(D, "7_selecao")

ORCAMENTO = 500          # alvo total (o utilizador fixou 400-600)
FATIA_GRUPOS = 0.5       # metade do orcamento vem de grupos inteiros
# Para estudar alternativas (outro tamanho de corpus, outra fatia de grupos) sem
# mexer nas constantes: usar sempre com MARTA_DATASET_DIR noutra pasta.
ORCAMENTO = int(os.environ.get("MARTA_ORCAMENTO", ORCAMENTO))
FATIA_GRUPOS = float(os.environ.get("MARTA_FATIA_GRUPOS", FATIA_GRUPOS))
MIN_GRUPO, MAX_GRUPO = 3, 20



def pastas_de_codigo():
    """gem -> (raiz do codigo, pastas de codigo relativas a essa raiz).

    As pastas sao as da camada 6 (lib/, src/, app/ e, nos monorepos, <sub>/lib),
    as mesmas que a ferramenta poe no load path. A camada 6 grava-as relativas a
    raiz do CLONE (activesupport/lib); a ferramenta corre com cwd na raiz do
    codigo, por isso passam a relativas a essa raiz (lib)."""
    with open(f"{D}/2_parser/parse.csv", encoding="utf-8") as f:
        raizes = {r["gem"]: (r["raiz_codigo"] or ".") for r in csv.DictReader(f)}
    out = {}
    with open(f"{D}/6_carregamento/gems.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            raiz = raizes.get(r["gem"], ".")
            pref = "" if raiz == "." else raiz.rstrip("/") + "/"
            pastas = []
            for p in r["load_paths"].split():
                if pref and not p.startswith(pref):
                    raise SystemExit(f"{r['gem']}: pasta de carregamento {p} fora da raiz {raiz}")
                pastas.append(p[len(pref):])
            out[r["gem"]] = (raiz, pastas)
    return out


def certificados():
    """As linhas do carregam.csv que sao codigo do projeto e passam na porta RSpec.

    Codigo do projeto: dentro das pastas de codigo da gem (o "src" do Ruby). Fora
    delas ficam exemplos, benchmarks, tarefas de rake, geradores de site e
    configuracao de extensoes, que o projeto nao entrega como codigo.
    Porta RSpec (porta_rspec.py): um modulo que falha pela ferramenta nao pode
    ser alvo, nem membro de grupo.
    Devolve (modulos, contagens do filtro)."""
    fora = set()
    porta = f"{D}/6_carregamento/falham_rspec.csv"
    if os.path.exists(porta):
        with open(porta, encoding="utf-8") as f:
            fora = {(r["gem"], r["ficheiro"]) for r in csv.DictReader(f)}
    pastas = pastas_de_codigo()
    with open(f"{D}/6_carregamento/carregam.csv", encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))
    no_src = [r for r in linhas
              if any(r["ficheiro"].startswith(p.rstrip("/") + "/")
                     for p in pastas[r["gem"]][1])]
    ficam = [r for r in no_src if (r["gem"], r["ficheiro"]) not in fora]
    return ficam, {"carregam_na_camada_6": len(linhas),
                   "fora_das_pastas_de_codigo": len(linhas) - len(no_src),
                   "barrados_pela_porta_rspec": len(no_src) - len(ficam)}


NUMERICAS = ["loc_medio", "pct_singleton", "pct_duck", "mixins_por_classe",
             "profundidade_heranca", "metaprog_por_100", "formas"]


# --------------------------------------------------------------- diversidade
def normaliza(itens, campos):
    """Cada valor vira a sua posicao relativa em [0,1].

    Por POSICAO e nao por min-max: a metaprogramacao vai de 0 a 800 e um so
    modulo extremo esmagava a escala toda.
    """
    for c in campos:
        vals = sorted({float(i[c]) for i in itens})
        pos = {v: (n / (len(vals) - 1) if len(vals) > 1 else 0.0)
               for n, v in enumerate(vals)}
        for i in itens:
            i["_" + c] = pos[float(i[c])]


def distancia(a, b, campos):
    d = sum((a["_" + c] - b["_" + c]) ** 2 for c in campos)
    if a["categoria"] != b["categoria"]:
        d += 1.0                     # pesa como uma caracteristica no maximo
    return math.sqrt(d)


def farthest_first(itens, campos, para):
    """Guloso: semente = o mais tipico, depois sempre o mais afastado do que ja
    foi escolhido. `para(escolhidos)` diz quando chega."""
    centro = {"_" + c: sum(i["_" + c] for i in itens) / len(itens) for c in campos}
    semente = min(itens, key=lambda i: math.sqrt(
        sum((i["_" + c] - centro["_" + c]) ** 2 for c in campos)))
    escolhidos = [semente]
    dmin = {id(i): distancia(i, semente, campos) for i in itens}
    restantes = [i for i in itens if i is not semente]
    while restantes and not para(escolhidos):
        alvo = max(restantes, key=lambda i: dmin[id(i)])
        escolhidos.append(alvo)
        restantes.remove(alvo)
        for i in restantes:
            d = distancia(i, alvo, campos)
            if d < dmin[id(i)]:
                dmin[id(i)] = d
    return escolhidos


# ------------------------------------------------------------ grafos
def _componentes(nos, adj):
    visto, comps = set(), []
    for m in sorted(nos):
        if m in visto:
            continue
        pilha, comp = [m], set()
        while pilha:
            x = pilha.pop()
            if x in comp:
                continue
            comp.add(x)
            visto.add(x)
            pilha.extend(adj[x] - comp)
        comps.append(comp)
    return comps


def grafos():
    """gem -> (componentes certas, adjacencia certa, adjacencia possivel).

    Grafo ao nivel do MODULO, entre modulos que carregam.
      certa     A liga-se a B se um metodo de A chama, com recetor certo e
                resolucao estrita, um metodo de B definido com `def` que nao e
                `initialize` (os que nao levam sumario nao enriquecem nada).
      possivel  qualquer aresta que a ferramenta veja, incluindo duck typing.
    As componentes (para os grupos) usam so a certa.
    """
    carregam = defaultdict(set)
    for r in certificados()[0]:
        carregam[r["gem"]].add(r["ficheiro"])

    porgem = defaultdict(list)
    with gzip.open(f"{D}/2_parser/analise_completa.jsonl.gz", "rt",
                   encoding="utf-8") as f:
        for linha in f:
            d = json.loads(linha)
            if d["gem"] in carregam:
                porgem[d["gem"]].append(d)

    fora = {}
    for gem, ficheiros in porgem.items():
        idx, estrito, metodos, dono = ProjectTypeIndex(), IndiceEstrito(), [], {}
        for d in ficheiros:
            fp = _from_json({"path": d["ficheiro"], "classes": d["classes"],
                             "methods": d["metodos"], "examples": [],
                             "groups": [], "errors": []})
            idx.add_file(fp)
            estrito.add_file(fp)
            for m in fp.methods:
                metodos.append(m)
                dono[m.qualified_name] = d["ficheiro"]
        elig = carregam[gem]
        certa, possivel = defaultdict(set), defaultdict(set)

        def liga(adj, a, b):
            if a in elig and b in elig and a != b:
                adj[a].add(b)
                adj[b].add(a)

        for e in StaticCallGraph.build(metodos, idx).edges:
            liga(possivel, dono.get(e.caller), dono.get(e.callee))
        for e in StaticCallGraph.build(metodos, estrito).edges:
            if e.kind in CERTOS and not e.callee.endswith("#initialize"):
                a, b = dono.get(e.caller), dono.get(e.callee)
                liga(certa, a, b)
                liga(possivel, a, b)
        fora[gem] = (_componentes(elig, certa), certa, possivel)
    return fora


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    mods, filtro = certificados()
    por_chave = {(m["gem"], m["ficheiro"]): m for m in mods}
    print(f"populacao: {len(mods)} modulos ({filtro})")

    print("a construir os grafos por gem (certo e possivel)...", flush=True)
    gs = grafos()
    comps = {gem: v[0] for gem, v in gs.items()}
    for m in mods:
        m["_chave"] = (m["gem"], m["ficheiro"])

    def certos_de(m):
        return {(m["gem"], f) for f in gs.get(m["gem"], ({}, {}, {}))[1].get(m["ficheiro"], ())}

    def possiveis_de(m):
        return {(m["gem"], f) for f in gs.get(m["gem"], ({}, {}, {}))[2].get(m["ficheiro"], ())}

    # etiquetar cada modulo com a sua componente (de arestas certas)
    grupos = []
    for gem, lista in comps.items():
        for n, comp in enumerate(lista):
            cid = f"{gem}#{n}"
            for f in comp:
                if (gem, f) in por_chave:
                    por_chave[(gem, f)]["componente"] = cid
                    por_chave[(gem, f)]["tamanho_componente"] = len(comp)
            if MIN_GRUPO <= len(comp) <= MAX_GRUPO:
                membros = [por_chave[(gem, f)] for f in sorted(comp)
                           if (gem, f) in por_chave]
                if membros:
                    grupos.append({"id": cid, "gem": gem,
                                   "categoria": membros[0]["categoria"],
                                   "membros": membros})
    for m in mods:
        m.setdefault("componente", "")
        m.setdefault("tamanho_componente", 1)
    print(f"componentes de {MIN_GRUPO} a {MAX_GRUPO} modulos: {len(grupos)}, "
          f"{sum(len(g['membros']) for g in grupos)} modulos, "
          f"{len({g['gem'] for g in grupos})} gems")

    # ---- passo 1: os X melhores, pelo ranking de diversidade ----------------
    # O farthest-first escolhe primeiro o modulo que mais acrescenta a cobertura
    # das oito caracteristicas, depois o que mais acrescenta a seguir, e assim por
    # diante: a ORDEM de escolha e o ranking. "Melhor" quer dizer "que mais
    # contribui para a diversidade do corpus"; que o modulo e adequado para gerar
    # testes ja foi garantido pelas camadas 4 a 6.
    normaliza(mods, NUMERICAS)
    ranking = farthest_first(mods, NUMERICAS, para=lambda esc: len(esc) >= ORCAMENTO)
    for pos, m in enumerate(ranking, 1):
        m["posicao_ranking"] = pos
    corpus = list(ranking)
    print(f"passo 1: os {len(corpus)} melhores do ranking de diversidade")

    # ---- passo 2: grupos ligados entram no lugar dos piores ------------------
    # Os grupos (componentes de 3 a 20 modulos com chamadas GARANTIDAS entre si)
    # ordenam-se tambem por diversidade: as caracteristicas de um grupo sao a
    # mediana das dos seus modulos, mais o tamanho. Cada grupo entra INTEIRO e
    # acrescenta so os membros que ainda nao estao no corpus; sai o mesmo numero
    # de modulos, a contar do FIM do ranking. Se um membro ja estava entre os X
    # melhores, nao se repete e sai menos um. Para quando os modulos de grupos
    # chegam a fatia pedida.
    for g in grupos:
        for c in NUMERICAS:
            vals = sorted(float(m[c]) for m in g["membros"])
            g[c] = vals[len(vals) // 2]
        g["tamanho"] = len(g["membros"])
    campos_g = NUMERICAS + ["tamanho"]
    normaliza(grupos, campos_g)
    ordem_g = farthest_first(grupos, campos_g, para=lambda esc: len(esc) >= len(grupos))
    teto = round(ORCAMENTO * FATIA_GRUPOS)

    no_corpus = {m["_chave"] for m in corpus}
    de_grupo, escolhidos_g, ja_estavam, sairam = set(), [], 0, []
    for g in ordem_g:
        if len(de_grupo) >= teto:
            break
        membros = {m["_chave"] for m in g["membros"]}
        novos = [m for m in g["membros"] if m["_chave"] not in no_corpus]
        removiveis = sorted((m for m in corpus
                             if m["_chave"] not in de_grupo and m["_chave"] not in membros),
                            key=lambda m: -m["posicao_ranking"])
        if len(removiveis) < len(novos):
            break
        saem = removiveis[:len(novos)]
        sai = {m["_chave"] for m in saem}
        sairam += saem
        corpus = [m for m in corpus if m["_chave"] not in sai] + novos
        no_corpus = {m["_chave"] for m in corpus}
        de_grupo |= membros
        ja_estavam += len(membros) - len(novos)
        escolhidos_g.append(g)
    n_g = sum(1 for m in corpus if m["_chave"] in de_grupo)
    print(f"passo 2: {len(escolhidos_g)} grupos, {n_g} modulos de grupos "
          f"(fatia pedida {teto}); {ja_estavam} ja estavam entre os melhores; "
          f"sairam {len(sairam)} do fim do ranking")

    # ---- etiquetar ---------------------------------------------------------
    for m in corpus:
        m["origem"] = "grupo" if m["_chave"] in de_grupo else "diversidade"
        m.setdefault("posicao_ranking", "")
        certos = certos_de(m) & no_corpus
        possiveis = possiveis_de(m) & no_corpus
        # vizinhos_no_corpus: modulos do corpus com que ha chamada GARANTIDA
        m["vizinhos_no_corpus"] = len(certos)
        m["ligacoes_possiveis_no_corpus"] = len(possiveis)
        m["relacionado"] = bool(certos)

    # Garantias. Se alguma falhar, para aqui em vez de gravar um corpus que diz
    # uma coisa e e outra.
    assert len(corpus) == ORCAMENTO, f"corpus com {len(corpus)} modulos"
    assert len(no_corpus) == len(corpus), "modulos repetidos no corpus"
    sem_aresta = [m["_chave"] for m in corpus if m["origem"] == "grupo" and not m["relacionado"]]
    assert not sem_aresta, f"modulos de grupo sem chamada garantida: {sem_aresta[:5]}"

    campos = [c for c in mods[0] if not c.startswith("_")]
    for extra in ("componente", "tamanho_componente", "origem", "posicao_ranking",
                  "relacionado", "vizinhos_no_corpus", "ligacoes_possiveis_no_corpus"):
        if extra not in campos:
            campos.append(extra)
    with open(f"{OUT}/corpus.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(corpus, key=lambda m: (m["gem"], m["ficheiro"])))

    with open(f"{OUT}/grupos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["componente", "gem", "categoria", "modulos", "escolhido"])
        esc = {g["id"] for g in escolhidos_g}
        for g in sorted(grupos, key=lambda x: -len(x["membros"])):
            w.writerow([g["id"], g["gem"], g["categoria"], len(g["membros"]),
                        g["id"] in esc])

    # projetos.json: tudo o que o cluster precisa para correr este corpus, num so
    # ficheiro. Nao decide nada de novo, junta o que as camadas anteriores ja
    # decidiram: de onde vem o codigo (camada 2), em que ambiente cada modulo foi
    # certificado (camada 6) e quais sao os alvos (esta camada). O prepare, o
    # verificador e o harness leem todos daqui. Antes havia tres versoes do
    # ambiente, e nenhuma era a que certificou os modulos.
    with open(f"{D}/2_parser/parse.csv", encoding="utf-8") as f:
        origem_codigo = {r["gem"]: r for r in csv.DictReader(f)}
    pastas = pastas_de_codigo()
    with open(f"{D}/6_carregamento/gems.csv", encoding="utf-8") as f:
        receita = {r["gem"]: r for r in csv.DictReader(f)}
    gems_corpus = {m["gem"] for m in corpus}
    # Os modulos que a camada 6 so certificou "com a biblioteca carregada" foram
    # carregados depois de TODA a biblioteca, em tres passagens (rb/ordem.rb).
    # Para os reproduzir e preciso a lista do que se carregou nessas passagens:
    # os modulos da gem que carregam. Vai so para as gems que tem algum alvo
    # nesse modo, para o manifesto nao crescer sem uso.
    # A lista e EXATAMENTE a que o ordem.rb recebeu: todos os modulos da gem que
    # entraram na camada 6, incluindo os que falharam isolados, menos os que
    # morreram abruptamente ou por timeout. Usar so os que carregaram deixava de
    # fora o brakeman/util.rb, sem o qual o template_parser nao carrega.
    carregados = defaultdict(list)
    with open(f"{D}/6_carregamento/carregam.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            carregados[r["gem"]].append(r["ficheiro"])
    with open(f"{D}/6_carregamento/falham.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("erro", "").startswith(("saida abrupta", "timeout")):
                carregados[r["gem"]].append(r["ficheiro"])
    codigo = defaultdict(list)
    with gzip.open(f"{D}/2_parser/analise_completa.jsonl.gz", "rt",
                   encoding="utf-8") as f:
        for linha in f:
            d = json.loads(linha)
            if d["gem"] in gems_corpus:
                codigo[d["gem"]].append(d["ficheiro"])
    projetos = {"_gerado": f"camada 7, {date.today()}"}
    for gem in sorted(gems_corpus):
        o, r = origem_codigo[gem], receita[gem]
        raiz, load_paths = pastas[gem]
        projetos[gem] = {
            "repo": o["repo_usado"], "etiqueta": o["etiqueta"],
            "commit": o["commit"], "raiz": raiz,
            "ambiente": r["ambiente"], "deps": r["deps"].split(),
            "load_paths": load_paths,
            # A porta de entrada só vai para o manifesto se a camada 6 a tiver
            # ABERTO. A doorkeeper tem porta (`doorkeeper`) que rebenta com
            # NoMethodError: mattr_reader — a camada 6 registou porta_abriu=False
            # e certificou os modulos sem ela. Carregá-la a força mataria a
            # execucao desses modulos, por uma decisao nossa e nao do codigo.
            "entrada": "" if (r["entrada"] in ("", "(sem porta)")
                              or r["porta_abriu"] != "True") else r["entrada"],
            "ficheiros_codigo": sorted(codigo[gem]),
            "biblioteca": sorted(carregados[gem]) if any(
                m["gem"] == gem and m["modo"] != "isolado" for m in corpus) else [],
            "alvos": [{"ficheiro": m["ficheiro"], "modo": m["modo"],
                       "origem": m["origem"], "componente": m["componente"],
                       "relacionado": m["relacionado"],
                       "vizinhos_no_corpus": m["vizinhos_no_corpus"],
                       "metodos": int(m["metodos"])}
                      for m in sorted(corpus, key=lambda x: x["ficheiro"])
                      if m["gem"] == gem],
        }
    with open(f"{OUT}/projetos.json", "w", encoding="utf-8") as f:
        json.dump(projetos, f, indent=1, ensure_ascii=False)

    com = sum(1 for m in corpus if m["vizinhos_no_corpus"] > 0)
    funil = {
        "data": str(date.today()),
        "orcamento": ORCAMENTO, "fatia_grupos": FATIA_GRUPOS,
        "grupo_min": MIN_GRUPO, "grupo_max": MAX_GRUPO,
        **filtro,
        "populacao": len(mods),
        "componentes_elegiveis": len(grupos),
        "grupos_escolhidos": len(escolhidos_g),
        "modulos_de_grupos": n_g,
        "membros_de_grupo_ja_entre_os_melhores": ja_estavam,
        "sairam_do_fim_do_ranking": len(sairam),
        "modulos_do_ranking": len(corpus) - n_g,
        "corpus": len(corpus),
        "gems": len({m["gem"] for m in corpus}),
        "categorias": len({m["categoria"] for m in corpus}),
        "metodos": sum(int(m["metodos"]) for m in corpus),
        "relacionados": com,
        "relacionados_vindos_do_ranking": sum(1 for m in corpus
                                              if m["origem"] == "diversidade" and m["relacionado"]),
        "sem_chamada_garantida_no_corpus": len(corpus) - com,
    }
    with open(f"{OUT}/funil.json", "w", encoding="utf-8") as f:
        json.dump(funil, f, indent=2, ensure_ascii=False)
    print("\n" + json.dumps(funil, indent=1))


if __name__ == "__main__":
    main()
