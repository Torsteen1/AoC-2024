def import_data(filename):
    # Reads input data from a file and converts each line into a list of integers.
    with open(filename, 'r') as file:
        return [list(map(int,line.split())) for line in file] 
    
filename = 'Day 2/input.txt'
levels = import_data(filename) 


def Red_Nosed_Reindeer_nuclear_fusion_fission_plant (levels):
    increasing = all(a < b for a, b in zip(levels, levels[1:]))
    decreasing = all(a > b for a, b in zip(levels, levels[1:]))

    valid_diffrence = all(1 <= abs(a - b) <= 3 for a, b in zip(levels, levels[1:]))
    
    return (increasing or decreasing) and valid_diffrence

def is_safe_with_removal (levels):

    if Red_Nosed_Reindeer_nuclear_fusion_fission_plant(levels):
        return True
    #Checks if a level list is safe, either as-is or by removing one level.
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]  
        if Red_Nosed_Reindeer_nuclear_fusion_fission_plant(modified_levels):
            return True  
        
    return False 

safe_reports = sum(1 for levels in levels if is_safe_with_removal(levels))
print(safe_reports)