import random

class LRU:
    def __init__(self,size):
        self.hit=0
        self.miss=0
        self.order=[]
        self.size=size
    
    def access(self,page):
        if page in self.order:
            self.hit+=1
            self.order.remove(page)
            self.order.append(page)
            return 1
        else:
            self.miss+=1;
            if len(self.order)>=self.size:
                self.order.pop(0)
            self.order.append(page)
            return 0
    
    def stats(self):
        sum=self.hit+self.miss
        if sum>0:
            return(
                f"Hits: {self.hit}\n"
                f"Misses: {self.miss}\n"
                f"Hit rate: {self.hit}/{sum}\n"
                f"Miss rate: {self.miss}/{sum}"
            )
        else:
            return 0
    def simulate(self,max):
        for i in range(0,self.size):
            random_page=random.randint(1,max)
            print("Accessing page:",random_page)
            y=self.access(random_page)
            if y==1:
                print("HIT")
            else:
                print("MISS")

cache=LRU(50)
cache.simulate(100)
x=cache.stats()
print(x)
    
