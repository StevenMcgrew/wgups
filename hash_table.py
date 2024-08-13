class HashTable:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def get_row_list(self, key):
        row_index = hash(key) % len(self.table)
        return self.table[row_index]

    def insert(self, key, value):
        row_list = self.get_row_list(key)
        for item in row_list:
            if item[0] == key:
                item[1] = value
                return
        new_item = [key, value]
        row_list.append(new_item)

    def get(self, key):
        row_list = self.get_row_list(key)
        for item in row_list:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        row_list = self.get_row_list(key)
        for item in row_list:
            if item[0] == key:
                row_list.remove([item[0], item[1]])

    def __str__(self):
        primary_list = []
        for i in range(len(self.table)):
            current_row = self.table[i]
            intermediary_list = []
            for j in range(len(current_row)):
                current_item = current_row[j]
                intermediary_list.append([current_item[0], str(current_item[1])])
            primary_list.append(intermediary_list)
        return str(primary_list)
