import os

os.chdir("/Users/BasicallySteve/Desktop")

with open("s.txt", "r+") as f:
    s = f.readline()

with open("t.txt") as f2:
    t = f2.readline()

index_list = []

index = 0

while index < len(s):
    index = s.find( t, index)
    if index == -1:
        break
    index_list.append(index)
    index += 1

for x in index_list:
    x += 1
    print(x, end=" ")
