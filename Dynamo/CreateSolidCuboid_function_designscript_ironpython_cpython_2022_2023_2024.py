import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Cuboid

def create_solid_dynamo():

	solid = Cuboid.ByLengths(10.0, 10.0, 10.0)
	return solid

solid_dynamo = create_solid_dynamo()

OUT = solid_dynamo