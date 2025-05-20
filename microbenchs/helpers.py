import inspect
from pathlib import Path
from typing import Optional
from pyperf import Benchmark, BenchmarkSuite

BENCH_ROOT_DIR = Path(__file__).parent
RESULTS_DIR = BENCH_ROOT_DIR.parent.joinpath("results")

def _result_file_path(*local_names: str) -> Path:
    caller_path = inspect.stack()[2][1]
    caller_path = Path(caller_path).relative_to(BENCH_ROOT_DIR)
    sanitized_path = str(caller_path).replace("/", "_")
    joined_args = ":".join(local_names)
    if joined_args:
        joined_args = f":{joined_args}"
    return RESULTS_DIR.joinpath(f"{sanitized_path}{joined_args}.json")

def save_bench_result(bench: Optional[Benchmark | BenchmarkSuite], *local_names: str) -> None:
    if bench is not None:
        file=_result_file_path(*local_names)
        # print(f"saving to {file}")
        RESULTS_DIR.mkdir(exist_ok=True)
        bench.dump(str(file), replace=True)
    # else:
    #     print(f"nothing to save")
