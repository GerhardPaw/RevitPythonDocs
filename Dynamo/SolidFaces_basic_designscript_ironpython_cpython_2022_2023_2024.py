import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Solid

solid_dynamo = IN[0]

faces = solid_dynamo.Faces

OUT = faces