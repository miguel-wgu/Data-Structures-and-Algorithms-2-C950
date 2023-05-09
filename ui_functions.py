import datetime
import csv


# Space Complexity: O(1)
# Time Complexity: O(n)
# This function prints total truck mileage and packages delivered by truck 1, truck 2, and truck 3
def option1(truck, packages_table):
    # Print truck packages information
    print('\033[91m' + '***Delivered by Truck 1 with a total mileage of {:.2f}'.format(truck.route_miles) + '\033[0m')

    # Loop through all packages in truck, set status to delivered, and print package information
    for package_id in truck.packages:
        package = packages_table.lookup(package_id)
        package.status = 'Delivered'
        print(package)
    print()


# Space and Time Complexity: O(1)
# This function prints the status of a package at a given time and package ID
def option2(truck1, truck2, truck3, packages_table, input_time):
    truck = None
    found = False
    package_id = input('Please enter a package ID: ')  # Prompt user for package ID
    print()

    # A truck is assigned to the truck variable if the package_id is in the truck's packages list and found is set to
    # True
    if int(package_id) in truck1.packages:
        truck = truck1
        found = True
    elif int(package_id) in truck2.packages:
        truck = truck2
        found = True
    elif int(package_id) in truck3.packages:
        truck = truck3
        found = True

    # If a package was found, call the print_package_status function
    if found is True:
        print_package_status(truck, packages_table, input_time, package_id)
    print()


# Space Complexity: O(1)
# Time Complexity: O(n)
# This function prints the status of all packages at a given time
def option3(truck, packages_table, input_time):
    # Loop through all packages in the truck's packages list and call the print_package_status function
    for package_id in truck.packages:
        print_package_status(truck, packages_table, input_time, package_id)
    print()


# Space and Time Complexity: O(1)
# This function contains the logic that determines package status based on the input time
def print_package_status(truck, packages_table, input_time, package_id):
    time_format = "%I:%M %p"
    truck_start_time = datetime.datetime.strptime(truck.starting_time, time_format).time()
    package = packages_table.lookup(int(package_id))
    package_delivery_time = datetime.datetime.strptime(package.delivery_time, time_format).time()
    # If the input time is less than the truck's starting time, the package status is set to At the Hub
    if input_time < truck_start_time:
        print(
            f"Package ID: {package.ID} | Address: {package.address} | City: {package.city} | State: {package.state} |"
            f"Zip: {package.zip_code} | Weight: {package.weight} | Delivery Deadline: {package.deadline} | "
            f"Delivery Status: At Hub | Departure Time: N/A | Delivery Time: N/A | Special Notes: {package.special_notes}")
    # Else if the input time is less than the package's delivery time, the package status is set to En Route
    elif input_time < package_delivery_time:
        print(
            f"Package ID: {package.ID} | Address: {package.address} | City: {package.city} | State: {package.state} |"
            f"Zip: {package.zip_code} | Weight: {package.weight} | Delivery Deadline: {package.deadline} | "
            f"Delivery Status: En Route | Departure Time: {truck.starting_time} | Delivery Time: N/A | "
            f"Special Notes: {package.special_notes}")
    # Else the package status is set to Delivered
    else:
        print(
            f"Package ID: {package.ID} | Address: {package.address} | City: {package.city} | State: {package.state} |"
            f"Zip: {package.zip_code} | Weight: {package.weight} | Delivery Deadline: {package.deadline} | "
            f"Delivery Status: Delivered | Departure Time: {truck.starting_time} | Delivery Time: {package.delivery_time}"
            f" | Special Notes: {package.special_notes}")


distance_table = []  # Stores the distances from the csv file
address_table = []  # Stores the addresses from the csv file


# Space and Time Complexity: O(n)
# Reads the WGUPS Distance Table_2.csv file and adds the data to the distances and addresses lists.
def load_distances(file_name):
    with open(file_name, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # Add in distance and/or addresses to either addresses = [] or distances = [].
            address = row[0].replace('\n', '').split('(')[0].strip()  # Remove the new line character and the zip code
            address_table.append(address.strip())  # Add the address to the addresses list
            distance_table.append(row[1:])  # Add the distances to the distances list


# Method to get address number from string literal of address
def get_address_index(address):
    index1 = address_table.index(address)  # return index from address_list
    return index1


# Method to get distance between two addresses
def get_distance(address1, address2):
    distance = distance_table[address1][address2]  # 2 dimensional array to get distance
    if distance == '':
        distance = distance_table[address2][address1]
    return float(distance)  # return distance as float
