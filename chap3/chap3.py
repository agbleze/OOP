#%% 
from __future__ import annotations
from typing import List, Any, Optional
from math import hypot

#%%
class ContactList(list["Contact"]):
    def search(self, name: str) -> list["Contact"]:
        matching_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            return matching_contacts
class Contact:
    all_contacts: ContactList()
    
    def __init__(self, /, name: str = "", email: str ="", 
                 **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
    def __repr__(self) -> str:
        return (
                f"{self.__class__.__name__}("
                f"{self.name!r}, {self.email!r}"
                f")"
            )
        
#%%
Contact.all_contacts = ContactList()
c_1 = Contact('Dusty', 'dusty@example.com')
c_2 = Contact('Steve', 'steeve@example.com')
c3 = Contact("Jenna", "cutty@sark.io")

[c.name for c in Contact.all_contacts.search('Dusty')]

#print(Contact.all_contacts)


#%%
test_search = """
>>> Contact.all_contacts = ContactList()
>>> c1 = Contact("John A", "johna@example.net")
>>> c2 = Contact("John B", "johnb@sloop.net")
>>> c3 = Contact("Jenna C", "cutty@sark.io")
>>> [c.name for c in Contact.all_contacts.search('John')]
['John A', 'John B']
"""
#%%
class Supplier(Contact):
    def order(self, order: "Order") -> None:
        print("If this were a real systems we would send "
              f"'{order}' order to '{self.name}'"
              
            )

# %%
c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.com")
print(c.name, c.email, s.name, s.email)
# %%
from pprint import pprint
pprint(c.all_contacts)

#%%
class LongNameDict(dict[str, int]):
    def longest_key(self) -> Optional[str]:
        """In effect max(self, key=len), but less obscure"""
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest

#%%
articles_read = LongNameDict()
articles_read['lucy'] = 42
articles_read['c_c_philips'] = 6
articles_read['steve'] = 7
articles_read.longest_key()

max(articles_read, key=len)

# %%  
# OVERRIDING nd super
# multiple inheritance

class AddressHolder:
    def __init__(self,
                 /, 
                 street:str, 
                 city: str, 
                 state: str, 
                 code: str,
                 **kwargs: Any
                 )->None:
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        

class Friend(Contact, AddressHolder):
    def __init__(self, 
                 /,
                 phone: str = "",
                 **kwargs: Any
                 ) -> None:
        super().__init__(**kwargs)
        self.phone = phone
# %%
#f = Friend("Dusty", "Dusty@private.com", "555-1212")
#Contact.all_contacts

######################################################################
# %% Diamond inheritance
class BaseClass:
    num_base_calls = 0
    
    def call_me(self):
        print("Calling methods on BaseClass")
        self.num_base_calls += 1
        
class LeftSubclass_S(BaseClass):
    num_left_calls = 0
    
    def call_me(self) -> None:
        super().call_me()
        print("Calling methond on LeftSubclass")
        self.num_left_calls += 1
        
class RightSubclass_S(BaseClass):
    num_right_calls = 0
    
    def call_me(self) -> None:
        super().call_me()
        print("Calling method on the RightSubclass")
        self.num_right_calls += 1
        
class Subclass_S(LeftSubclass_S, RightSubclass_S):
    num_sub_calls = 0
    
    def call_me(self) -> None:
        super().call_me()
        print("cALLING method on subclass")
        self.num_sub_calls += 1
        

# %%
ss = Subclass_S()
ss.call_me()
# %%


############################ Polymorphism  ################################
#%%
from pathlib import Path

class AudioFile:
    ext: str
    
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format")
        self.filepath = filepath
        
class MP3File(AudioFile):
    ext = ".mp3"
    
    def play(self) -> None:
        print(f"playing {self.filepath} as mp3")
        
class WavFile(AudioFile):
    ext = ".wav"
    
    def play(self) -> None:
        print(f"playing {self.filepath} as wav")
        
class OggFile(AudioFile):
    ext = ".ogg"
    
    def play(self) -> None:
        print(f"playing {self.filepath} as ogg")

#%%
p1 = MP3File(Path("Heart of the sunrise.mp3"))
p1.play()

p2 = WavFile(Path("Roundabout.wav"))
p2.play()


######################## case study  ##########################
# %%
class ED(Distance):
    def distance(self, s1: "Sample", s2: "Sample") -> float:
        return hypot(
            s1.sepal_length - s2.sepal_length,
            s1.sepal_width - s2.sepal_width,
            s1.petal_length - s2.petal_length,
            s1.petal_width - s2.petal_width,
        )









