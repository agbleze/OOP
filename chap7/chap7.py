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

#%% 
import datetime
def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low)/2), date)

#%% NamedTuple
from typing import NamedTuple


#%%
class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float
    
    @property
    def middle(self) -> float:
        return (self.high + self.low)/2
    
    

#%%
Stock("AAPL", 123.52, 137.98, 53.15)

#%%
s2 = Stock("AAPL", 123.52, high=137.98, low=53.15)


#%%
s2.high

symbol, current, high, low = s2

#%%
s2.middle

# %% tuple can contain mutable elements
t = ("Relayer", ["Gates of Delirium", "Sound Chaser"])
t[1].append("To Be Over")
t





# %%
