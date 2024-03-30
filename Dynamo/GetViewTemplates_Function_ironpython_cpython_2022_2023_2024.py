import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, View, ViewType

doc = DocumentManager.Instance.CurrentDBDocument

def get_view_templates():
	views = FilteredElementCollector(doc).OfClass(View)
	templates = []
	for view in views:
		if view.ViewType != ViewType.ThreeD and view.ViewType != ViewType.Schedule and view.IsTemplate == True:
			templates.append(view)
	if not templates:
		raise ValueError('No view templates found')
	return templates

templates = get_view_templates()

OUT = templates