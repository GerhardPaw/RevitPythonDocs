import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, ViewFamilyType

doc = DocumentManager.Instance.CurrentDBDocument

def get_view_family_types():
	types = FilteredElementCollector(doc).OfClass(ViewFamilyType).WhereElementIsElementType().ToElements()
	if not types:
		raise ValueError('No view family types found')
	return types

view_family_types = get_view_family_types()

OUT = view_family_types