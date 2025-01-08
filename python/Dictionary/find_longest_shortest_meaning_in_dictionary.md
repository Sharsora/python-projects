```sh
dict1 = {'piece': 'portion of an object or of material, produced by cutting',
'patch': 'a piece of cloth or other material used to mend or strengthen a torn or weak point',
'area': 'a region or part of a town, a country, or the world',
'visit': 'go to see and spend time with (someone)',
'small': 'less than normal',
'with' : 'having or possessing'
}

keys = list(dict1.keys())
values = list(dict1.values())
lens = [ len(x) for x in values]

max_len= max(lens)
min_len= min(lens)

max_index = lens.index(max_len)
min_index = lens.index(min_len)

print('Max',keys[max_index],values[max_index])
print('Min', keys[min_index],values[min_index])
```
<img width="1043" alt="image" src="https://github.com/user-attachments/assets/62d023d6-7d61-48bd-ad25-234c0d858c3c" />
