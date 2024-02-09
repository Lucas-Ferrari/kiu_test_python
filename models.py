class Clients:
    def __init__(self, client_id, name, email, phone, address):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"Id: {self.client_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"


class Travels:
    def __init__(self, travel_id, origin, destination, date):
        self.travel_id = travel_id
        self.origin = origin
        self.destination = destination
        self.date = date

    def __repr__(self):
        return f"Id: {self.travel_id}, Origin: {self.origin}, Destination: {self.destination}, Date: {self.date}"


class Packages:
    def __init__(self, package_id, client, travel, description):
        self.package_id = package_id
        self.client = client
        self.travel = travel
        self.description = description

    def __repr__(self):
        return f"Id: {self.package_id}, Client: {self.client}, Travel: {self.travel}, Description: {self.description}"
