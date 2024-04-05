import os

directory = './dir/subdir/'

print(os.listdir(directory))

for i in range(1, 31):
    file = open("{directory}{i}.txt", "x")
    file.close()