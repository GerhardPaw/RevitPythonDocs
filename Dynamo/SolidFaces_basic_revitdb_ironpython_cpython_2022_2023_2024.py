import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import Solid

solid_revit = IN[0]

faces = solid_revit.Faces

OUT = faces