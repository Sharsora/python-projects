<img width="992" alt="image" src="https://github.com/user-attachments/assets/4822fb63-da51-471a-bc67-619b02e4eb27" />

```sh

L1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'A', 'B', 'A']

result = []

for x in L1:
    cnt = L1.count(x)

    if (x, cnt) not in result:
        result.append((x,cnt))

print(result[0:2])
```

```sh
L1 = ['A', 'B', 'C', 'D', 'A', 'B', 'E', 'F', 'D', 'B', 'E']

result = []

for x in L1:
    if x not in result:
        result.append(x)
        count = L1.count(x)
        result.append(count)

print(result)
```
output
```sh
sharsora@SHARSORA-M-G1WP python-practise % python3 occurrences.py 
['A', 2, 'B', 3, 'C', 1, 'D', 2, 'E', 2, 'F', 1]
sharsora@SHARSORA-M-G1WP python-practise %
```
