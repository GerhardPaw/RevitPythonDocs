import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Solid, Cuboid

width = 10.0
length = 20.0
height = 15.0
solid_dynamo = Cuboid.ByLengths(width, length, height)

OUT = solid_dynamo