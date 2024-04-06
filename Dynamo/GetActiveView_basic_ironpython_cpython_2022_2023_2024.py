import clr
clr.AddReference('RevitNodes')
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = DocumentManager.Instance.CurrentDBDocument

element = doc.ActiveView

if element.Category.Id == ElementId(BuiltInCategory.OST_Views):
	active_view = element

OUT = active_view