import datetime
import textwrap

def pythonTitle(title, shortDesc, varSpacing):
  varReturn = ""
  varDashes = "# "
  whiteSpace = ""

  for _ in range(1, varSpacing):
    varDashes += "-"

  varReturn = f"{varDashes}\n"
  
  varHalf = ((varSpacing - len(title)) / 2) - 1
  
  for _ in range (1, int(varHalf)):
    whiteSpace += " "    

  if len(title) % 2 != 0:
    varReturn += f"# |{whiteSpace}{title} {whiteSpace}|"
    varReturn += f"\n{varDashes}" 
    
  else:
    varReturn += f"# |{whiteSpace}{title}{whiteSpace}|"
    varReturn += f"\n{varDashes}" 

  varReturn += "\n# Dean Ralph"
  varReturn += f"\n# {str(datetime.date.today())}"
  varReturn += "\n#"
  varReturn += f"\n# Project Title:\n# {title}\n#"
  varReturn += f"\n# Short Description:"
  
  for lines in textwrap.wrap(shortDesc, width=varSpacing):
    varReturn += f"\n# {lines}"

  varReturn += "\n\n# Imports:\n\n\n# Main App:"

  return varReturn
