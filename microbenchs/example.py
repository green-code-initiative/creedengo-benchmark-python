#!/usr/bin/env python3
import pyperf
from pathlib import Path
from helpers import *

def doubled_comprehension(vec):
    return [x*2 for x in vec]

def doubled_manual(vec):
    output = []
    for i in range(len(vec)):
        output.append(vec[i]*2)
    return output


def main():
    runner = pyperf.Runner()
    benchmarks = []
    sizes = [10, 10_000]
    for size in sizes:
        func_args = [i for i in range(size)]

        res = runner.bench_func(f"doubled_comprehension_{size}", doubled_comprehension, func_args)
        if res:
            benchmarks.append(res)

        res = runner.bench_func(f"doubled_manual_{size}", doubled_manual, func_args)
        if res:
            benchmarks.append(res)

    suite = pyperf.BenchmarkSuite(benchmarks)
    save_bench_result(suite)

main()
