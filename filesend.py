# USAGE: python FileSender.py [file]

import sys, socket
class func:
	def __init__(self):
		HOST = 'localhost'
		CPORT = 9091
		MPORT = 9090
		FILE = "ser.py"

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
	
		try:
			ms.send(data)
			print "Send file "
		except:
			print "step1......"
		ms.close()

