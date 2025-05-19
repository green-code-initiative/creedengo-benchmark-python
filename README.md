# Python µBenchmarks

Microbenchmarks that (in)validate CreednGo rules.

This repository is a [`uv`](https://docs.astral.sh/uv/) project that depends on the [`pybench` benchmarking toolkit](https://pyperf.readthedocs.io/en/latest/index.html).

## Caution required

Rules often suggest an alternative way of writing small pieces of code.
Measuring the effect of a small and isolated amount of code is hard, we need to be cautious.

CPython (the default implementation of Python) does not (as of may 2025) have a complex AOT (ahead of time) compiler like C or Rust, nor a complex JIT (just in time) compiler like Java, which means that you will probably not get your code removed by an optimization.
However:

- It is still non-trivial to create reproducible benchmarks. See [How to get reproducible benchmark results](https://pyperf.readthedocs.io/en/latest/run_benchmark.html#how-to-get-reproducible-benchmark-results).
- Some Python implementations _do_ have an advanced JIT compiler, for example PyPy or GraalPy. See [JIT compilers](https://pyperf.readthedocs.io/en/latest/run_benchmark.html#jit-compilers)

## Required tools

To run or create benchmarks, you need `uv` and python (uv will install/find it for you).
See [Installing uv](https://docs.astral.sh/uv/getting-started/installation/) to setup your environment easily.

To load the project and its dependencies, run:

```sh
uv sync
```

A virtualenv will be automatically created for you.

## Writing a new benchmark

- Create a new file in `microbenchs`.
- In your main, use one of the following methods of `pyperf.Runner` to compare different scenarios:
  - `bench_func` ([doc](https://pyperf.readthedocs.io/en/latest/examples.html#bench-func-method)).
  - `timeit` ([doc](https://pyperf.readthedocs.io/en/latest/examples.html#timeit-method)).
  - `bench_time_func` ([doc](https://pyperf.readthedocs.io/en/latest/examples.html#bench-time-func-method)).

See [`example.py`](microbenchs/example.py).

## Running one/multiple benchmark(s)

Each benchmark file is a Python script that accepts arguments (thanks to `pyperf.Runner`).

Use the `bench.sh` script, which is a small wrapper around that.
Run `./bench.sh example.py --help` too see the available PyPerf options.

To run a single benchmark file:

```sh
./bench.sh filename
```

The benchmark results are printed to stdout and stored in [`results/{benchmark}.json`](results/example.py.json).
