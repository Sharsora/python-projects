```sh
for i in range(0,5):
    print('* '* 5)
```

<img width="1048" alt="image" src="https://github.com/user-attachments/assets/bea03731-3f0a-48e0-b548-256df0358962" />

```sh
for i in range(0,5):
    for j in range(0,5):
        if i >= j:
            print('*',end=' ')
    print('')
```
```sh
sharsora@SHARSORA-M-G1WP python-practise % python3 pattern.py 
* 
* * 
* * * 
* * * * 
* * * * * 
sharsora@SHARSORA-M-G1WP python-practise %
```

### pattern
```sh
for i in range(0,5):
    for j in range(0,5):
        if i >= j:
            print('*',end=' ')
    print('')
```
```sh
sharsora@SHARSORA-M-G1WP python-practise % python3 pattern.py
* 
* * 
* * * 
* * * * 
* * * * * 
sharsora@SHARSORA-M-G1WP python-practise % 
```

### pattern
```sh
for i in range(1,6):
    print('* ' * i)
```
```sh
sharsora@SHARSORA-M-G1WP python-practise % python3 pattern.py
* 
* * 
* * * 
* * * * 
* * * * * 
sharsora@SHARSORA-M-G1WP python-practise %
```



```sh
for i in range(5,0,-1):
    print('* ' * i)
```

```sh
sharsora@SHARSORA-M-G1WP python-practise % python3 pattern.py
* * * * * 
* * * * 
* * * 
* * 
* 
sharsora@SHARSORA-M-G1WP python-practise % 
```

