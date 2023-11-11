import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Solid, Cuboid

def create_solid_dynamo():
	width = 10.0
	length = 20.0
	height = 15.0
	solid = Cuboid.ByLengths(width, length, height)
	return solid

solid_dynamo = create_solid_dynamo()

OUT = solid_dynamo