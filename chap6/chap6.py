#%%
import abc

class MediaLoader(abc.ABC):
    @abc.abstractmethod
    def play(self) -> None:
        ...
        
    @property
    @abc.abstractmethod
    def ext(self) -> str:
        ...

# %%
class Wav(MediaLoader):
    pass
# %%
x = Wav()
# %%
class Ogg(MediaLoader):
    ext = '.ogg'
    def play(self):
        pass
o = Ogg()

# %%
