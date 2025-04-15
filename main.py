r=-1;f=-1
CAHCE_SIZE=5

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
        else:
            self.miss+=1;
            if len(self.order)>=self.size:
                self.order.pop(0)
            self.order.append(page)
    
#    def stats(self):
        #add the hit rate and miss rate calc here


#testing
chinNIG=LRU(5)
list=[1,1]

for i in list:
    chinNIG.access(i)
    