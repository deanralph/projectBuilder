import json

class project:

  def __init__(self, fileName):
    with open(filename, "r") as file:
      self.conf = file.json.load()
