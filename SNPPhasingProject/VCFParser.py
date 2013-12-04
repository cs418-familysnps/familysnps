import sys
import os
import vcf

# Look in the __init__ for some instructions on how to use this stuff.

# Below I'm parsing through the first 5000 lines of our data.

vcf_reader = vcf.Reader(open('top_5000_lines.vcf', 'r'))

for record in vcf_reader:
    temp = str(record.ALT[0])
    if(len(record.REF) == 1 and record.ALT[0] != None and len(temp) == 1):
    #if(True):
    #	len(temp)
    #    print record.REF,record.ALT[0],'  ',record.POS
    #print record.QUAL
        #print record
        print record.CHROM
        #print record.POS
        #print record.ID
        #print record.REF
        #print record.ALT
        #print record.QUAL
        #print record.FILTER
        #print record.INFO   
        #print record.genotype
        print record.samples
        print record.num_hom_ref, record.num_het, record.num_hom_alt
        print "-------------------------------"

#class VCFData():
