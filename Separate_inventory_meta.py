import os



# inputPath = 'F:\\Documents\\2018 - work\\Architecture\\Volume management\\data\\Leica containers kits\\files\\'
# inputPath = 'F:\\Documents\\2018 - work\\Architecture\\Volume management\\data\\Research kits\\files\\'
inputPath = 'F:\\Documents\\2018 - work\\Architecture\\Volume management\\data\\cleaning kits\\files\\'

inventory = list()
meta = list()

metamark = False
inventorymark = False

files = os.listdir(inputPath)

for ifile in files:    
    pgdmp = open((inputPath + ifile), "r", encoding="UTF-8")
    lines = pgdmp.readlines()
    inventory = []
    meta = []
    for line in lines:
        if "COPY inventorymetadatums (id, inventoryitemid, " in line:
            metamark = True
            meta.append('1	2	3	4	5	6	7	8	9	10\n')
            continue
        if  "COPY inventoryitems (id, upi, lotnumber, inventoryunit, " in line:
            inventorymark = True
            inventory.append('1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21\n')
            continue            
                              
        if inventorymark:
                if "\." in line:
                    fileparts = ifile.split('.')
                    fileparts[0] += 'inventory'
                    outFileName = inputPath + fileparts[0] + '.' + fileparts[1]
                    outFile = open(outFileName, 'w')
                    outFile.writelines(inventory)
                    outFile.close()
                    inventorymark = False
                else:
                    inventory.append(line)

        if metamark:
                if "\." in line:
                    fileparts = ifile.split('.')
                    fileparts[0] += 'meta'
                    outFileName = inputPath + fileparts[0] + '.' + fileparts[1]
                    outFile = open(outFileName, 'w')
                    outFile.writelines(meta)
                    outFile.close()
                    metamark = False
                else:
                    meta.append(line)

   