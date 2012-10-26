# USAGE: python FileSender.py [file]

import sys, socket
class func:
	def __init__(self):
		HOST = '192.168.1.3'
		CPORT = 5555
		MPORT = 5556
		FILE = "ser.py"

		cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			cs.connect(HOST, CPORT)
		except:
			print "unable to connect "
			sys.exit(1)
		cs.send("SEND " + FILE)
		cs.close()

		ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			ms.connect(HOST, MPORT)
		except :
			print "unable to connect  "
		f = open(FILE, "rb")
		data = f.read()
		f.close()
	
		try:
			ms.send(data)
			print "Send file "
		except:
			print "step1......"
		ms.close()


m=func()

