from typing import List
from typing_extensions import Annotated

XYZ = Annotated[List[int], "length=3"]
