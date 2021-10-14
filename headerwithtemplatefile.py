# Dean Ralph
# 2021-10-14
#
# Project Title: Pyhton Boilerplate Maker
# Current Version: 0.1
#
# Short Description: A quick and easy header maker for new python files
#
# Imports:

import datetime
import textwrap


# Main:

peramsDic = {"AUTH":"", 
"DATE":datetime.date.today(), 
"PRO":"",
"VER":"0.1",
"DESC":""}

peramsDic.update({"AUTH":input("Auther Name: ")})
peramsDic.update({"PRO":input("Project Name: ")})
peramsDic.update({"DESC":input("Short Description: ")})

plate = ""

with open("boilderplate.txt", "r") as f:
    for line in f:
        if len(line) > 2 and line.find("$") != -1:
            _split = line.split("$")
            _construct = _split[0] + str(peramsDic[_split[1]]) + _split[2]
            plate += _construct
        else:
            plate += line

with open(f"{peramsDic['PRO']}.py", "a") as w:
    w.write(plate)
