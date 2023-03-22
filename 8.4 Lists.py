fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    xline=line.rstrip()
    xline=xline.split()
    for i in range(len(xline)):
        if xline[i] not in lst:
            lst.append(xline[i])
        else:
            continue
lst.sort()
print(lst)
