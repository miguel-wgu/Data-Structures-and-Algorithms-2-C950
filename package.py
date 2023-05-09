import csv
from hash_table import HashTable


class Package:
    def __init__(self, ID, address, city, state, zip_code, deadline, weight, special_notes, status="At the hub",
                 departure_time=None,
                 delivery_time=None):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = departure_time
        self.delivery_time = delivery_time
        self.special_notes = special_notes

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.city, self.state, self.zip_code,
            self.deadline, self.weight + ' kilos', self.status,
            self.departure_time, self.delivery_time, self.special_notes)


# Space and Time Complexity: O(n)
# Reads the package csv file and returns a list of packages
def read_package_csv(file_path):
    packages = HashTable(40)  # Initialize a hash table with 40
    with open(file_path) as packages_file:
        csv_reader = csv.reader(packages_file)
        next(csv_reader)
        for row in csv_reader:
            if row[0].isdigit():
                # Extract the package data from the csv file
                package = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], status="At the hub",
                                  special_notes=row[7])
                # Insert the package into the hash table
                packages.insert(package.ID, package)
    return packages


# This function is used to load the package data into the hash table
def load_package_data(packages_table):
    packages = read_package_csv("CSV_FILES/WGUPS Package File.csv")
    for package_id in packages.get_all_keys():
        package = packages.lookup(package_id)
        packages_table.insert(package_id, package)
