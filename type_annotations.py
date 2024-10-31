from typing import List
from typing_extensions import Annotated

XYZ = Annotated[List[int], "length=3"]
RelativeXYZ = Annotated[List[str], "length=3"]
