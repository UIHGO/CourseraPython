import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1115771.txt"
file=open(name)
search= re.findall('[0-9]+', file.read())
summa=0
for number in search:
    summa = summa + (int(number))
print(summa)

