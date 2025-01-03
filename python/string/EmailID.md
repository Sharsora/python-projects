```sh
emailid = input('Enter email id')

atrate = emailid.find('@')

print(atrate)

print('user id:', emailid[:atrate])
print('domain name:', emailid[atrate+1:])
```

<img width="970" alt="image" src="https://github.com/user-attachments/assets/f25baac3-7359-48c1-9361-315616edfc2e" />
