# differential-equations-solverへようこそ

## Characteristic
1. ndarrayを多用することで演算の高速化とシンプルさを実現した。
2. モジュール化してしまうことで演算方法ごとの比較検討がしやすくなった。また、新たな演算方法の追加・削除もしやすくなった。

## Getting started
1. DiffEquSolverをdiffeq_solver.pyからインポートする。
```Python
from diffeq_solver import DiffEquSolver 
```
2. 初期値を設定してインスタンス化する。
```Python
solver = DiffEquSolver(t,h,N,init,func)
```
ここで引数は以下の表の通りである。
|変数名|内容|
|:--:|:--|
|t|演算を開始するtの値|
|h|tの計算上の間隔|
|N|演算する点の数|
|init|初期値。__必ずタプル型で入力__|
|func|演算したい微分方程式|
3. メソッドを使う。オイラー法、改良オイラー法、ルンゲ＝クッタ法の3つが使える。
```Python
result1 = solver.euler() #オイラー法
result2 = solver.fixed_euler() #改良オイラー法
result3 = solver.runge() #ルンゲ＝クッタ法
```
返り値はすべてndarrayである。その列の順番は初期条件を入力した順番に一致している。