# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,"w")

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    print(line)
    ipos = line.find(":")

    value = line[ipos + 2:]
    lst = list()
    lst.append(value)

avg = sum(lst) / len(lst)
print(avg)
print("Done")
