from collections import Counter

def import_data(filename):
    with open(filename, 'r') as file:
        return zip(*[map(int, line.split()) for line in file])
    
filename = 'Day 1/input.txt'
list1, list2 = import_data(filename) 

def calculate_distance(list1, list2): 
  return sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2)))

def similiraity_score(list1, list2):
    frequency_dict = Counter(list2)
    return sum(num * frequency_dict.get(num, 0) for num in list1)

print("Similarity score:", similiraity_score(list1, list2))
print("Total Distance:" , calculate_distance(list1, list2))  




