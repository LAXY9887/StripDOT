# fileDir = Input a BED format file
# targetCol = Gene/Transcript ID column (default = 4, the fourth column)
# stripSymbol = The letter to be remove, default = "." It will delete every thing behind it.
# outFile = Output a text file (default = ./converted.txt) that contains Gene/Transcript list.

# 沒有用任何package，歡迎自行修改

def strip(fileDir,targetCol,stripSymbol,sep,outFile):
    targrtfile = open(fileDir)
    context = targrtfile.readlines()
    targrtfile.close()

    convert = []
    converted = []

    for each in context:
        convert.append(each.split(sep)[targetCol])

    for each in convert:
        converted.append(each.split(stripSymbol)[0])

    newFile = open(outFile,"w")
    for each in converted:
        newFile.write(each+"\n")
    newFile.close()

if __name__=="__main__":
    print("Strip DOT of gene/transcript accession number from a BED file.")