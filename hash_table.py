class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    # Space Complexity: O(1) Time Complexity: O(n)
    # A self-adjusting algorithm that uses the move-to-front heuristic.
    def insert(self, key, value):
        bucket_index = self._hash(key)  # Compute the index for the key
        bucket = self.table[bucket_index]  # Get the bucket at the index
        for i, item in enumerate(bucket):  # Iterate through the bucket
            if item[0] == key:  # If the key already exists in the bucket
                item[1] = value  # Update the value
                bucket.pop(i)  # Remove the item from its current position
                bucket.insert(0, item)  # Insert the item at the front of the bucket
                return
        bucket.insert(0, [key, value])  # Insert the item at the front of the bucket

        # Move the most recently accessed item to the front of its bucket
        if len(bucket) > 1:
            most_recently_accessed = bucket.pop(-1)
            bucket.insert(0, most_recently_accessed)

    # Space Complexity: O(1)
    # Time Complexity: O(n)
    # Computes the index and iterates through the items in the bucks.
    def lookup(self, key):
        bucket_index = self._hash(key)
        bucket = self.table[bucket_index]
        for item in bucket:
            if item[0] == key:  # If the key already exists in the bucket
                return item[1]  # Return the value

    def get_all_keys(self):
        keys = []
        for bucket in self.table:
            for key, value in bucket:
                keys.append(key)
        return keys
