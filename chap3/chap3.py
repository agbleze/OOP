#%% 
from typing import List

#%%
class Contact:
    all_contacts: List["Contact"] = []
    
    def __init__(self, name: str, email: str) -> None:
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
c_1 = Contact('Dusty', 'dusty@example.com')
c_2 = Contact('Steve', 'steeve@example.com')
print(Contact.all_contacts)

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





# %%
