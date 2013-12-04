import sys
from Variant_ADTs import Variant
from Variant_ADTs import VariantType

def parse23andmeFile(file):
	
	SNPfile = file

	dictionary = {}

	for line in SNPfile.readlines():
		if line[0] != '#':
			line = line.rstrip()
			fields = line.split('\t')
			chromosome = fields[1]
			position = fields[2]
			alt = list(fields[3])
			#print "Record(CHROM=%s, POS=%s, REF=%s, ALT=%s)" % (chromosome, position, "?", alt)
			variant = Variant()

			if len(alt) == 1:
				variant.myType = VariantType.SINGLESTRANDED
			else:
				if len(alt) == 2:
					if alt[0] == alt[1]:
						variant.myType = VariantType.HOMOZYGOUS
					else:
						variant.myType = VariantType.HETEROZYGOUS	
	
	
			variant.location = ("chr%s" % (chromosome),position)
			
			variant.allele1 = alt[0]
			
			if len(alt) == 2:
				variant.allele2 = alt[1]
			else:
				variant.allele2 = alt[0]
	
			#dictionary[position] = variant
			dictionary[variant.location] = variant
	
	return dictionary			
