import requests
import os
import json

url = 'https://www.prepostseo.com/apis/checkPlag'
comptext = 'This is a coded text'
myobj = {'key': '10fe417f49dd780d501d78ace5336ccf' , 'data': comptext}

x = requests.post(url, data = myobj)
y = json.loads(x.text)
if y["plagPercent"]<40 :
    print(y)
else :
    os.system('python pycode_similar/pycode_similar.py pycode_similar/tests/original_version.py pycode_similar/tests/false_doc.py')