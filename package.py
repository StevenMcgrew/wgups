class Package:
    def __init__(self, id_, address, city, state, zip_code, deadline, weight, status):
        self.id_ = id_
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):
        return str([self.id_,
                    self.address,
                    self.city,
                    self.state,
                    self.zip_code,
                    self.deadline,
                    self.weight,
                    self.status,
                    ])
