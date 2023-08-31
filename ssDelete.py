import os

path = "./"
def ssDel():
    for x in os.listdir(path):
        file = path+x
        if x.endswith('.jpg'):
            os.remove(file)
