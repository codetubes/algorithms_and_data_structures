

class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return  [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key =hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        foundKey = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                foundKey = True
                break
        if foundKey:
            bucket[index] = (key,value)
        else:
            bucket.append((key,value))

    def get_val(self, key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        foundKey = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                foundKey = True
                break
        if foundKey:
            return record_value
        else:
            return "No Record Found"

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = HashTable(256)
print(hash_table)
hash_table.set_val("arman@gmail.com","My Names is Arman")
hash_table.set_val("simon@gmail.com","Hey what's up?")
print(hash_table)
hash_table.set_val("arman@gmail.com","Updated Value")
print(hash_table)
print(hash_table.get_val("arman@gmail.com"))