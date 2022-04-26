import re

file_input=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
file_output=open("cut_genes.fa","w")

name_store=[]
length_store=[]
line_store=[]

i=0
for line in file_input:
    if line.startswith(">"):
        name=">"+re.findall(r"gene:(\w+)",line)[0]
        name_store.append(name)
        i=i+1
    if not line.startswith(">"):
        newline=line.strip("\n")
        if len(line_store) < i:
            line_store.append(newline)
        else:
            line_store[i-1]=line_store[i-1]+newline

for i in range(len(line_store)):
    length_store.append(len(line_store[i]))

for i in range(len(name_store)):
    if len(re.findall("GAATTC",line_store[i])) !=0:
        file_output.write(name_store[i])
        file_output.write("     ")
        file_output.write(str(length_store[i]))
        file_output.write("\n")
        file_output.write(line_store[i])
        file_output.write("\n")

file_output.close()
