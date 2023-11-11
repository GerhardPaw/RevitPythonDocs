import clr
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

views = UnwrapElement(IN[0])
view_templates = UnwrapElement(IN[1])

def set_view_template():
	try:
		TransactionManager.Instance.EnsureInTransaction(doc)

		for view, view_template in zip(views, view_templates):
			view.ApplyViewTemplateParameters(view_template)

		TransactionManager.Instance.TransactionTaskDone()
		return views

	except Exception as e:
		TransactionManager.Instance.ForceCloseTransaction()
		return str(e)

result = set_view_template()

OUT = result