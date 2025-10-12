class HashTable:
    def __init__(self, capacity_initial=16, load_factor_initial=0.7):
        self.size = 0                       
        self.capacity = capacity_initial         
        self.load_factor = load_factor_initial
        self.table = [None] * self.capacity     
        self.DUMMY = object()                 

    def hash_key(self, key):
        return hash(key) % self.capacity

    def probe_index(self, key, step):
        return (self.hash_key(key) + step) % self.capacity

    def change_size(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for entry in old_table:
            if entry and entry is not self.DUMMY:
                k, v = entry
                self.insert(k, v)

    def insert(self, key, value):
        if self.size / self.capacity >= self.load_factor:
            self.change_size()

        step = 0
        while True:
            idx = self.probe_index(key, step)
            current_entry = self.table[idx]

            if current_entry is None or current_entry is self.DUMMY:
                self.table[idx] = (key, value)
                self.size += 1
                return
            elif current_entry[0] == key:
                self.table[idx] = (key, value)
                return
            else:
                step += 1

    def get(self, key):
        step = 0
        while True:
            idx = self.probe_index(key, step)
            current_entry = self.table[idx]

            if current_entry is None:
                raise KeyError(f"Key {key} not found")
            elif current_entry is self.DUMMY:
                step += 1
                continue
            elif current_entry[0] == key:
                return current_entry[1]
            else:
                step += 1

    def delete(self, key):
        step = 0
        while True:
            idx = self.probe_index(key, step)
            current_entry = self.table[idx]

            if current_entry is None:
                raise KeyError(f"Key {key} not found")
            elif current_entry is self.DUMMY:
                step += 1
                continue
            elif current_entry[0] == key:
                self.table[idx] = self.DUMMY
                self.size -= 1
                return
            else:
                step += 1
