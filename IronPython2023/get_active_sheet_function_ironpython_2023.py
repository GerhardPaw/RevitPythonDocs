import clr
clr.AddReference('RevitNodes')
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')
from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

def get_active_sheet():
	try:
		element = doc.ActiveView
		if element.Category.Id.IntegerValue == int(BuiltInCategory.OST_Sheets):
			active_view = element
			return active_view
		else:
			return 'Active view is not of category Views'
	except:
		return 'Error accessing active view'

active_sheet = get_active_sheet()

OUT = active_sheet
