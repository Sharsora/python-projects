- adding the previous two terms we got a new term
example: `0,1,1,2,3,5,8,13,21,34` - 10 terms
a = first
b = second
c = a + b

<img width="1057" alt="image" src="https://github.com/user-attachments/assets/001429ab-dd6c-44d3-9ca2-d3ef63cd871f" />

```sh

n = int(input('Enter Number of Terms'))
a = 0
b = 1

for i in range(n+1):
    print(a)
    c = a + b
    a = b
    b = c
```
