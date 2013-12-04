from Variant_ADTs import Variant
from Variant_ADTs import VariantType


def phaseVariants(motherVariantMap, fatherVariantMap, childVariantMap, outputFileName):
    
    outputFile = open(outputFileName,'w')

    for location in childVariantMap.keys():

        variant = childVariantMap[location]
        #print("variant was: ", variant.allele1, variant.allele2)
        if variant.myType == VariantType.HOMOZYGOUS:
            variant.allele1Source = "U"
            variant.allele2Source = "U"
            continue

        if variant.myType == VariantType.SINGLESTRANDED:

            if fatherVariantMap[variant.location].myType == VariantType.SINGLESTRANDED:
                variant.allele1Source = "F"
            elif motherVariantMap[variant.location].myType == VariantType.SINGLESTRANDED:
                variant.allele1Source = "M"
            else:
                variant.allele1Source = "U"

            continue

        #  This is the real meat of the algorithm
        if variant.myType == VariantType.HETEROZYGOUS:
            #print("was heterozygous")
            if fatherVariantMap[variant.location].myType == VariantType.HOMOZYGOUS:

                if fatherVariantMap[variant.location].allele1 == variant.allele1:

                    variant.allele1Source = "F"
                    variant.allele2Source = "M"
                else:
                    variant.allele1Source = "M"
                    variant.allele2Source = "F"

            elif motherVariantMap[variant.location].myType == VariantType.HOMOZYGOUS:

                if motherVariantMap[variant.location].allele1 == variant.allele1:

                    variant.allele1Source = "M"
                    variant.allele2Source = "F"
                else:
                    variant.allele1Source = "F"
                    variant.allele2Source = "M"

            else:     # In the case of parents both giving a different variant to their child, this would be phaseable, but that is rare and time is short.
                      # Feel free to improve the code to take that case into account.
                variant.allele1Source = "U"
                variant.allele2Source = "U"

	# Write to file
	line = " ".join([variant.location[0], variant.location[1], variant.allele1, variant.allele1Source, variant.allele2, variant.allele2Source])
	outputFile.write(line + "\n")
