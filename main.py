import random

class LRU:
    # Initialising the class variables
    def __init__(self,size):
        self.hit=0
        self.miss=0
        self.order=[]
        self.size=size
    
    #Function for accessing a page, It registers the hit if the page accessed is in the cache else it is a miss.
    #We use a simple double ended Queue for this.
    #The least recently used is put in the front and is removed using pop(0) where 0 is the index
    #The newly Added/Hit element is appended to the end of the queue.
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
    
    #Function to compute the hit and miss rate.
    def stats(self):
        sum=self.hit+self.miss
        hit_rate=self.hit/sum
        miss_rate=self.miss/sum
        if sum>0:
            return(
                f"Hits: {self.hit}\n"
                f"Misses: {self.miss}\n"
                f"Hit rate: {hit_rate}\n"
                f"Miss rate: {miss_rate}"
            )
        else:
            return 0
        
    #Function to simulate the cache accessing, it uses the random module to create a random sequence of elements.
    def simulate(self,number,max):
        for i in range(0,number):
            random_page=random.randint(1,max)
            print("Accessing page:",random_page)
            y=self.access(random_page)
            if y==1:
                print("HIT")
            else:
                print("MISS")


#Creating a class and calling the needed function. The parameter is the size of the cache
cache=LRU(10)
#Simulating the accessing of the cache and the parameter is the number of pages requested and
# max element random can choose upto.
cache.simulate(20,100)
#Computing the stats and priting it
x=cache.stats()
print(x)
    
