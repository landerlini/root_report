# root_report
Simple python package to create HTML report out of Cern ROOT scripts.

## Example 
```
from root_report import Report 
import ROOT

ROOT.SetBatch(1) 

report = Report ( "name_of_the_report", "/some/browser-accessible/path/" ) 
report.outputTitle ( "Title of the Report" )

f1 = ROOT.TF1 ( "parab", "x**2", -1, 1)
f1.Draw()

report.outputCanvas ( "figureIdentifier" ) 
report << "Some <B>HTML</B> description here. " << report.br 

report.close() 
```
