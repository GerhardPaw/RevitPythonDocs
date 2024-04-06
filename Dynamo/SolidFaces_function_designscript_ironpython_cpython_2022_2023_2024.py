import clr
clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import Solid

def get_faces(solid):
    if not isinstance(solid, Solid):
        raise ValueError("Input is not a dynamo solid")

    faces = solid.Faces

    if not faces:
    raise ValueError("No faces found")

    return faces

solid_dynamo = IN[0]
faces = get_faces(solid_dynamo)

OUT = faces