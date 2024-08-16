import datetime
import sys

from route_optimizer import optimize_route
from strings import *


class CLI:
    def __init__(self, packages, distances, trucks):
        self.packages = packages
        self.distances = distances
        self.trucks = trucks

    def run(self):
        print(TITLE)
        self.run_simulation()
        self.run_menu()

    def run_menu(self):
        print(MENU)
        choice = self.accept_menu_choice()

        if choice == '1':
            package = self.accept_id_and_get_package()
            time = self.accept_time()
            original_status = package.status
            if time >= package.log['at hub']:
                package.status = 'at hub'
            if time >= package.log['en route']:
                package.status = 'en route'
            if time >= package.log['delivered']:
                package.status = original_status
            print("\n| ID | Address | City | State | Zip Code | Weight | Deadline | Status | Truck |")
            print(package)
            input("\n    Press ENTER to return to menu")
            self.run_menu()

        if choice == '2':
            time = self.accept_time()
            all_packages = self.trucks[0].packages + self.trucks[1].packages + self.trucks[2].packages
            all_packages.sort(key=lambda x: x.id_)
            print("\n| ID | Address | City | State | Zip Code | Weight | Deadline | Status | Truck |")
            for pkg in all_packages:
                self.sync_package_status_with_time(pkg, time)
                print(pkg)
            input("\n    Press ENTER to return to menu")
            self.run_menu()

        if choice == '3':
            sys.exit("Goodbye!")

    def run_simulation(self):
        # First driver will drive Truck 2
        t2 = self.trucks[1]
        time = datetime.datetime.strptime('08:00:00', '%H:%M:%S')
        t2.drive_route(time, self.distances)
        start_time = t2.start_time.strftime('%H:%M:%S')
        end_time = t2.time_of_completion.strftime('%H:%M:%S')
        miles_2 = round(t2.miles_driven, 1)
        print(f"Truck {t2.id_}: start {start_time}, end {end_time}, miles {miles_2}")

        # Package 9's address is updated at 10:20 AM
        address_update_time = datetime.datetime.strptime("10:20:00", '%H:%M:%S')
        package_9 = self.packages.get(9)
        package_9.address = '410 S State St'
        package_9.zip_code = '84111'

        # When the first driver is done driving Truck 2,
        # they will drive Truck 3 after Package 9's address was updated
        truck_3_start_time = t2.time_of_completion
        if truck_3_start_time < address_update_time:
            truck_3_start_time = address_update_time
        t3 = self.trucks[2]
        t3.route = optimize_route(t3.packages, self.distances)
        t3.drive_route(truck_3_start_time, self.distances)
        start_time = t3.start_time.strftime('%H:%M:%S')
        end_time = t3.time_of_completion.strftime('%H:%M:%S')
        miles_3 = round(t3.miles_driven, 1)
        print(f"Truck {t3.id_}: start {start_time}, end {end_time}, miles {miles_3}")

        # Second driver waits for delayed packages, then drives Truck 1
        t1 = self.trucks[0]
        time = datetime.datetime.strptime('09:50:00', '%H:%M:%S')
        t1.drive_route(time, self.distances)
        start_time = t1.start_time.strftime('%H:%M:%S')
        end_time = t1.time_of_completion.strftime('%H:%M:%S')
        miles_1 = round(t1.miles_driven, 1)
        print(f"Truck {t1.id_}: start {start_time}, end {end_time}, miles {miles_1}")

        print()
        print(f"Total miles for all trucks: {round(miles_1 + miles_2 + miles_3, 1)}")
        print()

    def accept_menu_choice(self):
        while True:
            choice = input(f"Please choose a menu option: ")
            if choice not in ('1', '2', '3'):
                print(f"Invalid input. Enter 1, 2, or 3.")
                continue
            return choice

    def accept_id_and_get_package(self):
        while True:
            package_id = input(f"    Please enter a package id: ")
            if package_id == 'MENU':
                self.run_menu()
                return
            package = self.packages.get(int(package_id))
            if package is None:
                print("    Package not found. Input a valid package id, or input 'menu' to go back to menu.")
                continue
            return package

    def accept_time(self):
        while True:
            time = input(f"    Please enter time as HH:MM in 24hr clock time: ")
            if time == 'menu':
                self.run_menu()
                return
            is_valid = True
            if len(time) != 5:
                is_valid = False
            if time[2] != ':':
                is_valid = False
            try:
                time = datetime.datetime.strptime(time, '%H:%M')
            except ValueError as ve:
                is_valid = False
            if is_valid is False:
                print("    Invalid input. Please input as HH:MM, or input 'menu' to go back to menu.")
                continue
            return time

    def sync_package_status_with_time(self, package, time):
        original_status = package.status
        package.status = 'at hub'
        if time >= package.log['en route']:
            package.status = 'en route'
        if time >= package.log['delivered']:
            package.status = original_status


