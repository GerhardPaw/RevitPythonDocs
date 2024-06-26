import clr
clr.AddReference("RevitAPI")
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, View, ViewType

doc = DocumentManager.Instance.CurrentDBDocument

views = FilteredElementCollector(doc).OfClass(View)
templates = []

for view in views:
    if view.ViewType == ViewType.Schedule and view.IsTemplate == True:
        templates.append(view)

if not templates:
    raise ValueError("No view templates found")

OUT = templates