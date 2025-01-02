<img width="1065" alt="image" src="https://github.com/user-attachments/assets/d67d0a9d-8275-4035-9c8c-3f6a0b911ba8" />
-
-
-
-
```sh
for n in range (1, 100+1):
   count = 0

   for i in range(1, n+1):
       if n % i == 0:
           count += 1
   if count == 2:
       print('Its a Prime')
   else:
       print('Its Not a Prime')
```
