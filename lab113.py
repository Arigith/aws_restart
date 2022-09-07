import csv
import copy

myvehicle = {
    'vin':'<empty>',
    'make':'<empty>',
    'model':'<empty>',
    'year':0,
    'range':0,
    'topspeed':0,
    'zerosixty':0.0,
    'mileage':0
}
for key, value in myvehicle.items():
    print(f'{key} : {value}')
    myinventorylist = []

with open('car_fleet.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    linecount = 0
    for row in csvreader:
        if linecount == 0:
            print(f'Column names are: {", ".join(row)}')
            linecount += 1
        else:
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topspeed: {row[5]}, zerosixty: {row[6]}, milage: {row[7]}')
            currentvehicle = copy.deepcopy(myvehicle)
            currentvehicle['vin'] = row[0]
            currentvehicle['make'] = row[1]
            currentvehicle['model'] = row[2]
            currentvehicle['year'] = row[3]
            currentvehicle['range'] = row[4]
            currentvehicle['topspeed'] = row[5]
            currentvehicle['zerosixty'] = row[6]
            currentvehicle['mileage'] = row[7]
            myinventorylist.append(currentvehicle)
            linecount += 1
print(f'Processed {linecount} lines.')
for mycarproperties in myinventorylist:
    for key, value in mycarproperties.items():
        print(f'{key} : {value}')
        print('-----')