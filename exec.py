import os
os.system('tonegen3.py')

for x in range(10):
    print(x)
    
os.kill('tonegen3.py')