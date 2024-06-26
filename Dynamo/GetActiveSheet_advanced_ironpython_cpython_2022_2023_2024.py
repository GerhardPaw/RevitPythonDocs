import clr
clr.AddReference("RevitNodes")
clr.AddReference("RevitServices")
clr.AddReference("RevitAPI")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = DocumentManager.Instance.CurrentDBDocument

active_view = doc.ActiveView

if active_view.Category.Id != ElementId(BuiltInCategory.OST_Sheets):
    raise TypeError("Active view is not of category Sheets")

OUT = active_view