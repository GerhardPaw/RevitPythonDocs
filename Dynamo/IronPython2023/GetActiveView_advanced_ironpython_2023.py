import clr
clr.AddReference('RevitNodes')
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')
from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

try:
	element = doc.ActiveView
	if element.Category.Id.IntegerValue == int(BuiltInCategory.OST_Views):
		active_view = element
		OUT = active_view
	else:
		OUT = 'Active view is not of category Views'
except:
	OUT = 'Error accessing active view'