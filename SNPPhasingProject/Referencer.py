#  This method adds Variants to the parent maps corresponding to all child variants, if they do not already exist there.
#  We need this information to phase the child's variants.

from Bio import SeqIO

def referenceVariantMaps(fatherVariantMap, motherVariantMap, childVariantMap):
	
	# for each of the child's variants

	for variant in childVariantMap:
		
		parentAllele = lookupReference(variant.location)


		if variant.myType == VariantType.SINGLESTRANDED:

			if fatherVariantMap[variant.location] == None:
				fatherVariantMap[variant.location] = Variant(variant.location, VariantType.DUMMY)

			if motherVariantMap[variant.location] == None:
				motherVariantMap[variant.location] = Variant(variant.location, VariantType.DUMMY)

			continue

		if fatherVariantMap[variant.location] == None:
			fatherVariantMap[variant.location] = Variant(variant.location, VariantType.HOMOZYGOUS) # TODO: we need the reference alleles
			
			

		if motherVariantMap[variant.location] == None:
			motherVariantMap[variant.location] = Variant(variant.location, VariantType.HOMOZYGOUS) # TODO: we need the reference alleles
			
def lookupReference(variantLocation):

	GENOME_PATH="/fslgroup/fslg_hap_rockets/compute/data/hg18"

	chromosome = variantLocation[0]
		
	# there should only be one record.....
	record = SeqIO.read(GENOME_PATH + "/" + str(chromosome) + ".fa", "fasta")
	referenceBase = record.seq[variantLocation[1]]
	print referenceBase
