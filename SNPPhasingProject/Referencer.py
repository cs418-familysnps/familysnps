#  This method adds Variants to the parent maps corresponding to all child variants, if they do not already exist there.
#  We need this information to phase the child's variants.

referenceVariantMaps(fatherVariantMap, motherVariantMap, childVariantMap)

	for variant in childVariantMap:

		if variant.myType = VariantType.SINGLESTRANDED:

			if fatherVariantMap[variant.location] == None
				fatherVariantMap[variant.location] = new Variant(variant.location, VariantType.DUMMY)

			if motherVariantMap[variant.location] == None
				motherVariantMap[variant.location] = new Variant(variant.location, VariantType.DUMMY)

			continue

		if fatherVariantMap[variant.location] == None
			fatherVariantMap[variant.location] = new Variant(variant.location, VariantType.HOMOZYGOUS) # TODO: we need the reference alleles

		if motherVariantMap[variant.location] == None
			motherVariantMap[variant.location] = new Variant(variant.location, VariantType.HOMOZYGOUS) # TODO: we need the reference alleles