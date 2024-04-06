import clr
clr.AddReference("RevitAPI")
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).ToElements()

OUT = walls