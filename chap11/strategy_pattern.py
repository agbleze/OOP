

#### strategy pattern #####
import abc
from pathlib import Path
from PIL import Image
from typing import Tuple

Size = Tuple[int, int]

class FillAlgorithm(abc.ABC):
    @abc.abstractmethod
    def make_background(self, img_file: Path,
                        desktop_size: Size
                        ) -> Image:
        pass
    
    
class TilledStrategy(FillAlgorithm):
    def make_background(self, img_file: Path, 
                        desktop_size: Size
                        ) -> Image:
        in_img = Image.open(img_file)
        out_img = Image.open("RGB", desktop_size)
        num_tiles = [
                        o // i + 1 for o, i in zip(out_img.size, in_img.size)
                    ]
        for x in range(num_tiles[0]):
            for y in range(num_tiles[1]):
                out_img.paste(in_img,
                              (in_img.size[0]*x,
                               in_img.size[1]*y,
                               in_img.size[0]*(x + 1),
                               in_img.size[1]*(y + 1),
                               ),
                              )
                return out_img
            
            
            
class ScaledStrategy(FillAlgorithm):
    def make_background(self, img_file: Path,
                        desktop_size: Size
                        ) -> Image:
        in_img = Image.open(img_file)
        out_img = in_img.resize(desktop_size)
        return out_img
    
    
    
    
    
    
    
###

## Kitti output
## dir_setup
## coco2kitti
## main
## __init__.py
## __main__.py

            










