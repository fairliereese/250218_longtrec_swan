import swan_vis as swan 
import scanpy as sc
import pandas as pd
import anndata
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sg = swan.read('../data/c2c12.p')
sc.pl.umap(sg.adata, color='leiden', frameon=False, size=120, show=False)
sc.pl.umap(sg.adata, color='celltype', frameon=False, size=120, show=False)
sg.adata.var = sg.adata.var.merge(sg.t_df, left_index=True, right_index=True)
sc.pl.umap(sg.adata, color='Tpm2-202', gene_symbols='tname', frameon=False, size=120, show=False)
sc.pl.umap(sg.tss_adata, color='Nisch_2', gene_symbols='tss_name', frameon=False, size=120, show=False, cmap='magma')
print(sg.t_df.loc[sg.t_df.tname == 'Tpm2-202'])
sc.pl.violin(sg.adata, 'ENSMUST00000107913.9', groupby='leiden', jitter=0.4,
             size = 4, show = False, ylabel='Tpm2-202 Expression')
_ = sg.gen_report('Tpm2', 
              prefix='figures/Tpm2', 
              cmap='viridis', 
#               display_numbers=True, 
              groupby='leiden',
              metadata_cols=['celltype', 'leiden'],
              indicate_novel=True, 
              transcript_col='tname',
#               browser=True,
              novelty=True)