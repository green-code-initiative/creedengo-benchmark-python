
import time
import pyperf
from helpers import *

# Déclaration de la variable globale
global_counter = 0

def increment_global(n):
    global_counter = 0
    for _ in range(n):
        global_counter += 1 
    return global_counter

# Declaration de la variable locale

def increment_local(n):
    local_counter = 0  # Variable locale
    for _ in range(n):
        local_counter += 1
    return local_counter

# Comparaison des performances
def main():
    runner = pyperf.Runner()
    benchmarks = []
    increments = [10, 1_000, 1_000_000]
    for inc in increments:
         func_args = inc
         res = runner.bench_func(f"global{inc}", increment_global, func_args)
         if res:
            benchmarks.append(res)
         res = runner.bench_func(f"local{inc}", increment_local, func_args)
         if res:
            benchmarks.append(res)
    suite = pyperf.BenchmarkSuite(benchmarks)
    save_bench_result(suite)
    
    
main()

