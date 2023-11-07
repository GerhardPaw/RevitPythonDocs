import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

def create_material():
	def get_fill_pattern(doc, pattern_name):

		fill_patterns = FilteredElementCollector(doc).OfClass(FillPatternElement)
		fill_pattern = next((fp for fp in fill_patterns if fp.Name == pattern_name), None)
		return fill_pattern

	def get_appearance_asset(doc, asset_name):

		collector = FilteredElementCollector(doc).OfClass(AppearanceAssetElement)
		for asset in collector:
			if asset.Name == asset_name:
				return asset
		return None

	def set_properties(material):

		material.Color = color
		material.Shininess = 0.5
		material.Smoothness = 0.5
		material.Transparency = 10
		material.MaterialClass = 'Concrete'
		material.MaterialCategory = 'Structural'
		material.UseRenderAppearanceForShading = True
		material.AppearanceAssetId = asset.Id

		material.SurfaceForegroundPatternId = fill_pattern.Id
		material.SurfaceForegroundPatternColor = color
		material.SurfaceBackgroundPatternId = fill_pattern.Id
		material.SurfaceBackgroundPatternColor = color
		material.CutForegroundPatternId = fill_pattern.Id
		material.CutForegroundPatternColor = color
		material.CutBackgroundPatternId = fill_pattern.Id
		material.CutBackgroundPatternColor = color

	material_name = 'material_01'
	pattern_name = '<Solid fill>'
	asset_name = 'Cyan'
	color = Color(128, 128, 128)

	TransactionManager.Instance.EnsureInTransaction(doc)

	try:

		fill_pattern = get_fill_pattern(doc, pattern_name)
		if fill_pattern is None:
			raise Exception('Solid fill pattern not found.')

		asset = get_appearance_asset(doc, asset_name)
		if asset is None:
			raise Exception('Appearance asset not found.')

		material_id = Material.Create(doc, material_name)
		material = doc.GetElement(material_id)

		set_properties(material)

		TransactionManager.Instance.TransactionTaskDone()
		return material

	except Exception as e:
		TransactionManager.Instance.ForceCloseTransaction()
		return str(e)

material = create_material()

OUT = material
