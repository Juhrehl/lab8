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

people = csv2list('people.csv')

def create_email(people):
  emails = []

  for country in people:
    print (country[4])

def count_country(people):
  countries = []

  for country in people:
    if country[4] not in countries:
      countries.append(country[4])

  print(countries)

count_country(people)