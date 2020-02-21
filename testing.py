import pythonHeader
import os

varFilePath = input("Where are we saying to? ")
varProjectName = input("Whats the project called? ")
varDesc = input("What does it do? ")

if not os.path.exists(f"{varFilePath}\{varProjectName}"):
    os.mkdir(f"{varFilePath}\{varProjectName}")

with open(f"{varFilePath}\{varProjectName}\main.py","a") as f:
    f.write(pythonHeader.pythonTitle(varProjectName, varDesc, 65))
    if os.path.exists(f"{varFilePath}\{varProjectName}\main.py"):
        print ("Success")