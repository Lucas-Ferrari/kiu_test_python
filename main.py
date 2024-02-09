from models import Clients, Travels, Packages

# Constants
PACKAGE_COST = 10
DAILY_REPORT = {
    "date": "",
    "total_packages": 0,
    "total_earnings": 0,
}


def setUp():
    tb_clients, tb_travels, tb_packages = [], [], []
    return tb_clients, tb_travels, tb_packages


def create_sample_data(tb_clients, tb_travels, tb_packages):
    # TODO: Remove from file
    # Create some travels
    travel_1 = Travels(1, "Buenos Aires", "Córdoba", "2023-12-01")
    travel_2 = Travels(2, "Buenos Aires", "Rosario", "2023-12-02")
    travel_3 = Travels(3, "Buenos Aires", "Mendoza", "2023-12-03")
    travel_4 = Travels(4, "Buenos Aires", "Salta", "2023-12-03")

    # Load travels into the table
    insert_data(tb_travels, travel_1)
    insert_data(tb_travels, travel_2)
    insert_data(tb_travels, travel_3)
    insert_data(tb_travels, travel_4)

    # Create some clients
    client_1 = Clients(
        1, "Juan Perez", "juanperez@gmail.com", "1151112233", "Calle Falsa 123"
    )
    client_2 = Clients(
        2, "Jorge Ramirez", "jorgeramirez@gmail.com", "1151112233", "Calle Falsa 321"
    )
    client_3 = Clients(
        3, "Ana Lopez", "analopez@gmail.com", "1151112233", "Avenida Verdadera 111"
    )
    client_4 = Clients(
        4, "Laura Gomez", "lauragomez@gmail.com", "1151112233", "Ruta 15 213"
    )

    # Load clients into the table
    insert_data(tb_clients, client_1)
    insert_data(tb_clients, client_2)
    insert_data(tb_clients, client_3)
    insert_data(tb_clients, client_4)

    # Create some packages with the clients and travels
    package_1 = Packages(1, client_1.client_id, travel_1.travel_id, "Fragile")
    package_2 = Packages(2, client_2.client_id, travel_1.travel_id, "Urgent")
    package_3 = Packages(3, client_3.client_id, travel_1.travel_id, "Normal")
    package_4 = Packages(4, client_4.client_id, travel_2.travel_id, "Fragile")
    package_5 = Packages(5, client_1.client_id, travel_2.travel_id, "Green box")
    package_6 = Packages(6, client_2.client_id, travel_2.travel_id, "Red box")
    package_7 = Packages(7, client_3.client_id, travel_3.travel_id, "Blue box")
    package_8 = Packages(8, client_4.client_id, travel_3.travel_id, "Fragile")
    package_9 = Packages(9, client_1.client_id, travel_4.travel_id, "Heavy")
    package_10 = Packages(10, client_1.client_id, travel_4.travel_id, "Heavy")
    package_11 = Packages(11, client_1.client_id, travel_4.travel_id, "Heavy")
    package_12 = Packages(12, client_1.client_id, travel_4.travel_id, "Heavy")

    # Load packages into the table
    insert_data(tb_packages, package_1)
    insert_data(tb_packages, package_2)
    insert_data(tb_packages, package_3)
    insert_data(tb_packages, package_4)
    insert_data(tb_packages, package_5)
    insert_data(tb_packages, package_6)
    insert_data(tb_packages, package_7)
    insert_data(tb_packages, package_8)
    insert_data(tb_packages, package_9)
    insert_data(tb_packages, package_10)
    insert_data(tb_packages, package_11)
    insert_data(tb_packages, package_12)


def insert_data(table, data):
    table.append(data)


def generate_report_by_day(tb_packages, tb_travels, day):
    report = DAILY_REPORT
    # Search all travls for the given day
    travels = [travel for travel in tb_travels if travel.date == day]

    # Search all packages for those travels, matching by travel_id
    packages = [
        package
        for package in tb_packages
        if package.travel in [travel.travel_id for travel in travels]
    ]

    report["date"] = day
    report["total_packages"] = len(packages)
    report["total_earnings"] = len(packages) * PACKAGE_COST
    return report


def main():
    # Create new tables
    tb_clients, tb_travels, tb_packages = setUp()

    # Create sample data
    create_sample_data(tb_clients, tb_travels, tb_packages)

    # Generate report by day
    report = generate_report_by_day(tb_packages, tb_travels, "2023-12-03")
    print(report)
    pass


if __name__ == "__main__":
    main()
