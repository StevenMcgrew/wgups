import datetime


class CLI:
    def __init__(self, packages, distances, trucks):
        self.packages = packages
        self.distances = distances
        self.trucks = trucks

    def run(self):
        self.run_simulation()

    def run_simulation(self):
        print()

        # Drive Truck 2
        t2 = self.trucks[1]
        time = datetime.datetime.strptime('08:00:00', '%H:%M:%S')
        t2.drive_route(time, self.distances)
        start_time = t2.start_time.strftime('%H:%M:%S')
        end_time = t2.time_of_completion.strftime('%H:%M:%S')
        miles_2 = round(t2.miles_driven, 1)
        print(f"Truck {t2.id_}: start {start_time}, end {end_time}, miles {miles_2}")

        # Drive Truck 3
        t3 = self.trucks[2]
        t3.drive_route(t2.time_of_completion, self.distances)
        start_time = t3.start_time.strftime('%H:%M:%S')
        end_time = t3.time_of_completion.strftime('%H:%M:%S')
        miles_3 = round(t3.miles_driven, 1)
        print(f"Truck {t3.id_}: start {start_time}, end {end_time}, miles {miles_3}")

        # Drive Truck 1
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

    def print_menu(self):
        pass

    def accept_menu_choice(self):
        pass
