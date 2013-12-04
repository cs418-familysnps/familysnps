import sys
from Referencer import referenceVariantMaps
from VariantPhaser import phaseVariants
from 23andme import parse23andmeFile

# Given a valid filename of a vcf or 23andme file, returns a mapping of location to Variant
def mapInputFile(fileName):
    try:
        inputFile = open(fileName)
    except:
        print(fileName, ' could not be opened. Aborting...')
        exit(1)

    splitFile = fileName.split('.')
    fileType = splitFile[len(splitFile - 1)]
    
    if fileType != 'vcf' and fileType != 'txt':
        print('File format is unsupported.  Only VCF or 23andMe formats are supported at this time.')
        exit(1)

    if fileType == 'vcf':
        print("")#TODO: do VCF parsing here, and return the map

    if fileType == 'txt':
        return parse23andmeFile(inputFile)

motherFileName = ''
fatherFileName = ''
childFileName = ''
pathToReference = ''

if len(sys.argv) < 5:
    print('Arguments must be: motherFileName, fatherFileName, childFileName, pathToReference')
    exit(1)

motherFileName = sys.argv[1]
fatherFileName = sys.argv[2]
childFileName = sys.argv[3]
pathToReference = sys.argv[4]

motherVariantMap = mapInputFile(motherFileName)
fatherVariantMap = mapInputFile(fatherFileName)
childVariantMap = mapInputFile(childFileName)

print "Referencing Variant Maps"
referenceVariantMaps(motherVariantMap, fatherVariantMap, childVariantMap)
print "Phasing variants"
phaseVariants(motherVariantMap, fatherVariantMap, childVariantMap, 'phasedvariants.txt')
