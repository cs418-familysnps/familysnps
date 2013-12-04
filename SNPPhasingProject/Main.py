import sys
from Referencer import referenceVariantMaps
from VariantPhaser import phaseVariants
from parse23andme import parse23andmeFile
from Variant_ADTs import Variant
from Variant_ADTs import VariantType
import sys
import os
import vcf

motherFileName = ''
fatherFileName = ''
childFileName = ''
pathToReference = ''

def getVCFDictionary(fileName):
    vcf_reader = vcf.Reader(open(fileName, 'r'))
    snps = dict();
    for record in vcf_reader:        
        if(len(record.REF) == 1 and record.ALT[0] != None and len(str(record.ALT[0])) == 1):
            variant = Variant()
            variant.allele1 = record.REF
            variant.allele2 = record.ALT[0]
            if(record.num_het == 1):
                variant.myType = VariantType.HETEROZYGOUS
            elif(record.num_hom_alt == 1):
                variant.myType = VariantType.HOMOZYGOUS   
            snps.update({record.POS : variant})
            print len(snps)
    return snps

# Given a valid filename of a vcf or 23andme file, returns a mapping of location to Variant
def mapInputFile(fileName):
    try:
        inputFile = open(fileName)
    except:
        print(fileName, ' could not be opened. Aborting...')
        exit(1)

    splitFile = fileName.split('.')
    fileType = splitFile[len(splitFile) - 1]
    
    if fileType != 'vcf' and fileType != 'txt':
        print('File format is unsupported.  Only VCF or 23andMe formats are supported at this time.')
        exit(1)

    if fileType == 'vcf':
        snps = getVCFDictionary(fileName);
        print("")#TODO: do VCF parsing here, and return the map

    if fileType == 'txt':
        return parse23andmeFile(inputFile)


if len(sys.argv) < 5:
    print('Arguments must be: motherFileName, fatherFileName, childFileName, pathToReference')
    exit(1)

motherFileName = sys.argv[1]
fatherFileName = sys.argv[2]
childFileName = sys.argv[3]
pathToReference = sys.argv[4]

print "Reading input files"
motherVariantMap = mapInputFile(motherFileName)
fatherVariantMap = mapInputFile(fatherFileName)
childVariantMap = mapInputFile(childFileName)

print "Referencing Variant Maps"
referenceVariantMaps(motherVariantMap, fatherVariantMap, childVariantMap)
print "Phasing variants"
phaseVariants(motherVariantMap, fatherVariantMap, childVariantMap, 'phasedvariants.txt')
