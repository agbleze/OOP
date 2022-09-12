#%%# Python data structures

o = object()

# %%
o.x = 5
# %%
import random
# %%
random.randint(5, 500)
# %%
from typing import List
import random as rd
def countsums(wuerfel: int, wuerfe: int, seiten: int) -> List[int]:
    A = []
    for i in range(wuerfe):
        A.append(sum([rd.randint(1, seiten+1) for i in range(wuerfel)]))
        
    A.sort()
    for i in A:
        A.count(i)
        
    return A
        
        
f = countsums(5,500,7)
print(f)        
        
        
        
#%%
rd.randint(1, 7+1)        
        
        
# %%
class MyObject:
    pass















