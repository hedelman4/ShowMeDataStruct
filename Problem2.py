import os

def find_files(suffix, path, pathArray = []):
    for _ in os.listdir(path):
        if os.path.isdir(os.path.join(path,_)):
            find_files(suffix,os.path.join(path,_))
        elif _.endswith(".c"):
            pathArray.append(os.path.join(path,_))
    return pathArray

print(find_files(".c","./testdir"))
