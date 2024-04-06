import clr
clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import Solid

solid_dynamo = IN[0]

if not isinstance(solid_dynamo, Solid):
    raise TypeError("Input is not a dynamo solid")

faces = solid_dynamo.Faces

if not faces:
    raise ValueError("No faces found")

OUT = faces