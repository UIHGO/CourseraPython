name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()
for line in fh:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hours = time.split(':')
        counts[hours[0]] = counts.get(hours[0], 0) + 1
    else:
        continue
for k,v in sorted(counts.items()):
    print(k,v)