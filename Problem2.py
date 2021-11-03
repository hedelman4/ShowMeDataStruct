import os

global pathArray
pathArray = []

def find_files(suffix, path):
    if os.path.isdir(path):
        for _ in os.listdir(path):
            if os.path.isdir(os.path.join(path,_)):
                find_files(suffix,os.path.join(path,_))
            elif _.endswith(suffix):
                pathArray.append(os.path.join(path,_))
        return pathArray

print(find_files(".c","./testdir"))
pathArray.clear()
print(find_files("  ","./testdir"))
pathArray.clear()
print(find_files("./solution/problem2/problem2.py",".py"))
