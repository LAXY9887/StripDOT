# fileDir = input BED 檔案
# targetCol = ID欄位預設=3(BED檔)
# stripSymbol = 要切掉的字元預設"."，切掉.以後的字
# outFile = output路徑+檔名，預設:當前資料夾 ./converted.txt

# 沒有用任何package，歡迎自行修改

def strip(fileDir,targetCol,stripSymbol,outFile):
    targrtfile = open(fileDir)
    context = targrtfile.readlines()
    targrtfile.close()

    convert = []
    converted = []

    for each in context:
        convert.append(each.split("\t")[targetCol])

    for each in convert:
        converted.append(each.split(stripSymbol)[0])

    newFile = open(outFile,"w")
    for each in converted:
        newFile.write(each+"\n")
    newFile.close()

if __name__=="__main__":
    print("Strip DOT of gene accession number.")