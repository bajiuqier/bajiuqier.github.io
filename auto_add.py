# coding=utf-8                                                                                                                                              
import os
from pathlib import Path

home_dir = Path(__file__).parent

htmlbegin = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bajiuqier</title>
</head>
<!-- <body style="background:#E0EEE8"> -->
<body>
'''

htmlend = '''
</body>
</html>
'''
files = os.listdir(str(home_dir / 'docs.html'))
lsstr = ''
for f in files:
    if (f!="auto_add.py" and f!="index.html"):
        htmlbegin += f'''<h5><a href="./docs.html/{f}" style="text-decoration: none" target="_blank">{f}</a></h5>\n'''

html = htmlbegin + htmlend


with open(str(home_dir / 'index.html'), 'w') as f:
    f.writelines(html)