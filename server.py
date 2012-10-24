#!/usr/bin/env python

import sys
import socket
import string
import bz2 
import socket, time, string, sys, urlparse
from threading import *

try:
  import math
except:
  print('math lib missing')
  sys.exit(1)
try:
  import pygtk
  pygtk.require('2.0')
except:
  pass
try:
  import gtk
  import gtk.glade
except:
  print('GTK not available')
  sys.exit(1)



#------------------------------------------------------------------------

class StreamHandler ( Thread ):
    def __init__( this ):
        Thread.__init__( this )

    def run(this):
	print "running "
        this.process()

    def bindmsock( this ):
        this.msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	p1=this.p1
        this.msock.bind(('', p1))
        this.msock.listen(1)
        print '[Media] Listening on port '+str(p1)

    def acceptmsock( this ):
        this.mconn, this.maddr = this.msock.accept()
        print '[Media] Got connection from', this.maddr
    
    def bindcsock( this ):
        this.csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	p2=this.p2
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
	   # dec=bz2.decompress(data)
            f.write(data)
	    print data
        f.close()

        print '[Media] Got "%s"' % this.filename
        print '[Media] Closing media transfer for "%s"' % this.filename
    
    def close( this ):
        this.cconn.close()
        this.csock.close()
        this.mconn.close()
        this.msock.close()


    def process( this ):
	print "openfile"
	fi = open("temp.txt","r")
	fdata=fi.read()
	fi.close
	da=fdata.split("\n")
	#print da
	this.p1=int(da[0])
	this.p2=int(da[1])
        print this.p1
	print this.p2
	while 1:
	    this.bindcsock()
            this.acceptcsock()
            this.bindmsock()
            this.acceptmsock()
            this.transfer()
            this.close()

   

#------------------------------------------------------------------------

class con_gui():
        string =" "
	def __init__(self,s):
	    self.gladefile = "gui-soc.glade"
	    self.builder = gtk.Builder()
	    self.builder.add_from_file(self.gladefile)
	    self.builder.connect_signals(self)
	    self.window = self.builder.get_object("dialog1")
	    self.window.show()
	    print "getting object "
	    self.s=s	  
	    print "got object --> "+ str(self.s)  
	    
	def on_window1_destroy(self, object, data=None):
	    print "quit with cancel"
	    gtk.main_quit()

	def on_clicked_start(self, button, data="Nothing to send"):
	    self.entry1 = self.builder.get_object("entry1")
   	    self.entry2 = self.builder.get_object("entry2")
	    string ="Server running " 
	    self.display = self.builder.get_object("display")
	    self.display.set_text(string)
	    fi = open("temp.txt","w")
	    fi.write(self.entry1.get_text())
	    fi.write("\n")
	    fi.write(self.entry2.get_text())
	    fi.close()
	    self.s.start()
	    

	def on_clicked_stop(self, button, data="Nothing to send"):
	    string="stopping server "	
	    print string 
	    self.display = self.builder.get_object("display")
	    self.display.set_text(string)
	    
	 

s=StreamHandler()
n=con_gui(s)
gtk.main()

