import Variant_ADTs

#

def phaseSNPs(motherVariantMap, fatherVariantMap, childVariantMap, outputFileName):
    

    for location in childVariantMap.keys():

        if childVariantMap[location].myType == VariantType.HOMOZYGOUS:
            continue

        if variant.myType == VariantType.SINGLESTRANDED:

            if fatherVariantMap[variant.location].myType == SINGLESTRANDED:
                variant.allele1Source = "F"
            else if motherVariantMap[variant.location].myType == SINGLESTRANDED:
                variant.allele1Source = "M"
            else:
                variant.allele1Source = "U"

            continue

        #  This is the real meat of the algorithm
        if variant.myType == VariantType.HETEROZYGOUS:

            if fatherVariantMap[variant.location].myType == HOMOZYGOUS:

                if fatherVariantMap[variant.location].allele1 == variant.allele1:

                    variant.allele1Source = "F"
                    variant.allele2Source = "M"
                else:
                    variant.allele1Source = "M"
                    variant.allele2Source = "F"

        else if motherVariantMap[variant.location].myType == HOMOZYGOUS:

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