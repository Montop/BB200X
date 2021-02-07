import os

rows = int(input("How many columns? "))
cols = int(input("How many rows? "))

# Put all filenames from working directory into a list.
oldNames = list(os.listdir())

# Put the filenames into sub-lists (with the correct montage order) into a new list.
thing = []
for i in range(0, cols + 1):
    thing.append(oldNames[-i:0:-cols])

# For some reason the previous loop skips the 000_000 file. The next row adds it to the list.
thing[cols].append(oldNames[0])

# Reverses the order of the sub-lists to get everything into the correct montage order.
thing.reverse()

niceThing = []

# Puts the sub-lists into a normal list.
for i in thing:
    for x in i:
        niceThing.append(x)

newNames = list(x for x in range(0, len(oldNames)))

# Rename the files using the numbers in the newNames list.
for i in range(0, len(niceThing)):
    os.rename(str(niceThing[i]), str(newNames[i]) + '.ome.tif')