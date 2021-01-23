import pandas as pd 
import inflect


p = inflect.engine()

df = pd.read_csv('C:\\Users\\bss\\Documents\\Hackathon\\Melbourne\\Tbl_Tissue_Blocks.csv')

df['Tissue_Block_Name'] += df.groupby('Tissue_Block_Name').cumcount().add(1).map(p.ordinal).radd('_')
df.to_csv('C:\\Users\\bss\\Documents\\Hackathon\\Melbourne\\Tbl_Tissue_Blocks_no_duplicates.csv')


