def import_data(filename):
    with open(filename, 'r') as file:
        #return zip(*[map(int, line.split()) for line in file])
        return [(line.strip()) for line in file]
filename = 'Day 2/input.txt'
list = import_data(filename) 
print(list)

