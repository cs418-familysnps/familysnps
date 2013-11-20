'''An Enum for types of SNPs'''
def enum(**enums):
    return type('Enum', (), enums)

SNPType = enum(HETEROZYGOUS = 0, HOMOZYGOUS = 1)

'''SNP class, contains only the information needed to phase it'''
class SNP:
    myType = SNPType.HETEROZYGOUS
    location = -1
    alleles = ["A","A"]
