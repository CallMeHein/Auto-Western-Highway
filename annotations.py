from typing import Annotated, List
from typing_extensions import Annotated

XYZ = Annotated[List[int], "length=3"]
