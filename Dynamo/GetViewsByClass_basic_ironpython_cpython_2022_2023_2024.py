import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, View

doc = DocumentManager.Instance.CurrentDBDocument

views = FilteredElementCollector(doc).OfClass(View).ToElements()

OUT = views