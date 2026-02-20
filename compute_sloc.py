"""Compute SLOC (source lines of code) for .py and .js files
Excludes blank lines and comment lines (single-line and block comments).
Writes results to sloc_report.json and prints summary.
"""
import os
import json

root = os.path.dirname(__file__)
report = {}

def count_python(path):
    sloc = 0
    in_block = False
    triple_starts = ("'''", '"""')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            # handle triple-quote blocks
            if not in_block:
                for t in triple_starts:
                    if line.startswith(t):
                        # if ends on same line
                        if line.count(t) >= 2 and len(line) > len(t):
                            # single-line docstring/comment -> skip
                            line = ''
                        else:
                            in_block = True
                            line = ''
                        break
            else:
                if any(t in line for t in triple_starts):
                    in_block = False
                continue
            if not line:
                continue
            if line.startswith('#'):
                continue
            # remove inline comments after code (naive)
            if '#' in line:
                # keep code before #
                code_part = line.split('#',1)[0].strip()
                if code_part:
                    sloc += 1
                continue
            sloc += 1
    return sloc


def count_js(path):
    sloc = 0
    in_block = False
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if not in_block:
                if line.startswith('/*'):
                    in_block = True
                    # check end on same line
                    if '*/' in line and line.find('*/') > line.find('/*'):
                        in_block = False
                    continue
                if line.startswith('//'):
                    continue
                # remove inline //
                if '//' in line:
                    code_part = line.split('//',1)[0].strip()
                    if code_part:
                        sloc += 1
                    continue
                sloc += 1
            else:
                if '*/' in line:
                    in_block = False
                continue
    return sloc

py_files = []
js_files = []
for dirpath, dirnames, filenames in os.walk(root):
    # skip __pycache__
    if '__pycache__' in dirpath:
        continue
    for fn in filenames:
        if fn.endswith('.py'):
            py_files.append(os.path.join(dirpath, fn))
        elif fn.endswith('.js'):
            js_files.append(os.path.join(dirpath, fn))

report['files'] = []
py_total = 0
for p in sorted(py_files):
    sl = count_python(p)
    report['files'].append({'path': os.path.relpath(p, root), 'lang':'py', 'sloc': sl})
    py_total += sl

js_total = 0
for p in sorted(js_files):
    sl = count_js(p)
    report['files'].append({'path': os.path.relpath(p, root), 'lang':'js', 'sloc': sl})
    js_total += sl

report['summary'] = {'py_sloc': py_total, 'js_sloc': js_total, 'total_sloc': py_total + js_total}

out = os.path.join(root, 'sloc_report.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2)

print('SLOC report written to', out)
print('Python SLOC:', py_total)
print('JS SLOC:', js_total)
print('Total SLOC:', report['summary']['total_sloc'])
