

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
    
    










