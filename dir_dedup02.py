import os,sys
import subprocess

argv=sys.argv[1:]
cmd1="hadoop fs -cat "
cmd2=" | md5sum"
dir_list={}
dir_count=0
dup_count=0
filecount=0
x={}
y={}
flag=0
fiilelist=[]
output= open("op.txt","w")

def check_output(cmd):
    """ https://docs.python.org/2/library/subprocess.html#subprocess.Popen
        Implementation subprocess.check_output() for Python 2.6
     """
    process_list = []
    cmd_list = cmd.strip().split("|")
    for i, sub_cmd in enumerate(cmd_list):
        cmd_list = sub_cmd.strip().split(" ")
        STDIN = None
        if i > 0:
            STDIN = process_list[i - 1].stdout
        process_list.append(subprocess.Popen(cmd_list, stdin=STDIN, stdout=subprocess.PIPE))
    if len(process_list) == 0:
        return ''
    output = process_list[i].communicate()[0]
    return output


def dir_add(dirr):
        fiilelist = [ line  for line in check_output("hadoop fs -ls "+dirr).split('\n') if len(line.rsplit(None,1))][1:]

        for a in fiilelist:
                if a[0]=='d':
                        dir_list["/"+a.rsplit(" /",1)[-1]]=0
			dir_add("/"+a.rsplit(" /",1)[-1])
        return None



def dupli(direc):

        filelist = [ line.rsplit(None,1)[-1] for line in check_output("hadoop fs -ls "+direc).split('\n') if len(line.rsplit(None,1))][1:]
	global filecount
        for name in filelist:
		if(name.rsplit(".",1)[-1]==name):
			continue
		else:
                	x[name]=check_output(cmd1+name+cmd2)
			filecount = filecount + 1

        for a in x:
                y[x[a]]=0

        for a in x:
                y[x[a]]=y[x[a]]+1



for a in argv:
	root=a

dir_list[root]= 0

dir_add(root)

while(flag==0):
	flag=1
	for a in dir_list:
		if (dir_list[a]==0):
			dupli(a)
			dir_list[a]=1
			flag=0

for b in y:
	o=[]
	if(y[b]!=1):
		dup_count = dup_count + y[b]-1
	for q in x:
		if(b==x[q]):
			o.append(q)
	output.write(str(o)+","+str(y[b])+"\n")
output.write("Total No. of Directories: %d\n" % len(dir_list))
output.write("Total No. of Files: %d\n" % filecount)
output.write("Total No. of Duplicates: %d\n" % dup_count)

