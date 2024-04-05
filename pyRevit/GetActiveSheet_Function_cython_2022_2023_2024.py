#! python3
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = __revit__.ActiveUIDocument.Document

def get_active_sheet():

	active_view = doc.ActiveView
	if active_view.Category.Id == ElementId(BuiltInCategory.OST_Sheets):
		return active_view
	else:
		raise TypeError('Active view is not of category Sheets')

active_sheet = get_active_sheet()

print (active_sheet)