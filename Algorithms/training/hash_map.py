

class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for n in range(0,self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        updated=False
        for row_index, row in enumerate(bucket):
            f_key, f_value = row
            if f_key == key:
                bucket[row_index] = (key,value)
                updated=True

        if not updated:
            bucket.append((key, value))
    def get_val(self, key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        for row_index, row in enumerate(bucket):
            f_key, f_value = row
            if f_key == key:
                return bucket[row_index]

        return f"{key} not found in table"

    def __str__(self):
        return str(self.hash_table)

myTable = HashTable(256)
myTable.set_val("arman@gmail.com",{
    "full_name":"Arman Avetisyan",
    "age":25
})
myTable.set_val("julie@gmail.com",{
    "full_name":"Julie Ghazaryan",
    "age":27
})



print(myTable)
myTable.set_val("julie@gmail.com",{
    "full_name":"Julie Smith",
    "age":30
})
print(myTable)
print(myTable.get_val("julie@gmail.com"))