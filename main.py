import re

text = input()
count = 0
result = re.split(r'[",.!?:; ()]', text)
result = list(filter(None, result))
for res in result:
    if (res.replace("-","") == "" ):
        continue
    else:
        count += 1

print(count)