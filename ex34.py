animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

for i in range(0,6):
	if i == 0:
		print "This is the %dst animal %s." % (i + 1, animals[i])
	elif i == 1:
		print "This is the %dnd animal %s." % (i + 1, animals[i])
	elif i == 2:
		print "This is the %drd animal %s." % (i + 1, animals[i])
	else:
		print "This is the %dth animal %s." % (i + 1, animals[i])