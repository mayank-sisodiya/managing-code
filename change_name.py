import os,sys
directory=["/media/mayank/academic/cp/AC/","/media/mayank/academic/cp/WA-TLE/"]
for dire in directory:
    os.chdir(dire)
    for f in os.listdir("."):
        if f[-3:]!="cpp":
            os.remove(f)
