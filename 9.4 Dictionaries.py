name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()
for line in fh:
    if line.startswith("From "):
        words = line.split()
        #print(words[1])
        counts[words[1]] = counts.get(words[1], 0) + 1
    else:
        continue

bigcount = None
bigemail = None
for email, count in counts.items():
    if bigcount is None or bigcount<count:
        bigcount = count
        bigemail = email
print(bigemail, bigcount)
