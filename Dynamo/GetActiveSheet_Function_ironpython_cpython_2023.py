import clr
clr.AddReference('RevitNodes')
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

def get_active_sheet():

	active_view = doc.ActiveView
	if active_view.Category.Id.IntegerValue != int(BuiltInCategory.OST_Sheets):
		raise TypeError('Active view is not of category Sheets')

	return active_view

active_sheet = get_active_sheet()

OUT = active_sheet