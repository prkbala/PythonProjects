import os
import pandas as pd

# path = 'F:\\Documents\\2018 - work\\Architecture\\Volume management\\data\\Leica containers kits\\results\\'
path = 'F:\\Documents\\2018 - work\\Architecture\\Volume management\\data\\Research kits\\result'
files = os.listdir(path)

dfInvList = list()
dfList = list()
for ifile in files:
    inv = pd.read_csv((path + '\\' + ifile), sep='	')
    if 'inventory' in ifile:
        cs = inv.sort_values(['2'])
        dfInvList.append(inv)
    else:
        cs = inv.sort_values(['2'])
        dfList.append(inv)

finalDf = pd.concat(dfList)
grp = finalDf.groupby('3')
for name, group in grp:
    print(name)
    print(group

sortedfinalDf = finalDf.sort_values(['10'])
sortedfinalDf.to_csv(path + '\\' + 'finalmeta.sql')
finalInvDf = pd.concat(dfInvList)
sortedfinalInvDf = finalInvDf.sort_values(['17'])
sortedfinalInvDf.to_csv(path + '\\' + 'finalinv.sql')



inputPath = 'F:\\Documents\\2018 - work\\Architecture\\Volume management\\data\\Research kits\\files\\'
 
outFile = open(inputPath + "result.txt", "w")

MeasuredVolume = list()
AspiratedVolume = list()
AllocatedAccessibleVolume = list()
DisplayVolume = list()
AccessibleVolume = list()
inventoryItems = list()

mark = False
inventory = False

files = os.listdir(inputPath)

for ifile in files:    
    pgdmp = open((inputPath + ifile), "r", encoding="UTF-8")
    lines = pgdmp.readlines()
    for line in lines:
        if "COPY inventorymetadatums (id, inventoryitemid, " in line:
            mark = True
            continue
        if  "COPY inventoryitems (id, upi, lotnumber, inventoryunit, " in line:
            inventory = True
            continue
        if mark or inventory:
            if "\." in line:
                mark = False
                inventory = False
            if "10	MeasuredVolume	" in line:
                MeasuredVolume.append(line)
            if "10	AspiratedVolume	System.Int32" in line:
                AspiratedVolume.append(line)
            if "10	AllocatedAccessibleVolume	System.Int32" in line:
                AllocatedAccessibleVolume.append(line)
            if "10	DisplayVolume	System.Int32" in line:
                DisplayVolume.append(line)
            if "10	AccessibleVolume	" in line:
                AccessibleVolume.append(line)
            if inventory and "00000017" in line:
                inventoryItems.append(line)


outFile.writelines(inventoryItems)
outFile.writelines("\n\n")
outFile.writelines(MeasuredVolume)
outFile.writelines("\n\n")
outFile.writelines(AspiratedVolume)
outFile.writelines("\n\n")
outFile.writelines(AllocatedAccessibleVolume)
outFile.writelines("\n\n")
outFile.writelines(DisplayVolume)
outFile.writelines("\n\n")
outFile.writelines(AccessibleVolume)
    