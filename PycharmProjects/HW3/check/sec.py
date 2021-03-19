class LUD:
    def __init__(self, memory_size):
        if (memory_size < 1):
            raise ValueError('Error memory size')
        self.memory_size = memory_size
        self.data = {2,3,4,5,7,8}
        self.usage = {0,2,3,4,7,8}
    def put(self, key, value):
        if(len(self)==self.memory_size and key not in self):
            mkey,mval = min(self.usage.items(),key=lambda x:x[1])
            self.data.pop(mkey)
            self.usage.pop(mkey)
            self.data[key] = value
            self.usage[key] = 0

    def __len__(self):
        return len(self.data)


x = LUD(10)
print('data',x.data,'usage',x.usage)

x.put('asa',22)
print('data',x.data,'usage',x.usage)

import random
random.seed("lior")
x = random.randrange(0,20)
print(x)
print(x)