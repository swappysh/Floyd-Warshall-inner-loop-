from pandas import *

inf = 1000
arr = [
  [0,3,8,inf,-4],
  [inf,0,inf,1,7],
  [inf,4,0,inf,inf],
  [2,inf,-5,0,inf],
  [inf,inf,inf,6,0]
]

for k in range(5):
  for i in range(5):
    for j in range(5):
      arr[i][j] = min(arr[i][j],
                     arr[i][k]+arr[k][j])
  print(DataFrame(arr))