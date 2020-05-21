#!/usr/bin/env python3

import sys, os, requests, json, re

"""
1) create directory with given name
2) create README.md file inside that directory
3) get room data via THM api
4) get the questions via THM api
5) parse these questions and create my prefered structure to take notes
"""

# check number of args
if len(sys.argv) < 2:
    print("Usage: setup.py [URL Extension] {Optional: Name of Directory}", file=sys.stderr)
    exit(code=1)

# Set up URL argument and optional dir arg
# room = URL : dirname = new directory name
room=sys.argv[1]
if len(sys.argv) > 2:
    dirname=sys.argv[2]
else:
    dirname=room

# First we check if dir exists, and if the data from THM is good
# don't do anything if dir exists
if os.path.isdir(dirname):
    print("Directory already exists! Exitting...", file=sys.stderr)
    exit(code=1)

thm = "https://tryhackme.com/api/"

# 3) get room data via THM api
resp = requests.get(thm + "room/" + room)
if resp.status_code != 200:
    print("Failed to get room data. Exitting...", file=sys.stderr)
    exit(1)
roomData = json.loads(resp.text)
success = roomData["success"]
if not success:
    print("THM gave an error. Exitting...", file=sys.stderr)

# 4) get the questions via THM api
resp = requests.get(thm + "tasks/" + room)
if resp.status_code != 200:
    print("Failed to get question data. Exitting...", file=sys.stderr)
    exit(1)

# 5) parse these questions and create my prefered structure to take notes
taskData = json.loads(resp.text)
success = taskData["success"]
if not success:
    print("THM gave an error. Exitting...", file=sys.stderr)


# We know all is good --> start making files and writing to them

# 1) create directory with given name
os.mkdir(dirname)

# 2) create README.md file inside that directory
readme = open(dirname + "/README.md", "w+")
title = roomData["title"]
tasks = taskData["data"]

readme.write(
"""# {}

```
export IP=
```


""".format(title)
)

cleanrn = re.compile('<.*?>')

# loop over all the tasks
for i, task in enumerate(tasks, start=1):
    readme.write("## Task {}: {}".format(i,task["taskTitle"]) + os.linesep)
    for question in task["questions"]:
        # remove html tags from question text
        questionText = re.sub(cleanrn, '', question["question"])
        readme.write("""**{}**
```

```

""".format(questionText.strip()))
        

