'''AUTHOR = John
Kuriakose
description = A
prgm
that
contains
various
usages
of
datetime
module
'''
from datetime import datetime

current = datetime.now()
print(current)
form = current.strftime("%a")
print(form)
form1 = current.strftime(("%Y-%m-%d %H:%M:%S"))
print(form1)
form2 = current.strftime(("%m/%d/%Y"))
print(form2)
form3 = current.strftime(("%d,%m %d,%Y"))
print(form3)
form4 = current.strftime(("%d-%m-%Y %H:%M:%S %p"))
print(form4)
form5 = current.strftime("%a-%B-%d %H:%M:%S %p")
print(form5)
form6 = current.strftime("%A-%b_%d %H:%M:%S %Z %Y")
print(form6)
form7 = current.strftime("%d")
print(form7)
form8 = current.strftime("%H:%M:%S")
print(form8)
form9 = current.strftime("%B")
print(form9)
form10 = current.strftime("%Y")
print(form10)
