# USAGE: python FileReciever.py

import socket, time, string, sys, urlparse
from threading import *

#------------------------------------------------------------------------

class StreamHandler ( Thread ):
    def __init__( this ):
        Thread.__init__( this )

    def run(this):
	print "running "
        this.process()

    def bindmsock( this ):
        this.msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	p1=9999
        this.msock.bind(('', p1))
        this.msock.listen(1)
        print '[Media] Listening on port '+str(p1)

    def acceptmsock( this ):
        this.mconn, this.maddr = this.msock.accept()
        print '[Media] Got connection from', this.maddr
    
    def bindcsock( this ):
        this.csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	p2=9998
        this.csock.bind(('', p2))
        this.csock.listen(1)
        print '[Control] Listening on port '+str(p2)

    def acceptcsock( this ):
        this.cconn, this.maddr = this.csock.accept()
        print '[Control] Got connection from', this.maddr
        
        while 1:
            data = this.cconn.recv(1024)
            if not data: break
            if data[0:4] == "SEND": this.filename = data[5:]
            print '[Control] Getting ready to receive "%s"' % this.filename
            break

    def transfer( this ):
        print '[Media] Starting media transfer for "%s"' % this.filename
	s=this.filename.split("/")
	i=len(s)
	print s[i-1]
	this.filename=s[i-1]
        f = open(this.filename,"w+")
        while 1:
            data = this.mconn.recv(1024)
            if not data: break
            f.write(bz2.decompress(data))
            print bz2.decompress(data)
        f.close()

        print '[Media] Got "%s"' % this.filename
        print '[Media] Closing media transfer for "%s"' % this.filename
    
    def close( this ):
        this.cconn.close()
        this.csock.close()
        this.mconn.close()
        this.msock.close()

    def process( this ):
        while 1:
            this.bindcsock()
            this.acceptcsock()
            this.bindmsock()
            this.acceptmsock()
            this.transfer()
            this.close()

#------------------------------------------------------------------------

s = StreamHandler()
s.start()

