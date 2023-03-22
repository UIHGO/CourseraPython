# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
number=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    count=count+1
    number=float(line[line.find("0"):])+number
print("Average spam confidence:",number/count)
