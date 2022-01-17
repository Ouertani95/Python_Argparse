# TP2_Argparse

## About : select_fasta.py :

This script takes a fasta file as input and checks if the sequences inside are valid.

## Features :

**Main Feature** :
- Determine if sequences are valid or not valid

**Optional Features** :
- Determine number of nucletides of each sequence in the fasta file
- Determine positions of non nucleotides in each sequence
- output results in a text file

## Installation :

To install this script use the following commands :

```bash
mkdir ~/Desktop/OUERTANI/
cd ~/Desktop/OUERTANI/
git clone https://github.com/Ouertani95/TP2_Argparse
pip install -r requirements.txt
```
==> You're now good to go!

## Usage :

For information on using the script you can type the following commands :

```bash
cd ~/Desktop/OUERTANI/
python3 select_fasta.py -h
```

## Autocompletion :

if you don't get autocompletion using **TAB** after an argument do the following steps : 

```bash
pip uninstall argcomplete
sudo apt-get install python3-argcomplete 
sudo activate-global-python-argcomplete3
```
==> Now you can run the script on the terminal with autocompletion enabled.

## Authors :

**Mohamed Ouertani**