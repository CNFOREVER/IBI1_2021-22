import re

file_in=input("Please input the file name:")
file_input=open(file_in,"r")
file_output=open("count_cut_genes.fa","w")

name_store=[]
cut_store=[]
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
    cut_store.append(len(re.findall("GAATTC",line_store[i]))+1)

for i in range(len(name_store)):
    if len(re.findall("GAATTC",line_store[i])) !=0:
        file_output.write(name_store[i])
        file_output.write("     ")
        file_output.write(str(cut_store[i]))
        file_output.write("\n")
        file_output.write(line_store[i])
        file_output.write("\n")

file_output.close()
