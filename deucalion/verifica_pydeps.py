"""Os pydeps têm as versões que o requirements.txt fixa?

Os pydeps foram instalados uma vez com `pip install --target` (ver README), e o
requirements.txt pode ter mudado desde então. Uma versão diferente não dá erro no
arranque: dá comportamento diferente a meio de uma corrida de horas. Lê as versões
pelo mesmo sys.path que o job usa (PYTHONPATH com os pydeps à frente).

    python deucalion/verifica_pydeps.py requirements.txt
"""
import importlib.metadata as md
import re
import sys

diferentes, faltam = [], []
for linha in open(sys.argv[1], encoding="utf-8"):
    linha = linha.split("#", 1)[0].split(";", 1)[0].strip()
    if "==" not in linha:
        continue
    nome, versao = (x.strip() for x in linha.split("==", 1))
    nome = re.sub(r"\[.*\]", "", nome)
    try:
        instalada = md.version(nome)
    except md.PackageNotFoundError:
        faltam.append(f"{nome}=={versao}")
        continue
    if instalada != versao:
        diferentes.append(f"{nome}: pedida {versao}, instalada {instalada}")

for x in faltam:
    print(f"  falta     {x}")
for x in diferentes:
    print(f"  diferente {x}")
if faltam or diferentes:
    print(f"❌ {len(faltam)} em falta, {len(diferentes)} com versão diferente: reinstalar os pydeps (README, passo 4)")
    sys.exit(1)
print("✅ pydeps iguais ao requirements.txt")
