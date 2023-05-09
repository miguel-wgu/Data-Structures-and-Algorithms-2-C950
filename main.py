# Author: Miguel Guzman
# ID: 010153605

import package as pkg
import hash_table
import truck
import datetime
import ui_functions

# --------------------------------------------------------------------------------------------------#
#                Overall Program Space Complexity: 0(n) and Time Complexity: 0(n^2)                 #
# --------------------------------------------------------------------------------------------------#

# --------------------------------------------------------------------------------------------------#
#                         Initialize Package Hash Table and Distance File                           #
# --------------------------------------------------------------------------------------------------#

packages_table = hash_table.HashTable(40)  # Initialize the hash table
pkg.load_package_data(packages_table)  # Load the package data into the hash table
all_packages = packages_table.get_all_keys()  # Get all the keys from the hash table

ui_functions.load_distances("CSV_FILES/WGUPS Distance Table.csv")  # Load the distances into the distances list

# --------------------------------------------------------------------------------------------------#
#                                        Initialize Trucks                                          #
# --------------------------------------------------------------------------------------------------#

# Initialize the trucks following special notes
truck1 = truck.Truck(16, 18, [16, 29, 19, 21, 24, 39, 14, 30, 15, 12, 20, 34, 31, 13, 37], "8:00 AM")
truck2 = truck.Truck(16, 18, [18, 7, 33, 40, 8, 5, 6, 10, 36, 3, 1, 2, 38], "9:05 AM")
truck3 = truck.Truck(16, 18, [9, 35, 11, 28, 22, 27, 17, 26, 25, 23, 32, 4], "10:20 AM")


# Space complexity: O(n)
# Time complexity: O(n^2)
# Efficiently loads packages into the trucks to minimize the total route miles and time.
def nearest_neighbor(truck_obj):
    # Use list comprehension to append all packages to packages_not_delivered
    packages_not_delivered = [packages_table.lookup(package_id) for package_id in truck_obj.packages]
    truck_obj.packages.clear()  # Clear the truck's packages to load them in the correct order

    # Special case: update address and zip code for package 9 if the time is 10:20 AM
    if truck_obj.starting_time == "10:20 AM":
        packages_table.lookup(9).address = "410 S State St"
        packages_table.lookup(9).zip_code = "84111"

    while packages_not_delivered:  # While packages_not_delivered is not empty
        minimum_distance = float('inf')  # Set minimum distance to an inf float
        next_to_load_package = None

        for package_obj in packages_not_delivered:
            # Get distance from current location to package address
            distance = ui_functions.get_distance(ui_functions.get_address_index(truck_obj.current_location),
                                                 ui_functions.get_address_index(package_obj.address))
            if distance <= minimum_distance:
                minimum_distance = distance
                next_to_load_package = package_obj

        truck_obj.packages.append(next_to_load_package.ID)  # Add package to truck
        packages_not_delivered.remove(next_to_load_package)  # Remove package from packages_not_delivered
        truck_obj.current_location = next_to_load_package.address  # Set current location to package address
        truck_obj.route_miles += minimum_distance  # Add distance to route miles
        truck_obj.current_time += datetime.timedelta(hours=(minimum_distance / 18))  # Add time to current time
        next_to_load_package.delivery_time = truck_obj.current_time.strftime("%I:%M %p")  # Set delivery time
        next_to_load_package.departure_time = truck_obj.starting_time  # Set departure time


# Find the nearest neighbor for each truck
nearest_neighbor(truck1)
nearest_neighbor(truck2)
nearest_neighbor(truck3)

# --------------------------------------------------------------------------------------------------#
#                                          User Interface                                           #
# --------------------------------------------------------------------------------------------------#
# Display the main menu
print('\033[92m' + '****Welcome to the WGUPS package tracking system!****\n' + '\033[0m')
print('\033[92m' + 'Please select an option from the menu below:' + '\033[0m')
print('   1. Print All Package Status and Total Mileage')
print('   2. Get a Single Package Status with a Time')
print('   3. Get All Package Status with a Time')
print('   4. Exit the Program\n')

# Prompt user for input
user_input = int(input('Option: '))
print()

# Space complexity: O(1)
# Time complexity: O(n)
# While the user does not enter 4, display the main menu and prompt the user for input and call the appropriate function
while user_input != 4:
    # try:
    if user_input == 1:  # If user enters 1, print total mileage in red and all package status
        # Print total mileage for all trucks in green
        print('\033[92m' + 'Total mileage for all trucks: {:.2f}'.format(
            truck1.route_miles + truck2.route_miles + truck3.route_miles) + '\033[0m')
        print()
        ui_functions.option1(truck1, packages_table)
        ui_functions.option1(truck2, packages_table)
        ui_functions.option1(truck3, packages_table)

    elif user_input == 2:  # If user enters 2, get a single package status with a time
        valid = False  # Initialize pass to False
        while valid is False:
            try:  # Try to convert the user's input to a datetime object
                time_str = input('Please enter a time (HH:MM AM/PM): ')  # Prompt user for time
                input_time = datetime.datetime.strptime(time_str,
                                                        "%I:%M %p").time()  # Convert time_str to datetime object
                ui_functions.option2(truck1, truck2, truck3, packages_table, input_time)
                valid = True  # Set pass to True
            except ValueError:  # If the user enters an invalid time, print an error message
                print('\033[91m' + '\nInput is not valid. Please enter a valid time as HH:MM AM/PM.\n' + '\033[0m')

    elif user_input == 3:  # If user enters 3, get all package status with a time
        valid = False  # Initialize pass to False
        while valid is False:
            try:  # Try to convert the user's input to a datetime object
                time_str = input('Please enter a time (HH:MM AM/PM): ')  # Prompt user for time
                input_time = datetime.datetime.strptime(time_str, "%I:%M %p").time()  # Convert time to datetime object
                print('\nTruck 1:')
                ui_functions.option3(truck1, packages_table, input_time)
                print('Truck 2:')
                ui_functions.option3(truck2, packages_table, input_time)
                print('Truck 3:')
                ui_functions.option3(truck3, packages_table, input_time)
                valid = True  # Set pass to True
            except ValueError:  # If the user enters an invalid time, print an error message
                print('\033[91m' + '\nInput is not valid. Please enter a valid time as HH:MM AM/PM.\n' + '\033[0m')
    if user_input > 4 or user_input < 1: print(
        '\033[91m' + 'Input is not valid. Please enter a valid option.\n' + '\033[0m')
    user_input = int(input('Option: '))  # Prompt user for input again
    print()
