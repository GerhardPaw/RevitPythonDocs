import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Solid, Cuboid

def get_faces(solid):
    if isinstance(solid, Solid):
        faces = solid.Faces
        return faces
    else:
        return 'Input is not a Dynamo Solid.'

solid_dynamo = IN[0]
faces = get_faces(solid_dynamo)

OUT = faces