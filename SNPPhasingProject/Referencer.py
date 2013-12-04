#  This method adds Variants to the parent maps corresponding to all child variants, if they do not already exist there.
#  We need this information to phase the child's variants.

from Bio import SeqIO
from Variant_ADTs import VariantType
from Variant_ADTs import Variant

def referenceVariantMaps(fatherVariantMap, motherVariantMap, childVariantMap):
	
	# for each of the child's variants

	for location in childVariantMap:
		
		variant = childVariantMap[location]
		parentAllele = lookupReference(location)


		if variant.myType == VariantType.SINGLESTRANDED:

			if fatherVariantMap.get(location, None) == None:
				fatherVariantMap[location] = Variant(variant.location, VariantType.DUMMY)

			if motherVariantMap.get(location, None) == None:
				motherVariantMap[location] = Variant(location, VariantType.DUMMY)

			continue

		if fatherVariantMap.get(location, None) == None:
                        allele = lookupReference(location)
                        fatherVariantMap[location] = Variant()
                        fatherVariantMap[location].location = location
                        fatherVariantMap[location].myType = VariantType.HOMOZYGOUS
                        fatherVariantMap[location].allele1 = allele
                        fatherVariantMap[location].allele2 = allele
			
			

		if motherVariantMap.get(location, None) == None:
                        allele = lookupReference(location)
                        motherVariantMap[location] = Variant()
                        motherVariantMap[location].location = location
                        motherVariantMap[location].myType = VariantType.HOMOZYGOUS
                        motherVariantMap[location].allele1 = allele
                        motherVariantMap[location].allele2 = allele
			
def lookupReference(variantLocation):
	
	if(variantLocation == None):
		print "Invalid variant location format" + str(variantLocation)
		return None

	GENOME_PATH="/fslgroup/fslg_hap_rockets/compute/data/hg18"

	chromosome = variantLocation[0]
	if(isinstance(chromosome, int) or chromosome.isdigit()):
		chromosome = "chr" + str(chromosome)
	base = int(variantLocation[1])
	
	genomeFile = open(GENOME_PATH + "/" + chromosome + ".fa")
	
	firstLine = genomeFile.readline()
	genomeFile.seek(base/50 + base - 1, 1) # the reference genomes are 1-indexed
	
	referenceBase = genomeFile.read(1)
	return referenceBase
