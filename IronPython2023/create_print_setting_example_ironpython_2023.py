import clr
import System
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import PrintRange

doc = DocumentManager.Instance.CurrentDBDocument

def get_paper_size(size):
	for p in print_manager.PaperSizes:
		if p.Name == size:
			return p

def get_paper_source(source):
	for source in print_manager.PaperSources:
		if source.Name == source:
			return source

def set_print_paramneters():
	print_parameters = print_manager.PrintSetup.CurrentPrintSetting.PrintParameters
	print_parameters.PaperSize = get_paper_size('A0')
	print_parameters.ZoomType = print_parameters.ZoomType.Zoom
	print_manager.PrintSetup.CurrentPrintSetting.PrintParameters.Zoom = 100
	#print_parameters.ZoomType = print_parameters.ZoomType.FitToPage
	print_parameters.PageOrientation = print_parameters.PageOrientation.Landscape
	#print_parameters.PageOrientation = print_parameters.PageOrientation.Portrait
	print_parameters.ViewLinksinBlue = False
	print_parameters.HideReforWorkPlanes = True
	print_parameters.HideUnreferencedViewTags = True
	print_parameters.MaskCoincidentLines = True
	print_parameters.HideScopeBoxes = True
	print_parameters.HideCropBoundaries = True
	print_parameters.ReplaceHalftoneWithThinLines = True

	print_parameters.ColorDepth = print_parameters.ColorDepth.Color
	#print_parameters.ColorDepth = print_parameters.ColorDepth.GrayScale
	#print_parameters.ColorDepth = print_parameters.ColorDepth.BlackLine

	print_parameters.HiddenLineViews = print_parameters.HiddenLineViews.RasterProcessing
	#print_parameters.HiddenLineViews = print_parameters.HiddenLineViews.VectorProcessing

	#print_parameters.RasterQuality = print_parameters.RasterQuality.High
	#print_parameters.RasterQuality = print_parameters.RasterQuality.Low
	#print_parameters.RasterQuality = print_parameters.RasterQuality.Medium
	print_parameters.RasterQuality = print_parameters.RasterQuality.Presentation

	#print_parameters.PaperPlacement = print_parameters.PaperPlacement.Center
	print_parameters.PaperPlacement = print_parameters.PaperPlacement.LowerLeft
	#print_parameters.PaperPlacement = print_parameters.PaperPlacement.Margins
	print_parameters.MarginType = print_parameters.MarginType.NoMargin
	#print_parameters.MarginType = print_parameters.MarginType.PrinterLimit
	#print_parameters.MarginType = print_parameters.MarginType.UserDefined
	#print_parameters.OriginOffsetX = 0.01
	#print_parameters.OriginOffsetY = 0.01

try:
	TransactionManager.Instance.EnsureInTransaction(doc)

	print_setting_name = 'print_setting_16'
	printer_name = 'PDF-XChange Standard'

	print_manager = doc.PrintManager
	print_manager.SelectNewPrintDriver(printer_name)
	p_range = System.Enum.Parse(PrintRange, 'Select')
	combined = True
	print_manager.PrintRange = p_range
	paper_size = get_paper_size('A0')
	paper_source = get_paper_source('source_01')
	print_manager.Apply()

	set_print_paramneters()

	print_manager.PrintSetup.SaveAs(print_setting_name)
	print_manager.Apply()

	TransactionManager.Instance.TransactionTaskDone()
	OUT = 'Success'

except Exception as e:
	TransactionManager.Instance.ForceCloseTransaction()
	OUT = str(e)
