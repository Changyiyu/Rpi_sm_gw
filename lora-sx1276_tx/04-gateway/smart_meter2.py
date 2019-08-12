import csv
def smart_meter_state2(count):
    array = []
    with open('block_2.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile) 
        for i,rows in enumerate(reader):
            #if i == count:
                #row = rows
            array.append(rows)
    return array
                


