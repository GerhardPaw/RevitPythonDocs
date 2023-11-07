import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, View, BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

def get_views():
	elements = FilteredElementCollector(doc).OfClass(View).ToElements()
	views = [element for element in elements if element.Category and element.Category.Id.IntegerValue == int(BuiltInCategory.OST_Views)]
	return views

views = get_views()
OUT = views