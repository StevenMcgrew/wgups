class Package:
    def __init__(self, id_, address_id, address, city, state, zip_code, deadline, weight, status, log, truck_name=None):
        self.id_ = id_
        self.address_id = address_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.log = log
        self.truck_name = truck_name

    def __str__(self):
        return str([self.id_,
                    self.address,
                    self.city,
                    self.state,
                    self.zip_code,
                    self.weight,
                    self.deadline,
                    self.status,
                    self.truck_name
                    ])

    def __eq__(self, other):
        if not hasattr(other, 'id_'):
            return False
        return self.id_ == other.id_
