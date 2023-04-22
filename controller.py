import csv


def get_cupcakes(file):
    cupcake_list = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            cupcake_list.append(row)
    return cupcake_list

def find_cupcakes(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dict(file, cupcake):
    with open(file, 'a', newline='\n') as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling", "file_name"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def get_order(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        order = list(reader)
        return order
