import clr
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

viewports = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Viewports).WhereElementIsNotElementType().ToElements()
viewport_types = [doc.GetElement(id) for id in viewports[0].GetValidTypes()]
OUT = viewport_typesypes()]
	return viewport_types

viewport_types = get_viewport_types()

OUT = viewport_types