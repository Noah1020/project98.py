

import os
import shutil


file1 = input("type in the 1st file you want to switch")
file2 = input("type in the 2nd file you want to switch")


with open(file1, 'r') as a:
    data_a = a.read()

with open(file2, 'r') as b:
    data_b = b.read()



with open(file1, 'w') as a:
    a.write(data_b)

with open(file2, 'w') as b:
    b.write(data_a)