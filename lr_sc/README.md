## Data origin
Data comes from my 2021 paper on LR-RNA-seq in single cells / nuclei

* [Raw data](https://www.encodeproject.org/publications/31c1f27d-0fd5-46e5-88b2-52a3a4ea9e49/)
* [Manuscript](https://link.springer.com/article/10.1186/s13059-021-02505-w)

## Data download
```bash
# this is the only necessary one
wget https://zenodo.org/records/14904499/files/c2c12.p?download=1 -O ../data/c2c12.p

# but if you want to create the SwanGraph from 0, you can download the rest
wget https://zenodo.org/records/14904499/files/c2c12_metadata.tsv?download=1 -O ../data/c2c12_metadata.tsv
wget https://zenodo.org/records/14904499/files/c2c12_swan_abundance_filtered.tsv?download=1 -O ../data/c2c12_swan_abundance_filtered.tsv
wget https://zenodo.org/records/14904499/files/c2c12_talon.gtf?download=1 -O ../data/c2c12_talon.gtf
wget https://zenodo.org/records/14904499/files/gencode.vM21.annotation.gtf?download=1 -O ../data/gencode.vM21.annotation.gtf
wget https://zenodo.org/api/records/14904845/draft/files/gene_clusters_celltypes.tsv?download=1 -O ../data/gene_clusters_celltypes.tsv
```

## Create the SwanGraph
Again, this is optional as I've provided the full SwanGraph (`c2c12.p`) already.

Run the code in `make_swan_graph.ipynb`.
