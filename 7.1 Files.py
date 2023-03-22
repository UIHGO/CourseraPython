# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
x = inp.rstrip()
print(x.upper())
#print(inp.upper()[:len(inp)-1])
#for line in fh:
#    liner=line.rstrip()
#    print(liner.upper())
