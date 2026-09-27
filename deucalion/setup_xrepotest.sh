#!/bin/bash
# Download and validate CPU-only assets. Does not install in the shared home.
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
CODE="$BASE/MARTA"
XROOT="$BASE/xrepotest"
IMAGE="$XROOT/repaired-v2.sif"
REF=dungxg502/xrepotest-ruby@sha256:e7e857ff5c73345a9492a5352a52262da9796a3cb29c5f18053e0be1e8b6924d
REV=39fb6ab3173136d3dac2d38ed7c98baf6c470270
mkdir -p "$XROOT/home" "$XROOT/tmp" "$XROOT/downloads" "$XROOT/reports"
export SINGULARITY_CACHEDIR="$XROOT/downloads/cache"
export SINGULARITY_TMPDIR="$XROOT/tmp"

if [ ! -f "$IMAGE" ]; then
    ARCHIVE="$XROOT/downloads/marta-xrepotest-repaired-v2.tar"
    if [ ! -f "$ARCHIVE" ]; then
        echo "Falta $ARCHIVE. Transferir a imagem Docker validada localmente antes de preparar."
        echo "Não usamos automaticamente a imagem original: o bundle Hanami está incompleto."
        exit 1
    fi
    if [ ! -f "$ARCHIVE.sha256" ]; then
        echo "Falta $ARCHIVE.sha256. Transferir também o checksum criado localmente."
        exit 1
    fi
    (cd "$XROOT/downloads" && sha256sum -c "$(basename "$ARCHIVE").sha256")
    singularity build "$IMAGE.partial" "docker-archive://$ARCHIVE"
    mv "$IMAGE.partial" "$IMAGE"
fi
printf '%s\n' "$REF" > "$XROOT/image-reference.txt"
sha256sum "$IMAGE" > "$XROOT/image-sha256.txt"
if [ ! -d "$XROOT/XRepoTest-$REV" ]; then
    curl --fail --location --retry 3 "https://codeload.github.com/solis-team/XRepoTest/tar.gz/$REV" \
        --output "$XROOT/downloads/upstream.tar.gz"
    tar -xzf "$XROOT/downloads/upstream.tar.gz" -C "$XROOT"
fi

# Reuse only the existing Python runtime and MARTA dependencies. Ruby and the
# project bundles come from the documented repaired image; no old result is bound.
if [ ! -x "$XROOT/python/bin/python" ]; then
    mkdir -p "$XROOT/python"
    singularity exec --cleanenv --home "$XROOT/home:/home/marta" \
        --bind "$XROOT/python:/export" "$BASE/containers/marta_benchmark.sif" \
        cp -a /opt/conda/envs/test4py_env/. /export/
fi

singularity exec --cleanenv --home "$XROOT/home:/home/marta" "$IMAGE" python3 -B -c \
    'import json; d=json.load(open("/opt/xrepo/environment.json")); assert d["schema"] == 1 and len(d["projects"]) == 10; assert d["evaluator"]["revision"] == "coverage-order-and-exact-path-v1"; print("Ambiente corrigido: dez projetos e duas correções de cobertura registados")'

singularity exec --cleanenv --home "$XROOT/home:/home/marta" \
    --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo" \
    --bind "$XROOT/python:/opt/conda/envs/test4py_env:ro" \
    --bind "$BASE/pydeps/marta:/data/pydeps/marta:ro" \
    --env PYTHONPATH=/data/pydeps/marta:/opt/marta \
    "$IMAGE" /opt/conda/envs/test4py_env/bin/python -B -c \
    'import numpy, chromadb, transformers, torch; print("MARTA Python imports: OK; torch", torch.__version__)'

# Always recheck. A downloaded image is not evidence that all bundles work.
singularity exec --cleanenv --home "$XROOT/home:/home/marta" \
    --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo" \
    --env PYTHONPATH=/opt/marta --env PYTHONUNBUFFERED=1 \
    "$IMAGE" python3 -B -m benchmark.xrepotest.prepare \
    --dataset /app/xrepotest/ruby_functions.jsonl \
    --output /data/xrepo/reports/preflight.json

singularity exec --cleanenv --home "$XROOT/home:/home/marta" \
    --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo" \
    --env PYTHONPATH=/app:/opt/marta --env PYTHONUNBUFFERED=1 \
    "$IMAGE" python3 -B -m benchmark.xrepotest.environment.verify \
    --report /data/xrepo/reports/environment-diagnostics.json
