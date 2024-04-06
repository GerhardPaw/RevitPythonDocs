import clr
clr.AddReference("RevitAPI")
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, Floor

doc = DocumentManager.Instance.CurrentDBDocument

floors = FilteredElementCollector(doc).OfClass(Floor).ToElements()

if not floors:
    raise ValueError("No floors found")

OUT = floors