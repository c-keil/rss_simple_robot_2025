import os
from xacrodoc import XacroDoc

doc = XacroDoc.from_file("robot/simple.xacro")

# or write to a file
doc.to_urdf_file("robot/simple.urdf")