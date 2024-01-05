from os import listdir
from os.path import isfile, abspath, join

def listWPP():
    mypath = "./wpp" # <--- Változtasd meg a háttereid helyére!!!
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    wallpapers = []
    for f in files:
        wpp = join(mypath, f)
        wallpapers.append(wpp)
    return(wallpapers)
