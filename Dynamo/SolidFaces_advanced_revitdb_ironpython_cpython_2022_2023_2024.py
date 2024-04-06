import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import Solid

solid_revit = IN[0]

if not isinstance(solid_revit, Solid):
	raise TypeError('Input is not a revit solid')

faces = solid_revit.Faces

if not faces:
	raise ValueError('No faces found')

OUT = faces