import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, View, ViewType
import Autodesk
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

def get_view_templates():
	views = FilteredElementCollector(doc).OfClass(View)
	templates = []
	for view in views:
		if view.ViewType != ViewType.ThreeD and view.ViewType != ViewType.Schedule and view.ViewType != ViewType.Section and view.IsTemplate == True:
			templates.append(view)
	return templates

templates = get_view_templates()
OUT = templates