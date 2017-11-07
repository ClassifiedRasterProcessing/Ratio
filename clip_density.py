import arcpy, collections

#User input coordinates go inside function
def clip1():
    
    arcpy.Clip_management()

def density():

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
        

    
