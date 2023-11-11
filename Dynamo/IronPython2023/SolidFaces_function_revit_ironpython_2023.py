import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import XYZ, Line, CurveLoop, Solid, GeometryCreationUtilities

def get_faces(solid):
	if isinstance(solid, Solid):
		faces = solid.Faces
		return faces
	else:
		return 'Input is not a Revit Solid.'

solid_revit = IN[0]
faces = get_faces(solid_revit)

OUT = faces