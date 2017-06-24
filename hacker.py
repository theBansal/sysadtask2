
def mydiff(old,new):
    o=open(old)
    n=open(new)
    ol=o.readlines()
    nl=n.readlines()
    temp=[]
    for a in range(len(ol)):
        for b in range(len(nl)):
	    if ol[a]==nl[b]:
		temp.append(ol[a])
    for a in range(len(ol)):
	for b in range(len(temp)):
	    if ol[a]==temp[b]:
                break
	    elif b==(len(temp)-1):
		print "Delete at position ",a+1
		print "-",ol[a]

    for a in range(len(nl)):
        for b in range(len(temp)):
            if nl[a]==temp[b]:
                break
            elif b==(len(temp)-1):
                print "Add at position ",a+1
                print "+",nl[a]


