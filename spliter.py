

filename=open("tweets01.txt","r")
alist=filename.read()
filename.close()
#alist=alist.replace(',','\n')
alist=alist.split(',')

length=len(alist)
f=open("tweets02.txt","w")
for i in range(0,length):
    print alist[i]
    f.write(alist[i])
    f.write("\n")
f.close()

print alist[10]


    
