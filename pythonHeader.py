import datetime

def pythonTitle(title):
  varSpacing = 75
  varReturn = ""
  varDashes = "# "
  whiteSpace = ""
  varTitle = title

  for _ in range(1, varSpacing):
    varDashes += "-"

  varReturn = varDashes + "\n"

  if len(title) % 2 != 0:
    varHalf = ((varSpacing - len(title)) / 2) - 1

    for _ in range (1, int(varHalf)):
      whiteSpace += " "    
            
    varReturn += f"# |{whiteSpace}{title} {whiteSpace}|"
    varReturn += f"\n{varDashes}" 

  varReturn += "\n# Dean Ralph"
  varReturn += "\n# " + str(datetime.date.today())
  varReturn += "\n#"
  varReturn += f"\n# Project Title: {title}"
  varReturn += f"\n# Short Description:"

  return varReturn