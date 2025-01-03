<img width="1049" alt="image" src="https://github.com/user-attachments/assets/f78d3261-edcc-4058-8256-e15233dd2212" />

```sh
s1 = input('Enter a String')
s2 = input('Enter second String')

if len(s1) != len(s2):
    print('Not Anagram')
else:

    for x in s1:
        if x not in s2:
            print('Not Anagarm')
            break;
    else:
        print('Anagram')
```

<img width="940" alt="image" src="https://github.com/user-attachments/assets/42d95fec-ae51-4ff4-851f-3ed80c14f375" />
