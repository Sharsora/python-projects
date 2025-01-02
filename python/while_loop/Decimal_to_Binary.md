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
- suppose we want to convert the number 11 to binary
  <img width="1060" alt="image" src="https://github.com/user-attachments/assets/33aa854b-3759-400b-80b5-88630f27d342" />
- now we get the binary number 11 which is 1101
- r = n % 2 and n = n // 2
```
  1
  1
  0
  1
```
- binary = binary * 10 + r
- 1101
```sh
n = int(input('Enter a number'))

bin = 0

while n > 0:
    r = n % 2
    n = n // 2
    bin = bin * 10 + r
```

<img width="1033" alt="image" src="https://github.com/user-attachments/assets/a3a6d3cb-fb74-49dc-b760-46aaafb48083" />

- now we will do the reverse of that number to get the correct number
- The correct binary of 11 is 1011
```sh
n = int(input('Enter a number'))

bin = 0

while n > 0:
    r = n % 2
    n = n // 2
    bin = bin * 10 + r

brev = 0
while bin > 0:
    r = bin % 10
    bin = bin //10
    brev = brev *10 +r

print(brev)
```

# Here we get the issue for the code
- this code runs perfectly for odd numbers but when I Enter even numbers like 10 or 12 output does not show the correct result
- now suppose we have number n = 10
- r = n % 2 and n = n // 2 and binary = binary * 10 + r
- we have value n = 10 so r = 10 % 2 = reminder 0
- n = 10 // 2 = 5
- binary = (initially binary is 0) 0 * 10 + 0 = 0
- now the n = 5, so new value of r = 5 % 2 = reminder 1
- n = 5 // 2 = 2
- binary = (earlier binary value) 0 * 10 + (new value of reminder) 1 = 0 * 10 + 1 = 1

<img width="1011" alt="image" src="https://github.com/user-attachments/assets/5e90d19b-98ad-429d-979d-665515cf0530" />
