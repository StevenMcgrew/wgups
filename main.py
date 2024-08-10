from package import Package
from truck import Truck


def main():
    package1 = Package(35, "123 Main St", "2024-08-15", "New York", "10001", 2.5, "Out for Delivery")
    truck1 = Truck(2, 100, "10:00 AM")

    print(package1.address)  # Output: 123 Main St
    print(package1.deadline)  # Output: 2024-08-15
    print(package1.city)  # Output: New York
    print(package1.zip_code)  # Output: 10001
    print(package1.weight)  # Output: 2.5
    print(package1.status)
    print(truck1.time_finished)


if __name__ == '__main__':
    main()
