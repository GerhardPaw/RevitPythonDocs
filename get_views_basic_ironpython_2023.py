import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, ViewSheet

doc = DocumentManager.Instance.CurrentDBDocument

elements = FilteredElementCollector(doc).OfClass(ViewSheet).ToElements()

OUT = elementsT = elements element in elements if element.Category and element.Category.Id.IntegerValue == int(BuiltInCategory.OST_Views)]

OUT = viewslement)
OUT = views