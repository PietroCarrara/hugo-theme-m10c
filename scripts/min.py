from xmlformatter import Formatter
import json
import sys
import os
import re

formatter = Formatter(compress=True)
openSvg = re.compile(r"^<svg [^<]*")
closeSvg = re.compile(r"</svg>")

res = {}

for fname in sys.argv[1:]:
  with open(fname, 'r') as f:
    xml = formatter.format_string(f.read()).decode('utf-8')
    xml = re.sub(openSvg, '', xml)
    xml = re.sub(closeSvg, '', xml)

    name = os.path.splitext(os.path.basename(fname))[0]
    res[name] = xml

print(json.dumps(res))