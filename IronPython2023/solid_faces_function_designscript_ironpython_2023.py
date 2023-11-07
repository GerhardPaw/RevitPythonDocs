import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Solid, Cuboid

def dynamo_solid():
	width = 10.0
	length = 20.0
	height = 15.0
	solid = Cuboid.ByLengths(width, length, height)
	return solid

def faces_from_solid(solid):
	if isinstance(solid, Solid):
		faces = solid.Faces
		return faces
	else:
		return 'Input is not a Dynamo Solid.'

solid_dynamo = dynamo_solid()
faces = faces_from_solid(solid_dynamo)

OUT = faces