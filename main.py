import md5
import program
import subprocess

c=raw_input("enter client file address")
s=raw_input("enter sever file adress")

client=open(c,'rw+')
server=open(s,'rw+')
if len(c.read())<(2**30) and len(s.read())<(2**30):
    if program.checksum(client,server):
        if md5.checkmd5(client,server):
	    pass
        else:
	    client.write(server.read(1024))
    else:
        subprocess.call(["mv",c,s])
else:
    print("large file size")


