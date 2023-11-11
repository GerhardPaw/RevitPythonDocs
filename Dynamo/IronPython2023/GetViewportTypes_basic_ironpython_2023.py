import clr
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

viewport_types = []

viewports = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Viewports).WhereElementIsNotElementType().ToElements()
type_ids = viewports[0].GetValidTypes()
for type_id in type_ids:
	viewport_type = doc.GetElement(type_id)
	viewport_types.append(viewport_type)

OUT = viewport_types