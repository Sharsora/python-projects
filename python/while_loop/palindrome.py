
# 1. Counting the number of digits in a number
# if you divide the number using floor division the last number will be removed from the given number. Suppose number n = 12359 and if you do n // 10 = 1235, 9 will be removed because in floor division you will not get .9
# and we will count till the number becomes 0 

n = int(input('Enter a Number'))
counter = 0

while n > 0:
    n = n // 10
    counter += 1

print('Number of digits are: ', counter)

# 2. Find the sum of digits in a number
# Using the modular we can get the last digit of a number, suppose number n = 12359 then r = n % 10 = 9, and then use floor division of the number n = 12359, n // 10 so last digit will remove, number n = 1235, so this will continue til last digit and then we need tio sum of reminders 
# sum = reminders + sum

n = int(input('Enter a Number'))
sum = 0

while n > 0:
    r = n % 10
    n = n // 10
    sum = r + sum

print('Sum of digits are: ', sum)

# 3. Reversing a number
# Using the modular we can get the last digit of a number, suppose number n = 12359 then r = n % 10 = 9, 
# now 9 should become a 95 how it can happen so 95 = 9 * 10 + 5, now this 95 should become 953, so for that 953 = 95 * 10 + 3, now this 953 should become 9532, so for that 9532 = 953 * 10 + 2
<img width="1062" alt="image" src="https://github.com/user-attachments/assets/a9c7577b-0ced-4f52-916e-17a486d2b2bf" />

n = int(input('Enter a Number'))

rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r

print('Reverse of the number is : ', rev)

# 4. Check if the number is Palindrome
# If number n = 1221 and reverse of number rev = 1221, the reverse number is the same as the original number then the number is palindrome, ex. 25152
# For that we need to check if number == reverse then the number is palindrome, else number is not palindrome 
# but on the above script actual number n becomes zero at the end of the loop, so you always get the false only

<img width="1059" alt="image" src="https://github.com/user-attachments/assets/8308843c-550a-4f0c-a5e0-caa424d6b2a8" />

n = int(input('Enter a Number'))
m = n

rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r

if m == rev:
    print('Number is a Palindrome')
else:
    print('Number is not a Palindrome')
