## 1. Find the sum of the number given as the Input
<img width="1067" alt="image" src="https://github.com/user-attachments/assets/bce5c917-3822-448a-b837-ac43f0da34c4" />

```sh
num_of_nos = int(input('Enter number of number'))
sum = 0
count = 0

while count < num_of_nos:
    n = int(input('Enter a number'))
    sum = sum + n
    count = count + 1

print('Sum is :', sum)
```

## 2. Find the sum of positive and negative numbers
- here we have to check for a positive number and then sum the positive number
- now check the negative number and then the sum of the negative numbers

```sh
num_of_nos = int(input('Enter number of number'))
Psum =0
Nsum = 0
count = 0

while count < num_of_nos:
    n = int(input('Enter a number'))
    if n > 0:
       Psum = Psum + n
    else:
       Nsum = Nsum + n
    count = count + 1

print('positive sum is :', Psum)
print('Negative sum is :', Nsum)
```

## 3. Find the maximum number from the given numbers
- here we need to maintain the variable max, when the code reads numbers, max will assign that value.
- suppose the number is 69112, so first read the number 6 so the max is assigned 6, now the second number is 9 so modify the max value to 9, next number is 11 so it is bigger than 9 so modify value to 11.
- - next number is 2 which smaller then already assigned value of max 11, so max will not change
<img width="1064" alt="image" src="https://github.com/user-attachments/assets/f9d0ed9f-b62a-4e5a-89ad-d3221ba63f71" />

```sh
num_of_nos = int(input('Enter number of number'))

count = 0
max = int(input('Enter a number'))

while count < num_of_nos - 1:
    n = int(input('Enter a number'))
    if n > max:
       max = n
    count = count + 1

print('max number is :', max)
```

## 4. Conver a Decimal number to Binary 
- 
