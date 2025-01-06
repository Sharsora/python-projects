<img width="1062" alt="image" src="https://github.com/user-attachments/assets/bf120991-4fc4-437a-abd3-f0531950bc59" />


```sh

L1 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

L2 = [[5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8]]

L3 = []

for i in range(3):
    s = []
    for j in range(4):
        r = L1[i][j] + L2[i][j]
        s.append(r)
    L3.append(s)

print(L3)
```
