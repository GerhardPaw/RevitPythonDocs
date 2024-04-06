import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import XYZ, Line, CurveLoop, Solid, GeometryCreationUtilities

width = 10.0
length = 20.0
p0 = XYZ(0, 0, 0)
p1 = XYZ(width, 0, 0)
p2 = XYZ(width, length, 0)
p3 = XYZ(0, length, 0)
line1 = Line.CreateBound(p0, p1)
line2 = Line.CreateBound(p1, p2)
line3 = Line.CreateBound(p2, p3)
line4 = Line.CreateBound(p3, p0)
curveLoop = CurveLoop()
curveLoop.Append(line1)
curveLoop.Append(line2)
curveLoop.Append(line3)
curveLoop.Append(line4)
height = 15.0

solid_revit = GeometryCreationUtilities.CreateExtrusionGeometry([curveLoop], XYZ.BasisZ, height)

OUT = solid_revit