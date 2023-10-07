###### singleton pattern --- not recommended for use in python

#%%
class OnlyOne:
    _single = None
    def __new__(cls, *args, **kwargs):  ### create a new instance when called first time
        if not cls._single:
            cls._single = super().__new__(cls, *args, **kwargs)
        return cls._single
        
        
o1 = OnlyOne()
o2 = OnlyOne()

o1 == o2
# %%
