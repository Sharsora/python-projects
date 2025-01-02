
# ###1. Counting the number of digit in a number
# if you divide the number using floor division the last number will remove from the given number. Suppose number n = 12359 and if you do n // 10 = 1235, 9 will be remove because in flooe division you will not get .9
# and we will count till number became 0 

n = int(input('Enter a Number'))
counter = 0

while n > 0:
    n = n // 10
    counter += 1

print('Number of digits are: ', counter)
