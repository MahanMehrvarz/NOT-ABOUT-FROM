alist=["a","b","c","1","3"]
blist=["2","3","4"]

h=list(set(alist).intersection(blist))
if not h:
    print "nothing"

