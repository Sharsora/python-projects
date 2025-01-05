<img width="1064" alt="image" src="https://github.com/user-attachments/assets/40a4a5ec-dd17-4f7b-84a2-24579d7c34f1" />

```sh
work_hours = [int(x) for x in input('Enter hours per day in entire week, separated by space').split()]
wage = int(input('Enter hourly wage'))

total = sum(work_hours)

salary = total * wage

print('Salary is',salary)
```
