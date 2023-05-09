from datetime import datetime


class Truck:
    def __init__(self, capacity, speed, packages, starting_time):
        self.capacity = capacity  # The number of packages the truck can hold
        self.speed = speed  # The speed of the truck in miles per hour
        self.packages = packages  # The packages the truck is carrying
        self.starting_time = starting_time  # The time the truck departs the HUB
        self.current_time = datetime.strptime(self.starting_time, "%I:%M %p")  # The current time of the truck
        self.current_location = "HUB"  # The current location of the truck
        self.route_miles = 0  # The total miles traveled by the truck

    # Adds a package to the truck
    def add_packages(self, package_ids):
        for package_id in package_ids:  # Iterate through the package ids
            if package_id not in self.packages:  # If the package id is not in the truck, add it
                self.packages.append(package_id)

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (
            self.capacity, self.speed, self.packages, self.starting_time, self.current_time.strftime("%I:%M %p"))
