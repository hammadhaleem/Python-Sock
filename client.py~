#!/usr/bin/env python

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


class func:
	def __init__(self,string,host,mport,cport):
		HOST  = host
		CPORT = cport
		MPORT = mport
		print CPORT 
		print MPORT
		FILE = string
		print string
		cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		cs.connect((HOST, CPORT))
		cs.send("SEND " + FILE)
		cs.close()

		ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			ms.connect((HOST, MPORT))
		except :
			print " "
		f = open(FILE, "rb")
		data = f.read()
		f.close()
		encrypted_data = bz2.compress(data)
	
		try:
			ms.send(encrypted_data)
			print "Send file "
		except:
			print "step1......"
		ms.close()
	def stop(self):
		print "stop"
		



class con_gui:
        string =" "
	def __init__(self):
	    self.gladefile = "gui-ser.glade"
	    self.builder = gtk.Builder()
	    self.builder.add_from_file(self.gladefile)
	    self.builder.connect_signals(self)
	    self.window = self.builder.get_object("window1")
	    self.window.show()
	    
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
	    fu=func(self.fname,self.entry1.get_text(),int(self.entry2.get_text()),int(self.entry4.get_text()))
	    fu=func(self.fname,self.entry1.get_text(),int(self.entry2.get_text()),int(self.entry4.get_text()))


	def on_clicked_stop(self, button, data="Nothing to send"):
	    string="connected"
	    self.entry1 = self.builder.get_object("entry1")
   	    self.entry2 = self.builder.get_object("entry2")
	    string=string+" ::  Address : "+str(self.entry1.get_text())+" : "+str(self.entry2.get_text()+"\n\n")
	    self.display = self.builder.get_object("display")
	    self.display.set_text(string)
	 

	
	

n=con_gui()
gtk.main()

