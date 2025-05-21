#!/usr/bin/env python3
# Rules : GCI105 StringConcatenation #Python #DLG #RulesSpecifications #389
# Comment : 
#  check if the rules is good for the planet
#  control if there is other good pratice or new evolution which can change the rule
#  mesure benefice
import pyperf
from pathlib import Path
from helpers import *

CONST_CITY = 'New York'
CONST_STREET = '5th Avenue'
CONST_ZIP_CODE = '10001'

def not_compliant(it):
    city = CONST_CITY
    street = CONST_STREET
    zip_code = CONST_ZIP_CODE
    str_it = str(it)
    address = city + ', ' + street + ', ' + zip_code + ', ' + str_it        # Noncompliant: inefficient string concatenation : + on 1 line
    return address

def not_compliant2(it):
    city = CONST_CITY
    street = CONST_STREET
    zip_code = CONST_ZIP_CODE
    str_it = str(it)
    address = ''
    address += city
    address += ', '
    address += street
    address += ', '
    address += zip_code
    address += ', '
    address += str_it                                                       # Noncompliant2: inefficient string concatenation : += 7 times
    return address

def compliant(it):
    city = CONST_CITY
    street = CONST_STREET
    zip_code = CONST_ZIP_CODE
    str_it = str(it)
    address = f"{city}, {street}, {zip_code}, {str_it}"                     # compliant : syntaxe f"{...}..."
    return address

def compliant2(it):
    # or using str.join() for multiple string concatenations
    str_it = str(it)
    parts = [CONST_CITY, CONST_STREET, CONST_ZIP_CODE, str_it]
    address = ', '.join(parts)                                              # compliant : syntaxe ', '.join(parts)
    return address

def main():
    runner = pyperf.Runner()
    benchmarks = []
    sizes = [10, 10_000, 1_000_000]
    for size in sizes:
        func_args = size

        res = runner.bench_func(f"not_compliant_{size}", not_compliant, func_args)
        if res:
            benchmarks.append(res)

        res = runner.bench_func(f"not_compliant2_{size}", not_compliant2, func_args)
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
