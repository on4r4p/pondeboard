file = open("test","r+a")
lines = file.read().splitlines()
lenfile = len(lines)
lastitem = lines[lenfile -1]
print lastitem
newitem = int(lastitem) + 666
finalitem = str(newitem) + "\n"
print finalitem
file.write(finalitem)
file.close()

