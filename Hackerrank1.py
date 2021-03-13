# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

k,arr = int(input()),list(map(int, input().split()))

counter = collections.Counter(arr)
list1 = list(counter.values())
list2 = list(counter.keys())

for i in counter.values():
    
    if i != k:
        
        final_value = i
        a = list1.index(final_value)
        print(list2[a])
        
        
    
