**Name**: Angelica Hanley, **UFID**: 85716778

**Name**: Mikayla Cohen, **UFID**: 62308954

Description:
- This program implements and compares three cache eviction policies on the same request sequence. These are FIFO (First-In, First-Out), LRU (Least Recently Used), and OPTFF (Belady’s Farthest-in-Future, optimal offline). This program runs each cache eviction policy and outputs the total amount of cache misses.

Instructions to compile and run the code:
- Clone the repository
- Navigate to the project root directory 
- In src/main.py, set the filename inside open() to the wanted input file
- Run the program using python src/main.py
    - If your system uses "py", run: py src/main.py
    - If your system uses "python3", run: python3 src/main.py

Assumptions:
- The first number in the input file is k, cache capacity (k >= 1)
- The second number in the input file is m, number of requests
- The rest is ( r_1, .., r_m ) = sequence of integer IDs

Question 1:
- <img width="567" height="168" alt="Screenshot 2026-03-02 at 4 29 22 PM" src="https://github.com/user-attachments/assets/99438155-fc42-4e1e-9c43-e698a3bea5a5" />


Question 2:
Such a sequence does exist: 8 6 4 2 8 6 4 1 2 8 6 4 1
k = 3
m = 13

Miss count: 
LRU: 13
FIFO: 13
OPTFF: 8

LRU evicts the page that was least recently used by looking at the previous accesses in the cache. Therefore, even if that page is needed in the future relatively soon, the page is still removed because LRU is only considering the past pages, rather than also considering upcoming requests. Consequently, it can remove pages that could be reused in the near future, leading to misses that could have been avoided. Likewise, FIFO operates in a similar fashion. Rather than consider future requests before removing pages, it removes the page that has been in the cache for the longest. As a result, it also can remove pages that could be reused in the near future, leading to misses that could have been avoided, just like LRU. Unlike FIFO and LRU, OPTFF views future requests and considers them prior to evicting a page. This algorithm evicts the page whose use is farthest in the future, leading to less cache misses as the pages who are going to be used soon will remain in the cache. 


Question 3:
Let OPTFF be Belady’s Farthest-in-Future algorithm.
Let A be any offline algorithm that knows the full request sequence.

Both algorithms have the ability to view the future sequence. When the cache is full and there is a miss, both algorithms need to replace a page in the cache. Let n = the page OPTFF will choose to evict, the farthest in the future that will be needed. Let m = the page that A will choose to evict, a page that will be needed sooner than the page that OPTFF chose. This is due to the fact that OPTFF uses the one farthest in the future that will be needed. 


The first difference between these two algorithms is the page they choose to evict. Let’s exchange the page, m, that A will choose to evict with the greedy choice, n. Since m will be used in the future sooner than n will be, choosing to evict m cannot be the better option to evict compared to n. This is because A will have a miss sooner than OPTFF would have one with n as it will be used sooner than n. Therefore, if we replace m with n, the misses will not increase. A will not have fewer misses than OPTFF as it will log misses more frequently due to m’s closer proximity compared to n. If we repeat this process, A will eventually become OPTFF. Since OPTFF will have either the same amount of misses or less than, it is the more optimal algorithm with a number of misses no larger than of A.


