from collections import deque, OrderedDict

#fifo function - Evict the item that has been in the cache the longest
# k = capacity, m = list of requests
def fifo(k,m):
    #storing items currently in the cache
    cache=set()
    #tracking cache insertion order (FIFO)
    myQueue=deque()
    misses=0

    for x in m:
        #already in the cache = hit
        if x in cache:
            continue
        #if not, misses is incremented, since item not in cache
        misses=misses+1

        #if cache capacity is full, removed first in item (leftmost)
        if len(cache)==k:
            removedItem=myQueue.popleft()
            cache.remove(removedItem)
        #adds new item to cache and marks it as most recently inserted in queue
        cache.add(x)
        myQueue.append(x)
    return misses

def lru(k,m):
    cache=OrderedDict()
    misses=0

    for x in m:
        if x in cache:
            cache.move_to_end(x)
        else:
            misses=misses+1
    return misses

def main():
    #opening input file, splitting into individual values
    try:
        with open("data/example.in","r") as file:
            myData= file.read().strip().split()
    except FileNotFoundError:
        print("File opening error")
        return

    #1st number is cache capacity
    k=int(myData[0])
    #2nd number is number of requests
    requestsNum=int(myData[1])
    #rest is the list of request sequence, skips 1st 2 numbers
    requestStrings=myData[2:2+requestsNum]
    #converting request strings to ints
    m=[int(x) for x in requestStrings]
    #fifo ran and print out total misses
    fifoMisses=fifo(k,m)
    print(f"FIFO  : {fifoMisses}")

if __name__ == "__main__":
    main()