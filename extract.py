import os
import re
import glob

txt_files = glob.glob("text_format/*.txt")

# [print(file) for file in txt_files]

file_lines=[]
for file in txt_files:
    f= open(file,"r")
    file_lines.append(f.readlines())

exec(open("func.py").read())

for n,lines in enumerate(file_lines):
    for line in lines:
        if(re.findall("215B.E.A.R.S.",line)):
            print("File : " + txt_files[n])
            print("215B.E.A.R.S.")
            metadata_bears(lines)
            break
        elif(re.findall("Airport KPG III",line)):
            print("File : " + txt_files[n])
            print("Airport KPG III")
            metadata_airport(lines)
            break
        elif(re.findall("Asian Pacific Serviced Offices",line)):
            print("File : " + txt_files[n])
            print("Asian Pacific Serviced Offices")
            metadata_asian_pacific(lines)
            break
        elif(re.findall("Oracle America",line)):
            print("File : " + txt_files[n])
            print("Oracle America")
            metadata_oracle(lines)
            break
        elif(re.findall("VERMONT AVENUE ASSOCIATES",line)):
            print("File : " + txt_files[n])
            print("VERMONT AVENUE ASSOCIATES")
            metadata_vermont(lines)
            break
