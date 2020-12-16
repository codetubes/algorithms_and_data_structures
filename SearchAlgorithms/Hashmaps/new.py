

class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        updated=False
        for index, item in enumerate(bucket):
            item_key, item_value =  item
            if item_key == key:
                updated=True
                bucket[index] = (key, value)
                break
        if not updated:
            bucket.append((key,value))


    def get_val(self,key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        for index, item in enumerate(bucket):
            item_key, item_value = item
            if item_key == key:
                return item_value
        raise Exception("Item not found")

    def __str__(self):
        return "".join([str(item) for item in self.hash_table])


hash_table = HashTable(256)
hash_table.set_val("arman@gmail.com", "Hey there")
print(hash_table)
hash_table.set_val("simon@gmail.com",{
    "first_name":"Simon",
    "last_name":"Johns",
    "age":57
})
print(hash_table)
print(hash_table.get_val("simon@gmail.com"))