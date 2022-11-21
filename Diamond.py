
import os,sys, pandas as pd, numpy as np
#Diamond alignment with the VFDB database

#creating a diamond-formatted database file
os.system("./diamond makedb --in VFDB.fasta -d reference")
pasta_arquivos_fasta = "./faa/"
lista_dos_arquivos = os.listdir(pasta_arquivos_fasta)

for arquivo in lista_dos_arquivos:
    os.system("./diamond blastp -d reference -q "+arquivo+" -o "+arquivo+".tsv")
