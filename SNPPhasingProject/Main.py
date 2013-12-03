import sys

motherFileName = ''
fatherFileName = ''
childFileName = ''
pathToReference = ''

if len(sys.argv) < 5:
    print('Arguments must be: motherFileName, fatherFileName, childFileName, pathToReference')
    exit()

motherFileName = sys.argv[1]
fatherFileName = sys.argv[2]
childFileName = sys.argv[3]
pathToReference = sys.argv[4]
