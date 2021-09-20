
class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value


    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put("test",3)

# 이전값 제거 위험 -> linked list로 연결