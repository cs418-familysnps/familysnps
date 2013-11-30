'''An Enum for types of SNPs'''
def enum(**enums):
    return type('Enum', (), enums)

VariantType = enum(HETEROZYGOUS = 0, HOMOZYGOUS = 1, SINGLESTRANDED = 2, DUMMY = 3)

'''Variant class, contains only the information needed to phase it'''
class Variant:
    myType = VariantType.HETEROZYGOUS
    location = ("chr-1", -1)
    
    # could be bases or vcf indel notation
    allele1 = ""
    allele2 = ""

    # "M" for mother, "F" for father
    allele1Source = ""
    allele2Source = ""
	
	def getAlleles():
		return [allele1, allele2];