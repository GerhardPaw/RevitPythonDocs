import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import FilteredElementCollector
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

types = FilteredElementCollector(doc).OfClass(Autodesk.Revit.DB.ViewFamilyType).WhereElementIsElementType().ToElements()

OUT = types_Viewports).WhereElementIsNotElementType().ToElements()
types = [doc.GetElement(i) for i in viewports[0].GetValidTypes()]
OUT = types