<img width="810" alt="image" src="https://github.com/user-attachments/assets/ed9a641c-25d0-4c68-8811-94899e33c62d" />

```sh
L1 = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]

L2 = []

for x in L1:
    if x not in L2:
        L2.append(x)

print(L2)
```

<img width="975" alt="image" src="https://github.com/user-attachments/assets/fc546f85-8616-4955-919d-b74f5793e33d" />

- without using another variable L2

```sh
l1 = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]

for i in range(len(l1) - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if l1[i] == l1[j]:
            l1.pop(i)
            break  # Break the inner loop after removing the duplicate

print(l1)  # Output: [3, 5, 7, 9, 6, 2, 10] 

```
