def printer(a, tab = 0):
	if type(a) == type(list()):
		for i in a:
			printer(i, tab)
	elif type(a) == type(dict()):
		for i in a:
			if(type(a[i]) == type(dict())):
				for j in xrange(tab):
					print '\t',
				print i,': '
				printer(a[i], tab+1)
			elif type(a[i]) == type(list()):
				for j in xrange(tab):
					print '\t',
				print i,': '
				printer(a[i], tab+1)
			else:
				for j in xrange(tab):
					print '\t',
				print i, ': ', a[i]
	else:
		for i in xrange(tab+1):
			print '\t',
		print a
