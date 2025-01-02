- The number of the prime means a number that can be divisible by 1 and the number itself only
- so need to count the factors and how many factors are exactly dividable
- only 2 factor then the number is a prime number

<img width="1065" alt="image" src="https://github.com/user-attachments/assets/969bb9ed-e2e8-432d-9324-edb393c7645e" />

```sh
n = int(input('Enter a Number'))

count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print('Its a Prime')
else:
    print('Its Not a Prime')
```
