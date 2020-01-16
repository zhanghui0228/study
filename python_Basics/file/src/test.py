
print("this is test backup file")

import os.path, os

path = os.listdir()
for i in path:
    resu = os.path.isfile(i)
    print(resu)
print(path)

