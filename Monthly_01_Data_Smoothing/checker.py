
import json
import os
import matplotlib.pyplot as plt

files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
if "__pycache__" in files:
    files.remove("__pycache__")

if len(files) < 3 or len(files) > 4:
    print("please make sure you have 3 files total in the folder:\n\n- the solution you're checking in a python file\n- this program\n- the provided data list in a json file")
    quit()

for f in files:
    if f.endswith(".json"):
        with open(f) as j:
            data = json.load(j)
    if f.endswith(".py") and f != os.path.basename(__file__):
        solution = __import__(f.split(".")[0])

try:
    y = solution.smooth(data)
except:
    print("make sure you have the correct files in the folder:\n\n- the solution you're checking in a python file\n- this program\n- the provided data list in a json file")
    quit()

x = []
for i in range(len(y)):
    x.append(i)

plt.plot(x, y)
plt.show()
