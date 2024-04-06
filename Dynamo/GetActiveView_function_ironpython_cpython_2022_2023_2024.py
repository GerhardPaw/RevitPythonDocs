import clr
clr.AddReference('RevitNodes')
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = DocumentManager.Instance.CurrentDBDocument

def get_active_view():

	active_view = doc.ActiveView
	if active_view.Category.Id != ElementId(BuiltInCategory.OST_Views):
		raise TypeError('Active view is not of category Views')

	return active_view

active_view = get_active_view()

OUT = active_view