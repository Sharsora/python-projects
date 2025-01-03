<img width="1005" alt="image" src="https://github.com/user-attachments/assets/e6856fb4-eea7-42cf-ae8b-5d9129d45deb" />

```sh

punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

s1 = '[my_python@gmail.com]'

s2 = ''


for x in s1:
    if x not in punct:
        s2 = s2 + x

print(s2)
```
<img width="1012" alt="image" src="https://github.com/user-attachments/assets/135511e2-5c84-4b88-9467-803e04173654" />
