# RevitPythonDocs
Collection of Python Scripts for Dynamo and pyRevit.

**Welcome** to the revitpythondocs repository.<br>
This repository aims to foster a community-driven collection of scripts to enhance productivity and extend functionality within Revit through Python scripting.
The Python files contributed to this repo will automatically be loaded on [revitpythondocs.com](https://www.revitpythondocs.com) <br>

**General Coding Guidelines**<br>
This repo is dependent on your contribution.
To maintain a proper standard of quality and ensure consistency across contributions, we ask that all contributors adhere to the following guidelines.<br>

**Coding Style**<br>
Use snake_case or camelCase for variable names and function names. If you add a file to an existing script, maintain consistency within the script.<br>

**Imports**<br>
Necessary imports only as it helps beginners to get a better understanding for importing.<br>

**Comments and Docstrings:**<br>
Provide comments and explanations as needed to clarify complex logic or decisions made in your code. Avoid over-commenting by explaining only where necessary.
Use # for comments. If you wish to include the author's name, webpage, or email, start with a single-line comment at the top of the code.


For scripts where the title might not sufficiently explain the purpose, include a docstring after the imports of your script with a brief explanation of its functionality. Keep it short and simple.<br>
See the following example for a docstring.

<pre lang="python"><code>
import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import XYZ

"""
    This script creates a model curve by the end points of two model curves
    - Run
    - Select point on first model curve near the desired end
    - Select point on second model curve near the desired end
    - Finish selection
    - Model curve will be created with the same line style as selected model curve
"""

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication

rest of code
</code></pre>

**Script versions**
Scripts that represent a method or a single task have to be be categorized into one of four versions: 
+ **basic**
+ **advanced**
+ **function**
+ **example**.

Each version addresses a different level of complexity or use-case scenario. <br>
A more complex script that processes multiple task has to be categorized as a **tool**.

**Basic** code represents the most simple but working code that demonstrates the use of the task.
A basic code must not handle errors or varying inputs what is why it will not work for every scenario. Also it will not give user feedback and might fail silently.
See the following basic code for getting the active sheet.

<pre lang="python"><code>
import clr
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = DocumentManager.Instance.CurrentDBDocument

active_view = doc.ActiveView

if active_view.Category.Id == ElementId(BuiltInCategory.OST_Sheets):
    active_sheet = active_view

OUT = active_sheet
</code></pre>

**Advanced** code raises errors where necessary to give proper feedback to users.
Keep in mind that Dynamo already handles pretty much all exceptions itself what is why an excessive error handling is not necessary.
The error handling should focus on raising exceptions for null values to nprevent the code from failing silently.
If the script uses node inputs these have to be correctly handled for single elements and lists.
This code should work for all possible input scenarios and give user feedback in any possible case.
See the following advanced code for getting the active sheet.

<pre lang="python"><code>
import clr
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = DocumentManager.Instance.CurrentDBDocument

active_view = doc.ActiveView

if active_view.Category.Id != ElementId(BuiltInCategory.OST_Sheets):
    raise TypeError("Active view is not of category Sheets")

OUT = active_view
</code></pre>

**Function** code encapsulates the whole task into a function and calls it accordingly.
This code should handle errors and work for single element and list inputs.

<pre lang="python"><code>
import clr
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = DocumentManager.Instance.CurrentDBDocument

def get_active_sheet():

    active_view = doc.ActiveView
    if active_view.Category.Id != ElementId(BuiltInCategory.OST_Sheets):
        raise TypeError("Active view is not of category Sheets")

    return active_view

active_sheet = get_active_sheet()

OUT = active_sheet
</code></pre>

**Example** code demonstrates the use of the task in a larger workflow./b This gives the ability to use all possible API methods and properties related to the task.

See this link for an example: [Create Material](https://www.revitpythondocs.com/?search=Create%20Material)

A **Tool** is a larger, scripts encompassing multiple tasks or complex functionalities. Include a docstring at the beginning of the script, briefly explaining its purpose and any necessary background information.

See this example for a tool:[Model Curve By Curve Endpoints](https://www.revitpythondocs.com/?search=Tool%20Model%20Curve%20By%20Curve%20Endpoints)

**Contributing to the Repository**

We welcome contributions from everyone! To contribute your files it is **essential to follow the file name convention**. 
The process of loading your files to [revitpythondocs.com](https://www.revitpythondocs.com) is **fully automated** and can only work if you filenames are correct.

**File Name Convention**

Let´s look at an example and break it down:

**CreateMaterial_advanced_ironpython_cpython_2022_2023_2024.py**

+ The **script name** is the first part of the file name. Use CamelCase and the phrases will be seperated on the webpage later.
+ Provide a single **code version**: **basic, advanced, function, example** or **tool**.
+ Provide a single or multiple **python version**. Use can use **ironpython**, **cpython** or **ironpython_cpython**.
+ Providea single or multiple **Revit version**. 

A script for creating a material, that works for ironpython, cpython, Revit 2022-2024 and is provided with all 4 possible code versions will consist of the following files:

+ CreateMaterial_basic_ironpython_cpython_2022_2023_2024.py
+ CreateMaterial_advanced_ironpython_cpython_2022_2023_2024.py
+ CreateMaterial_function_ironpython_cpython_2022_2023_2024.py
+ CreateMaterial_example_ironpython_cpython_2022_2023_2024.py

As you can see, files that have the same script name will be combined into one button on the webpage.
It is your choice if you want to contribute the code in one or multiple versions.
Please add only Python version (ironpython, cpython) and Revit version (2022,2023,2024) attributes if you tested the script for the corresponding version. 

Fork the Repository: Start by forking this repository to your GitHub account.
Add Your Script: Place your script in the appropriate directory (Dynamo or pyRevit). Ensure it adheres to the naming rules and guidelines mentioned above.
Document Your Code: Include comments, a docstring if necessary, and ensure your code follows the prescribed coding style.
Create a Pull Request (PR): Once you've added your script, create a pull request to the main repository. In your PR, provide a brief overview of your script and its purpose.
Review: Your PR will be reviewed by the community. This process ensures that contributions align with the project's goals and quality standards. You may be asked to make revisions based on feedback.
By following these guidelines, we can together build a valuable resource for all Revit users looking to leverage Python for automation and customization. Your contributions not only help grow this repository but also support the broader Revit community in exploring new possibilities.

**Thank you for contributing and happy scripting!**
