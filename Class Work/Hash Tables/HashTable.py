from LinkedList import LinkedList

class HashTable:
  def __init__(self):
    self.__length = 16
    self.__buckets = []

    for _ in range(self.__length):
      self.__buckets.append(LinkedList())

  def _get_bucket(self, key):
    return hash(key) % self.__length

  def insert(self, item):
    bucket_key = self._get_bucket(item[0])
    ll = self.__buckets[bucket_key]
    ll.append(item)

    print(ll)

  def lookup(self, key):
    bucket_key = self._get_bucket(key)
    ll = self.__buckets[bucket_key]
    return ll.find(key)



if __name__ == "__main__":
    hashest_table = HashTable()

    hashest_table.insert(("Alex", 18))
    hashest_table.insert(("Alex", 21))

    hashest_table.insert(("Sam", 20))

    print(hashest_table.lookup("Alex"))