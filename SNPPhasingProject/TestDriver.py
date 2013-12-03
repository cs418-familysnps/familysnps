import VariantPhaser
from Variant_ADTs import Variant
from Variant_ADTs import VariantType
from Referencer import referenceVariantMaps
from Referencer import lookupReference

testVariant1 = Variant()
testVariant2 = Variant()
testVariant3 = Variant()

testVariant1.myType = VariantType.HOMOZYGOUS
testVariant1.location = ("chr1", 1)
testVariant1.allele1 = "A"
testVariant1.allele2 = "A"

testVariant2.myType = VariantType.HETEROZYGOUS
testVariant2.location = ("chr1", 1)
testVariant2.allele1 = "T"
testVariant2.allele2 = "A"

testVariant3.myType = VariantType.HETEROZYGOUS
testVariant3.location = ("chr1", 1)
testVariant3.allele1 = "T"
testVariant3.allele2 = "A"

testMotherMap = {testVariant1.location:testVariant1}
testFatherMap = {testVariant2.location:testVariant2}
testChildMap = {testVariant3.location:testVariant3}

testMotherMap2 = {testVariant2.location:testVariant2}
testFatherMap2 = {testVariant3.location:testVariant3}
testChildMap2 = {testVariant1.location:testVariant1}

testMotherMap3 = {testVariant2.location:testVariant2}
testFatherMap3 = {}
testChildMap3 = {testVariant1.location:testVariant1}


# begin VariantPhaser test

VariantPhaser.phaseVariants(testMotherMap, testFatherMap, testChildMap, "testOutput")

assert(testVariant3.allele1Source == "F")
assert(testVariant3.allele2Source == "M")

VariantPhaser.phaseVariants(testMotherMap2, testFatherMap2, testChildMap2, "testOutput")

assert(testVariant1.allele1Source == "U")
assert(testVariant1.allele2Source == "U")


# begin Referencer test

assert(lookupReference(("chr1",1)) == 't')

referenceVariantMaps(testMotherMap3, testFatherMap3, testChildMap3)

assert(testFatherMap3.get(('chr1', 1), None) != None)











