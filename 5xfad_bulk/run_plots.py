import swan_vis as swan 
import scanpy as sc
import pandas as pd
import anndata
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sg = swan.read('../data/5xfad.p')
test = sg.get_die_genes(kind='iso', obs_col='condition',
                        obs_conditions=['WT', '5xFAD'])
test.loc[test.gname=='Csf2ra']
sg.gen_report('Csf2ra', 
              'figures/Csf2ra', 
              metadata_cols=['condition'],
              novelty=True, 
              cmap='magma', 
              layer='pi',
              display_numbers=True,
              groupby='condition',
              indicate_novel=True,
              transcript_col='tname')
sg.gen_report('Csf2ra', 
              'figures/Csf2ra', 
              metadata_cols=['condition'],
              novelty=True, 
              cmap='viridis', 
              layer='tpm',
              groupby='condition',
              browser=True,
              transcript_col='tname')
test = sg.get_die_genes(kind='tss', obs_col='condition',
                        obs_conditions=['WT', '5xFAD'])
test.loc[test.gname=='Lsp1']
sg.gen_report('Lsp1', 'figures/Lsp1', 
              indicate_novel=True,  
              cmap='magma', 
              layer='pi',
              transcript_col='tname',
              groupby='condition',
              display_numbers=True, 
              novelty=True,
              metadata_cols=['condition'])

test = sg.get_die_genes(kind='tes', obs_col='condition',
                        obs_conditions=['WT', '5xFAD'], p=0.05, dpi=10)

test.loc[test.gname=='Myef2']
sg.gen_report('Myef2', 
              'figures/Myef2', 
              metadata_cols=['condition'],
              novelty=True, 
              cmap='magma', 
              layer='pi',
              groupby='condition',
              browser=True,
              display_numbers=True,
              transcript_col='tname')


df = swan.calc_tpm(sg.adata)
df = df.loc[df.any(axis=1)]
var_names = sg.t_df.loc[sg.t_df.gname=='Csf2ra'].index.tolist()
var_names = list(set(var_names)&(set(df.columns.tolist())))
var_names = sg.t_df.loc[var_names, 'tname'].tolist()
print(var_names)
sg.adata.var = sg.adata.var.merge(sg.t_df['tname'], left_index=True, right_index=True)
sc.pl.matrixplot(sg.adata, gene_symbols='tname', var_names=var_names, groupby='condition', swap_axes=True, figsize=(4,6))

myef2_tes = sg.tes_adata.var.loc[sg.tes_adata.var.gname == 'Myef2'].index.tolist()
myef2_adata = sg.tes_adata[:, myef2_tes]
sc.pp.filter_genes(myef2_adata, min_counts=1, inplace=True)
myef2_tes_name = myef2_adata.var.tes_name.tolist()

sc.pl.matrixplot(sg.tes_adata, gene_symbols='tes_name', var_names=myef2_tes_name, groupby='condition', swap_axes=True, figsize=(4,4))
