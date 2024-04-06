import clr
clr.AddReference("RevitNodes")
clr.AddReference("RevitServices")
clr.AddReference("RevitAPI")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = DocumentManager.Instance.CurrentDBDocument

active_view = doc.ActiveView

if active_view.Category.Id == ElementId(BuiltInCategory.OST_Sheets):
    active_sheet = active_view

OUT = active_sheet