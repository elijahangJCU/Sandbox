
with open('countries.csv', 'r') as f:
    for i in f:
     line = f.readline()
     record = [country.split(',') for country in line]
     print(record)