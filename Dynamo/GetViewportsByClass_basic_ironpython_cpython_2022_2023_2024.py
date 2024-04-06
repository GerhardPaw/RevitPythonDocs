import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, Viewport

doc = DocumentManager.Instance.CurrentDBDocument

viewports = FilteredElementCollector(doc).OfClass(Viewport).ToElements()

OUT = viewports