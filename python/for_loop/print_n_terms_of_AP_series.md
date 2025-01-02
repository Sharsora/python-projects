- AP means arithmetic progressions
- for example:
  `4,9,14,19,24,29,34,39` - 8 terms
  - here a = 4,
  - difference d = 5
  - number of terms n = 8
 

<img width="1049" alt="image" src="https://github.com/user-attachments/assets/c9c0b65e-b3e4-41ec-a0f2-de99e01caceb" />


```sh
a = int(input('Enter initial term'))
d = int(input('Enter common Difference'))
n = int(input('Enter Number of Terms'))

for t in range(a, a + n * d, d):
    print(t)
```
