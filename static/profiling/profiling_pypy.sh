pypy3 -m cProfile -o output_profiling_pypy ../Chess.py
pypy3 pstats_profiling.py > result_profiling_pypy