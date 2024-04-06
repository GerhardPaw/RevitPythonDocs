import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, Wall

doc = DocumentManager.Instance.CurrentDBDocument

walls = FilteredElementCollector(doc).OfClass(Wall).ToElements()

OUT = walls