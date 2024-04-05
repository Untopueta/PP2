import os

path = input()

print(os.access(path, os.F_OK)) # existence
print(os.access(path, os.R_OK)) # readability
print(os.access(path, os.W_OK)) # writability
print(os.access(path, os.X_OK)) # executability

os.chmod()