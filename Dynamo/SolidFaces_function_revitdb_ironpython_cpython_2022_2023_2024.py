import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import Solid

def get_faces(solid):
    if not isinstance(solid, Solid):
        raise ValueError("Input is not a revit solid")

    faces = solid.Faces

    if not faces:
    raise ValueError("No faces found")

    return faces


solid_revit = IN[0]
faces = get_faces(solid_revit)

OUT = faces