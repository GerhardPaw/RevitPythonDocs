import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

floors = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).ToElements()

if not floors:
	raise ValueError('No floors found')

OUT = floors