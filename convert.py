#!/usr/bin/env python

SRCDIR = "/Users/nfunnell/junk/12factor/content/"

locale = "de"
localelist = [
    "de",
    "es",
    "fr",
    "it",
    "ja",
    "ko",
    "pt_br",
    "ru",
    "zh_cn"
]

LEKDIR = "/Users/nfunnell/junk/12factor-lektor/content/"

src2lek = [
    {"lek": "01-codebase", "src": "codebase.md", "num": 1},
    {"lek": "02-dependencies", "src": "dependencies.md", "num": 2},
    {"lek": "03-config", "src": "config.md", "num": 3},
    {"lek": "04-backing-services", "src": "backing-services.md", "num": 4},
    {"lek": "05-build-release-run", "src": "build-release-run.md", "num": 5},
    {"lek": "06-processes", "src": "processes.md", "num": 6},
    {"lek": "07-port-binding", "src": "port-binding.md", "num": 7},
    {"lek": "08-concurrency", "src": "concurrency.md", "num": 8},
    {"lek": "09-disposability", "src": "disposability.md", "num": 9},
    {"lek": "10-dev-prod-parity", "src": "dev-prod-parity.md", "num": 10},
    {"lek": "11-logs", "src": "logs.md", "num": 11},
    {"lek": "12-admin-processes", "src": "admin-processes.md", "num": 12},
    {"lek": "root", "src": "background.md", "num": 0},
    {"lek": "root", "src": "intro.md", "num": 0}
]

template = """
title: {title}
---
subtitle: {subtitle}
---
factor_number: {num}
---
body:

{body}
"""

def getFileContents(name):
    with open(name, 'r') as fh:
        return fh.read()

def processFile(name, num):
    contents = getFileContents(name)
    title = ""
    subtitle = ""
    body = []
    for line in contents.split("\n"):
        if line.startswith("### "):
            subtitle = line.split("### ")[1].strip()
        elif "### " in line:
            subtitle = line.split("### ")[1].strip()
        elif line.startswith("## "):
            title = line.split("## ")[1].strip()
        elif "## " in line:
            title = line.split("## ")[1].strip()
        else:
            body.append(line)
    return {
        "title": title,
        "subtitle": subtitle,
        "num": num,
        "body": "\n".join(body)
    }

def buildLektorFile(data):
    return template.format(**data)

def writeFile(name, contents):
    with open(name, "w") as fh:
        fh.write(contents)

for locale in localelist:
    for row in src2lek:
        if row['num'] > 0:
            filename = SRCDIR + locale + "/" + row['src']
            data = processFile(filename, row['num'])
            newfile = buildLektorFile(data)
            newfilename = LEKDIR + row['lek'] + "/contents+" + locale + ".lr"
            writeFile(newfilename, newfile)
            print "wrote: " + newfilename
