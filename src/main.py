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
    #if cache hit, add item to end
    for x in m:
        if x in cache:
            cache.move_to_end(x)
        #if cache miss, increment misses
        else:
            misses=misses+1
        #if capcity reached, removes the first item (least recently used)
            if len(cache)==k:
                cache.popitem(last=False)
            #inserts x into end of the cache OrderedDict
            cache[x]=None
    return misses


def optff(k,m):
    misses = 0
    cache = []
    position = 0

    for request in m:
        #if yes, there's a hit!
        if request in cache:
            position += 1
            continue

        #miss
        misses += 1

        #k is cache capacity, if less than, we can add, if not, evict
        if (len(cache) < k):
            cache.append(request)

        #time to evict --> OPTFF (cuz cache full)
        else:
            #item who has the farthest index for its next use
            farthestIndex = -1
            #evict this item
            evictedItem = None

            #current item in cache
            for item in cache:
                #we are going to search for this item's position
                nextPosition = -1

                #search in request list, position+1 to look at the following items after the current item
                for nextTimeUsed in range(position + 1, len(m)):
                    if m[nextTimeUsed]==item:
                        nextPosition = nextTimeUsed
                        break

                #item never used again so perf candidate to remove
                if nextPosition == -1:
                    evictedItem = item
                    break

                #find the one that has farthest index
                if nextPosition > farthestIndex:
                    farthestIndex = nextPosition
                    evictedItem = item

            #remove farthest-indexed item and then add the request
            cache.remove(evictedItem)
            cache.append(request)

        position+= 1

    return misses

def main():
    #opening input file, splitting into individual values
    try:
        with open("data/file3.in","r") as file:
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
    #lru ran and print out total misses
    lruMisses=lru(k,m)
    print(f"LRU   : {lruMisses}")

    #optff ran and print our total misses
    optffMisses=optff(k,m)
    print(f"OPTFF : {optffMisses}")

if __name__ == "__main__":
    main()