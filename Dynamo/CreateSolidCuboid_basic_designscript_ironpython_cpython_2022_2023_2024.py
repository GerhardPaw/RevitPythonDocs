import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Cuboid

solid_dynamo = Cuboid.ByLengths(10.0, 10.0, 10.0)

OUT = solid_dynamo