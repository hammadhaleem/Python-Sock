import os 
for r,d,f in os.walk("/home/hammad/dir"):
    for files in f:
        if files.endswith(".doc"):
            d= os.path.join(r,files)
	    print d 
	     
