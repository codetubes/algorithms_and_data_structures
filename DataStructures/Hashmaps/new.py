


class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for i in range(self.size)]

    def set_val(self, key, value):
        #hashed_key = hash(key)%self.size
        hashed_key = 2
        bucket = self.hash_table[hashed_key]
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                bucket[index] = (key,value)
                return
        bucket.append((key,value))


    def get_val(self,key):
        #hashed_key = hash(key)%self.size
        hashed_key = 2
        bucket = self.hash_table[hashed_key]
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                return record

        return "Record Not Found"

        return self.hash_table[hashed_key]

    def __str__(self):
        return str(self.hash_table)


hash_table = HashTable(256)
hash_table.set_val("arman@gmail.com","Arman Avetisyan, 1993, Armenia")
hash_table.set_val("andrew@gmail.com","Andrew Hopkinns, 1993, USA")
print(hash_table.get_val("andrew@gmail.com"))