import vpk
import os
import time
from progress.bar import IncrementalBar

pathcustom = input("Write path to vpk: ")

try:
    pak = vpk.open(pathcustom)
    #print(pathcustom)

    basedir = os.path.splitext(os.path.basename(pathcustom))[0]
    curdir = os.path.dirname(pathcustom) + "/vpks_extracted/" + basedir
    if not os.path.exists(curdir):
        os.makedirs(curdir)
        print("Making a directory for vpk: ", basedir) # Creating a directory with vpk name
    file_count = 0
    print(basedir)
    print(curdir)

    # Calculating count
    for filepath_c in pak:
        file_count += 1
        
    progressstr = basedir+':'
        
    bar = IncrementalBar(progressstr, max = file_count)

    for filepath in pak:
        print("\n",filepath,"\n")
        pakfile = pak[filepath]
        nicedir = curdir + "/" + os.path.dirname(filepath)
        # print(curdir + "/" + filepath)
        if not os.path.exists(nicedir):
            os.makedirs(nicedir)
            print("Making a sub-directory") # Creating a folder from vpk
            # print("/" + filepath)
        pakfile.save(curdir + "/" + filepath) # Writing the file from vpk
        bar.next()
        
    bar.finish()

    print("\033[H\033[J", end="")
    print("Successfuly extracted vpk '%s', into: '%s'" % (basedir, curdir))
except FileNotFoundError:
    print("Error! VPK is not valid!")
