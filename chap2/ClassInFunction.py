#%%
from typing import Optional

class Formatter:
    def format(self, string: str) -> str:
        pass
    
def format_string(string: str, 
                  formatter: Optional[Formatter] = None
                  )->str:
    """
    Format a string using the formatter object, which is expected
    to have a format() method that accepts a string.
    """
    
    class DefaultFormatter(Formatter):
        """
        Format a string with a title case
        """
        def format(self, string: str) -> str:
            return str(string).title()
        
    if not formatter:
        formatter = DefaultFormatter()
    return formatter.format(string)
 
 
#%%
hello_string = 'hello world, how are you doing?'
print(f" input: {hello_string}")   
# %%
print(f"output: {format_string(hello_string)}")
# %%
