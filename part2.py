def csv2list(filepath):
  file = open(filepath)
  first = True
  
  L = []
  for line in file:
    if first:
      first = False
      continue
      
    L.append(line.strip().split(","))
    
  return L

def last_name(people, name):
  for i in people:
    name.append(i[2])
  print (name)

def create_email():
  name = []
  people = csv2list("people.csv")
  last_name(people, name)


create_email()