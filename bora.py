import os
import pandas as pd
#fazer diamond
os.system("./diamond makedb --in VFDB.fasta -d reference")
os.system("mv VFDB.fasta faa")
lista_dos_arquivos = os.listdir()
for arquivo in lista_dos_arquivos:
    if arquivo.endswith(".faa"):
        arquivo_mod = arquivo.replace(".faa","")+".csv"
        os.system("./diamond blastp -d reference -q "+arquivo+" -o "+arquivo_mod)
        tratamento_de_dados = pd.read_csv(arquivo_mod, sep=" ")
        tratamento_de_dados.columns = ["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore"]
        tratamento_de_dados.to_csv(arquivo_mod.replace(".csv","")+"_non_treated")
        arquivo_tratado1 = tratamento_de_dados[(tratamento_de_dados["pident"] > 70)]
        arquivo_tratado2 = arquivo_tratado1.filter(["qseqid"])
        arquivo_tratado2.to_csv(arquivo_mod.replace(".csv",".list"), header=False, index=False)
        arquivo3 = arquivo.replace(".faa","new.faa")
        os.system("list2ffnfaa.pl"+arquivo_mod.replace(".csv",".list ")+arquivo+ " > "+arquivo3)
        