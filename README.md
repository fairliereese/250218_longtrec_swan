# Swan tutorial and workshop

What you will need:
* A GitHub account and git cli set up on your computer

## Install [miniconda](https://docs.anaconda.com/miniconda/install/)
* Make sure you choose the version for your operating system!
* If you have conda set up already, skip this step

## Clone this repo and create the Swan conda environment

```bash
git clone git@github.com:fairliereese/250218_longtrec_swan.git
cd 250218_longtrec_swan
conda env create -f conda_env_config.yml
conda activate swan
pip install swan_vis
```

## Download data

Only the final `.p` files:
```bash
wget https://zenodo.org/records/14904845/files/5xfad.p?download=1 -O data/5xfad.p
wget https://zenodo.org/records/14904845/files/c2c12.p?download=1 -O data/c2c12.p
```

<!-- Everything:
```bash
wget https://zenodo.org/api/records/14904845/files-archive
``` -->

## Resources
* [Swan documentation](https://github.com/mortazavilab/swan_vis)
* [Swan GitHub](https://github.com/mortazavilab/swan_vis)
* [Swan manuscript](https://academic.oup.com/bioinformatics/article/37/9/1322/5912931)
* [Today's presentation](https://docs.google.com/presentation/d/10DQPfCY2aSK7bC0fFrnYNSCz2vqXWNxNDTNro3iy8FQ/edit?usp=sharing)
* [Data on Zenodo](https://zenodo.org/records/14904845)
