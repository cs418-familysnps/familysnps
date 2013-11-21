import Variant_ADTs

#

def phaseSNPs(motherVariantMap, fatherVariantMap, childVariantMap, outputFileName):
    

    for location in childVariantMap.keys():
        print("do magic here")
        if childVariantMap[location].myType == VariantType.HOMOZYGOUS:
            continue