from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = __revit__.ActiveUIDocument.Document

active_view = doc.ActiveView

if active_view.Category.Id == ElementId(BuiltInCategory.OST_Sheets):
	active_sheet = active_view

print active_sheet