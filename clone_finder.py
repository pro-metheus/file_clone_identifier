import os
import hashlib

def clone_finder(path):
    gen = os.walk(path)
    index = {}
    while True:
        try:
            root, folders, files = next(gen)
            for file in files:
              size = str(os.path.getsize(os.path.join(root,file)))
              if size not in index:
                  index[size] = [os.path.join(root,file)]
              else:
                  index[size].append(os.path.join(root,file))
        except:
            print('finished')
            break
    return index


def hash_verify(index):
    new_index = {}
    for item in index:
        for file in index[item]:
            f = open(file,'rb')
            try:
                content = f.read()
            except:
                pass
            f.close()
            _hash = hashlib.sha256(content).hexdigest()
            if _hash not in new_index:
                new_index[_hash] = [file]
            else:
                new_index[_hash].append(file)
    return new_index
            

if __name__ == '__main__':
    path = '' #enter root here
    index = hash_verify(clone_finder(path))
    for item in index:
        if len(index[item]) > 1:
            print(item)
            dirs = index[item]
            for d in dirs:
                print('\t\t',d)
                
                  
