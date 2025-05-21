#!/usr/bin/env python3
import pyperf
from helpers import *

global_counter = 0

def increment_global(n):
    global global_counter # Variable globale
    global_counter = 0
    for _ in range(n):
        global_counter += 1 
    return global_counter

def increment_local(n):
    local_counter = 0  # Variable locale
    for _ in range(n):
        local_counter += 1
    return local_counter

def main():
    runner = pyperf.Runner()
    benchmarks = []
    sizes = [1000]
    for size in sizes:
        func_args = size

        res = runner.bench_func(f"global_{size}", increment_global, func_args)
        if res:
            benchmarks.append(res)

        res = runner.bench_func(f"local_{size}", increment_local, func_args)
        if res:
            benchmarks.append(res)

    suite = pyperf.BenchmarkSuite(benchmarks)
    save_bench_result(suite)

main()
