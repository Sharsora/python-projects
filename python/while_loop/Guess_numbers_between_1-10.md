- suppose I have selected a random number 6
- now you guess number 2, I will say the number is lesser
- now you guess number 9, I will say the number is larger
- now you guess number 5, I will say the number is lesser
- now you guess a number between 5 - 9, which is 6, I will say that correct
- In this way, I will give multiple chances to guess a number. Every time you guess the  number, I will tell you whether the number is smaller than my number or greater than my number
- <img width="1062" alt="image" src="https://github.com/user-attachments/assets/f6ad916c-a9b4-4ee2-b048-94f704b333aa" />

- import a module random
- now calling the function n = random.randint(1,10) this will give some random number from 1 - 10, Just like I guess number 6
- now you have to repeatedly take inputs from user and find out whether he is guessing a correct number or not
- initially guess = 0
- now user inputs guess a number, now the guess number is less than a number that I Have randomly selected by calling the function, print number is lesser
- elif if the guess number is greater than n, then should the print number is larger
- else: the guess number is not larger or lesser than its correct number

- this process I should repeat how long I should repeat it, as long as the guess number is not equal to the random number (guess ! = n)

```sh
import random

n = random.randint(1, 10)
guess = 0

while guess != n:
    guess = int(input('Guess a number'))
    
    if guess < n:
        print(' it is smaller')
    elif guess > n:
        print(' it is larger')
    else:
        print('Correct Guess')
```
