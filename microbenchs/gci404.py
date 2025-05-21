#!/usr/bin/env python3
import pyperf
from helpers import *

# global variable so that the loop performs a dummy operation instead of nothing
# (which could be optimized away by the runtime)
GLOBAL = 0

def non_compliant(n):
    global GLOBAL
    for x in [y for y in range(n)]:
        GLOBAL = x

def compliant(n):
    global GLOBAL
    for x in (y for y in range(n)):
        GLOBAL = x

def compliant2(n):
    global GLOBAL
    for x in range(n):
        GLOBAL = x

def main():
    runner = pyperf.Runner()
    benchmarks = []
    sizes = [10, 100, 10_000, 1_000_000]
    for size in sizes:
        func_args = size

        res = runner.bench_func(f"non_compliant{size}", non_compliant, func_args)
        if res:
            benchmarks.append(res)

        res = runner.bench_func(f"compliant_{size}", compliant, func_args)
        if res:
            benchmarks.append(res)

        res = runner.bench_func(f"compliant2_{size}", compliant2, func_args)
        if res:
            benchmarks.append(res)

    suite = pyperf.BenchmarkSuite(benchmarks)
    save_bench_result(suite)

main()
