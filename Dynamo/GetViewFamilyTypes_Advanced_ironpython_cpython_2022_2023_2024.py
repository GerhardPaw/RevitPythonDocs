import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, ViewFamilyType

doc = DocumentManager.Instance.CurrentDBDocument

view_family_types = FilteredElementCollector(doc).OfClass(ViewFamilyType).WhereElementIsElementType().ToElements()

if not view_family_types:
	raise ValueError('No view family types found')

OUT = view_family_types