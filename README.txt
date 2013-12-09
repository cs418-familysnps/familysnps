This program phases heterozygous variants for a child when given the variants for the child and both of its parents. When both parents are heterozygous for an allele, the child variant cannot be phased and the variant is marked as of unknown origin.


USAGE:

run the command python Main.py [ARGS]

Arguments are:

  #1. path to the mother variant file (.vcf or 23andme format)
  #2. path to the father variant file (.vcf or 23andme format)
  #3. path to the child variant file (.vcf or 23andme format)
  #4. path to the directory of the reference genome (.fa format)
  
The 3 variant files do not have to all be the same format, but they all have to be using the same reference genome.

  
OUTPUT:
  
Output is printed to the screen, so route it to a file.  An example output would be:

chr1 358793874 A M T F

The position of the chromosome comes first, followed by the first allele and its source and the second allele and its source, either "M" for mother, "F" for father, or "U" for unknown, in the case of an unphasable variant.
