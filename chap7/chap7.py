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


# %% dataclasses
from dataclasses import dataclass

@dataclass
class Stock:
    symbol: str
    current: float
    high: float
    low: float

#%%
s = Stock("AAPL", 123.52, 137.98, 53.15)

#%%
s.current

# %%
s.current = 122.25
s

#%%
s.unexpected_attribute = 'allowed'
s.unexpected_attribute


#%% dataclass can take default values
@dataclass
class StockDefaults:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

#%%
StockDefaults("GOOG")

#%%
StockDefaults("GOOG", 1826.77, 1847.20, 1013.54)

# %% EQUALITY TEST FOR dataclasses
stock2 = Stock(symbol='AAPL', current=122.25, high=137.98, low=53.15)

#%%
s == stock2

#%% 
stock3 = StockDefaults("GOOG", 1826.77, 1847.20, 1013.54)

stock2 == stock3 

# %% adding comparison to dataclass
@dataclass(order=True)
class StockOrdered:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

# %%
stock_ordered1 = StockOrdered("GOOG", 1826.77, 1847.20, 1013.54)
stock_ordered2 = StockOrdered("GOOG")
stock_ordered3 = StockOrdered("GOOG", 1728.28, high=1733.18, low=1666.33)

#%%
stock_ordered1 < stock_ordered2

from pprint import pprint
pprint(sorted([stock_ordered1, stock_ordered2, stock_ordered3]))


#%% DICTIONARY
stocks = {"GOOG": (111.2, 123.23, 29182.12, 442.123),
          "MSFT": (110.31, 891.120, 123.12, 129.19)
          }

#%%
stocks["GOOG"]

#%%
stocks["RIMM"] # Keyerror

# %%
print(stocks.get("RIMM"))
print(stocks.get("RIMM", "NOT FOUND"))

#%% USE setdefault to set values if key not found
# else return the value of key found
stocks.setdefault("GOOG", "INVALID")

#%% will set value bcos key if not found
stocks.setdefault("BB", (11.34, 10.33, 982.12, 341))

# %%
stocks["BB"]

#%% # items() returns tuple of key, values and 
# can be used in loops
for stock, values in stocks.items():
    print(f"{stock} last value is {values[0]}")

#%%
x = 2020
y = 2305843009213695971 #2182137291786219
hash(x) == hash(y)

#%% defaultdict to provide default value when key 
# is not found in dict
from collections import defaultdict

def letter_frequency_2(sentence: str) -> defaultdict[str, int]:
    frequencies: defaultdict[str, int] = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

#%% write function and pass them into defaultdict
from dataclasses import dataclass

@dataclass
class Prices:
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0
    
#%% class will run as function without providing values
Prices()

#%% pass class to defaultdict
portfolio = defaultdict(Prices)
portfolio['GOOG']

#%%
portfolio["AAPL"] = Prices(current=122.25, high=137.98, low=53.15)

#%%
pprint(portfolio)

#%% Counter will return dict with key as itmes being
# counted and vaues as number of items
import collections
from collections import Counter
responses = [
    "vanilla", "chocolate", "vanilla", "vanilla",
    "caramel", "strawberry", "vanilla"
]

def letter_frequency_3(sentence: str) -> Counter[str]:
    return Counter(sentence)

#%%
letter_frequency_3("try this text")

# %%
favorites = collections.Counter(responses).most_common(1)
name, frequency = favorites[0]
name


#%% sorting
from typing import Optional, cast, Any
import datetime









# %%
