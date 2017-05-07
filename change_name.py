import os,sys
#to delete object files
directory=["/media/mayank/academic/cp/AC/","/media/mayank/academic/cp/ACTIVE/"]
for dire in directory:
    os.chdir(dire)
    for f in os.listdir("."):
        if f[-3:]!="cpp":
            os.remove(f)


#to move the cpp files of accepted problems to different directory
active_dir="/media/mayank/academic/cp/ACTIVE/"
count=0
s="//AC"
os.chdir(active_dir)
for f in os.listdir("."):
	infile=open(f,'r')
	first_line=infile.readline()
	first_line=first_line.rstrip()
	if first_line == s :
		os.rename(active_dir+f,"/media/mayank/academic/cp/AC/"+f)
		count+=1

print("Moved "+str(count)+" files")
