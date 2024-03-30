import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

viewports = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Viewports).ToElements()

OUT = viewports