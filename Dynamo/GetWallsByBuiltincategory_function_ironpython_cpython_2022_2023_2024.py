import clr
clr.AddReference("RevitAPI")
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

def get_walls():
    walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).ToElements()
    if not walls:
        raise ValueError("No walls found")
    return walls

walls = get_walls()

OUT = walls