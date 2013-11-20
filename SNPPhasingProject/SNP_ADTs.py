def enum(**enums):
    return type('Enum', (), enums)

SNPType = enum(HETEROZYGOUS = 0, HOMOZYGOUS = 1)

class SNP:
    myType = SNPType.HETEROZYGOUS
    location = -1
    alleles = ["A","A"]

print("Hello world!!!")
