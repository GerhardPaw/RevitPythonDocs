import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, ViewSheet

doc = DocumentManager.Instance.CurrentDBDocument

sheets = FilteredElementCollector(doc).OfClass(ViewSheet).ToElements()

OUT = sheets