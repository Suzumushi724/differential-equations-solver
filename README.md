# differential-equations-solverへようこそ

## Basic Information
## Getting started
1. DiffEquSolverをdiffeq_solver.pyからインポートする。
```Python
from diffeq_solver import DiffEquSolver 
```
2. 初期値を設定してインスタンス化する。
```Python
solver = DiffEquSolver(t,h,N,init,func)
```