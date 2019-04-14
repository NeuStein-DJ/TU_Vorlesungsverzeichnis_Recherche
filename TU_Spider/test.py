import re

s = " Mo, 15. Apr. 2019 [09:50] - Do, 18. Jul. 2019 [16:05]"
match = re.findall(r'\[[0-9]{2}:[0-9]{2}\]', s)
print(int(match[0][1:3]))