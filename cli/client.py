#!/usr/bin/env python

import bz2 
import os
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


class func:
	def __init__(self,string,h1,p2,p1):
		print p1 
		print p2
		FILE = string
		print string
		cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		cs.connect((h1, p1))
		cs.send("SEND " + FILE)
		cs.close()

		ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			ms.connect((h1, p2))
		except :
			print " "
		f = open(FILE, "rb")
		data = f.read()
		f.close()
		encrypted_data = bz2.compress(data)
	
		try:
			ms.send(encrypted_data)
			print encrypted_data
			print "Send file "
		except:
			print "Error Trying again !!"
		ms.close()
	
	def stop(self):
		print "stop"
		



class con_gui:
        string =" "
	def __init__(self):
	    self.gladefile = "gui-cli.glade"
	    self.builder = gtk.Builder()
	    self.builder.add_from_file(self.gladefile)
	    self.builder.connect_signals(self)
	    self.window = self.builder.get_object("window1")
	    self.window.show()
	    self.display = self.builder.get_object("display")
	    self.default_str='Request button will get these files  :: .doc .txt .pdf .docx .html .mp3 From this Directory :: /home/hammad/dir'
	    self.display.set_text(self.default_str)
	    self.fname="default"
	    
	def on_window1_destroy(self, object, data=None):
	    print "quit with cancel"
	    gtk.main_quit()

	def on_choose_file_set(self,obj,data=None):
	    print(obj.get_filename()+"----->selected")
	    string_filename =obj.get_filename()
	    self.fname=obj.get_filename()
	    s=self.fname.split("/")
	    i=len(s)

	def on_clicked_send(self, button, data="Nothing to send"):
	    string="connected"
	    self.entry1 = self.builder.get_object("entry1")
   	    self.entry2 = self.builder.get_object("entry2")
            self.entry4 = self.builder.get_object("entry4")
	    string="Address : "+str(self.entry1.get_text())+" : "+str(self.entry2.get_text()+"\n\n")
 	    self.display = self.builder.get_object("display")
	    self.display.set_text(string)
            if self.fname=="default" :
		self.display.set_text("Select a File First !")
	    else :
	    	fu=func(self.fname,self.entry1.get_text(),int(self.entry2.get_text()),int(self.entry4.get_text()))
 	        fu=func(self.fname,self.entry1.get_text(),int(self.entry2.get_text()),int(self.entry4.get_text()))

	def on_clicked_req(self, button, data="Nothing to send"):
		self.display = self.builder.get_object("display")
		self.entry1 = self.builder.get_object("entry1")
   	   	self.entry2 = self.builder.get_object("entry2")
            	self.entry4 = self.builder.get_object("entry4")
		self.entry3 = self.builder.get_object("entry3")
		v1=self.entry1.get_text()
		v2=int(self.entry2.get_text())
		v3=int(self.entry4.get_text())
		#fu=func(v1,v2,v3)
		data = self.entry3.get_text()
		l=['.doc','.txt','.pdf','.docx','.html','.mp3'] 
		if data in l :
			for r,d,f in os.walk("/home/hammad/dir"):
    				for files in f:
    				    if files.endswith(data):
     					        d= os.path.join(r,files)
				                print d 
					        m=func(d,v1,v2,v3)
						m=func(d,v1,v2,v3)
					        self.display.set_text("Sent  " + d ) 
		else :
			self.display.set_text("File format not supported for sending ")
			

	def on_clicked_stop(self, button, data="Nothing to send"):
	    string="connected"
	    self.entry1 = self.builder.get_object("entry1")
   	    self.entry2 = self.builder.get_object("entry2")
	    string=string+" ::  Address : "+str(self.entry1.get_text())+" : "+str(self.entry2.get_text()+"\n\n")
	    self.display = self.builder.get_object("display")
	    self.display.set_text(string)
	 

	
	

n=con_gui()
gtk.main()

