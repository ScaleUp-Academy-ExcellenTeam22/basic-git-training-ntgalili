
import os
path=input("enter a path of directory: ")
list_of_files=os.listdir(path)
deep_file=[]
for f in list_of_files:
    if len(f)>4 and f[:4]=='deep':
        deep_file+=[f]
print(deep_file)