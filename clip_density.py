import arcpy, collections

#User input coordinates go inside function
def clip1():
    
    arcpy.Clip_management()

def density(): #FIRST CODE USED

    my_items = collections.defaultdict(set)
    for row in cur1:
        id = row.getValue(CaseField)
        value = row.getValue(ReadFromField)
        my_items[id].add(value)


    total = sum(my_items.values())
    dicts = {}
    n = 1
    for i in my_items.values:
        dicts[n] = values[i / total]
        n += 1
    print(dicts)
    
#SECOND CODE USED
        
def density(inras, ratio, classification): #added the needed inputs
	fc = input1 #Determines file path from user input
	field = User_Field_Count #Determines pixel count field from user input
	cursor = arcpy.SearchCursor(fc)
	for row in cursor: #Calculates sum of all pixel counts
    		total = sum(row.getValue(field)) 

	final_ratio = float(classification)/float(total) #Calculates ratio for user input classification
	
	if final_ratio >= ratio: 
		return True, final_ratio #Returns true and final ratio if user input is met
	else:
		return False, final_ratio #Returns false and final ratio if user input is not met
    
