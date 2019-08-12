import csv
def smart_meter_state1(count):
    array = []
    with open('block_1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile) 
        for i,rows in enumerate(reader):
            #if i == count:
                #row = rows
            print(rows["tstp"].split(".")[0]+ " " +rows["LCLid"]+rows["energy(kWh/hh)"])

            array.append(rows["tstp"])
    return array

if __name__ == '__main__':
    print("1")
    smart_meter_state1(0)
