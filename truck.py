import datetime


class Truck:
    def __init__(self, id_, packages=None, route=None, avg_speed=18, miles_driven=0, start_time=None,
                 time_of_completion=None):
        self.id_ = id_
        self.packages = packages
        self.route = route
        self.avg_speed = avg_speed
        self.miles_driven = miles_driven
        self.start_time = start_time
        self.time_of_completion = time_of_completion

    def load_packages(self, packages, package_ids):
        truck_packages = []
        for pkg_id in package_ids:
            pkg = packages.get(pkg_id)
            pkg.truck_name = f"Truck {self.id_}"
            truck_packages.append(packages.get(pkg_id))
        self.packages = truck_packages

    def drive_route(self, start_time, distances):
        self.start_time = start_time
        self.time_of_completion = start_time
        self.update_all_to_en_route(start_time)
        # Iterate route, accumulate time and miles, drop off packages
        for i in range(len(self.route) - 1):
            starting_address_id = self.route[i]
            current_address_id = self.route[i + 1]
            miles = self.get_distance(starting_address_id, current_address_id, distances)
            self.miles_driven += miles
            minutes = round((miles / self.avg_speed) * 60)
            self.time_of_completion += datetime.timedelta(minutes=minutes)
            self.drop_off_packages(current_address_id, self.time_of_completion)

    def update_all_to_en_route(self, start_time):
        for pkg in self.packages:
            pkg.status = 'en route'
            pkg.log['en route'] = start_time

    def get_distance(self, start_id, end_id, distances):
        primary_index = start_id
        secondary_index = end_id
        if primary_index < secondary_index:
            temp_index = primary_index
            primary_index = secondary_index
            secondary_index = temp_index
        return distances[primary_index][secondary_index]

    def drop_off_packages(self, address_id, time):
        for pkg in self.packages:
            if pkg.address_id == address_id:
                pkg.status = "Delivered at " + time.strftime('%H:%M:%S')
                pkg.log["delivered"] = time
