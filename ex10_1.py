import sleep
while True:
	for i in ["/", "-", "|", "\\", "|"]:
		sleep(.9)
		print "%s\r" % i,