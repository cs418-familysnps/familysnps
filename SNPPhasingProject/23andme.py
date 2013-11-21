import sys

SNPfile = open(sys.argv[1])


for line in SNPfile.readlines():
	if line[0] != '#':
		for word in line.split('\t'):
			print word


