#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")"

if [ $# -eq 0 ]; then
    echo "Missing argument: BENCHMARK_FILE"
    exit 1
fi

BENCHMARK=$1
shift

# Ajoute './microbenchs' si le chemin ne contient pas de /
if [[ $BENCHMARK != *"/"* ]]; then
    BENCHMARK="./microbenchs/$BENCHMARK"
fi

# Ajoute un .py s'il n'est pas déja là.
if [[ $BENCHMARK != *.py ]]; then
    BENCHMARK="$BENCHMARK.py"
fi

mkdir -p results
python "$BENCHMARK" "$@"
