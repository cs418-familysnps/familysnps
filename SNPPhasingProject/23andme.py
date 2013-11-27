import sys

SNPfile = open(sys.argv[1])


for line in SNPfile.readlines():
	if line[0] != '#':
		line = line.rstrip()
		fields = line.split('\t')
		chromosome = fields[1]
		position = fields[2]
		alt = list(fields[3])
		print "Record(CHROM=%s, POS=%s, REF=%s, ALT=%s)" % (chromosome, position, "?", alt)

