import pandas as pd
import os


# path = 'F:\\Documents\\2018 - work\\Architecture\\Volume management\\data\\Leica containers kits\\results\\'
path = 'F:\\Documents\\2018 - work\\Architecture\\Volume management\\data\\Research kits\\result\\'
# path = 'F:\\Documents\\2018 - work\\Architecture\\Volume management\\data\\cleaning kits\\results\\'

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
# sort as per id/metadatums
sortedfinalDf = finalDf.sort_values(['2', '3', '10'])
sortedfinalDf.to_csv(path + '\\' + 'metasort.sql')
# sort as per last modified date
sortedfinalDf = finalDf.sort_values([ '10'])
sortedfinalDf.to_csv(path + '\\' + 'datesort.sql')

finalInvDf = pd.concat(dfInvList)
sortedfinalInvDf = finalInvDf.sort_values(['17'])
sortedfinalInvDf.to_csv(path + '\\' + 'finalinv.sql')
