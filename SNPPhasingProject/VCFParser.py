import sys
import os
import vcf

# Look in the __init__ for some instructions on how to use this stuff.

# Below I'm parsing through the first 5000 lines of our data.

vcf_reader = vcf.Reader(open('top_5000_lines.vcf', 'r'))

for record in vcf_reader:
    print(record)
    #Record.CHROM``
    #Record.POS``
    #Record.ID``
    #Record.REF``
    #Record.ALT``
    #Record.QUAL``
    #Record.FILTER``
    #Record.INFO``    