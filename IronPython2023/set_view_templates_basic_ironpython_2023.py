import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

def get_views():
	elements = FilteredElementCollector(doc).OfClass(View).ToElements()
	views = [element for element in elements if element.Category and element.Category.Id.IntegerValue == int(BuiltInCategory.OST_Views)]
	return views

def get_view_templates():
	views = FilteredElementCollector(doc).OfClass(View)
	templates = []
	for view in views:
		if view.ViewType != ViewType.ThreeD and view.ViewType != ViewType.Schedule and view.ViewType != ViewType.Section and view.IsTemplate == True:
			templates.append(view)
	return templates

views = get_views()
view_template = get_view_templates()[0]

try:
	TransactionManager.Instance.EnsureInTransaction(doc)

	for view in views:
		view.ApplyViewTemplateParameters(view_template)

	TransactionManager.Instance.TransactionTaskDone()
	OUT = views

except Exception as e:
	TransactionManager.Instance.ForceCloseTransaction()
	OUT = str(e)