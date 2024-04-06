import clr
clr.AddReference("RevitAPI")
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, View

doc = DocumentManager.Instance.CurrentDBDocument

def get_views():
    views = FilteredElementCollector(doc).OfClass(View).ToElements()
    if not views:
        raise ValueError("No views found")
    return views

views = get_views()

OUT = views