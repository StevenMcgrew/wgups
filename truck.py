from datetime import time


class Truck:
    def __init__(self, id_, packages, route, miles_traveled=0, time_finished=None):
        self.id = id_
        self.packages = packages
        self.route = route
        self.miles_traveled = miles_traveled
        self.time_finished = time_finished

    def drive_route(self, start_time):

        # Update package status and log
        for pkg in self.packages:
            pkg.status = 'en route'
            pkg.log['en route'] = start_time



        pass
