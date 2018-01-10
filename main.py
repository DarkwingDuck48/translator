import os
import os.path
import re

LANGYAGES = {
    "Python": {
        "extention": ".py",
        "module": "python"
    },
    "VBScript": {
        "extention": ".vbs",
        "module": "vbscript"
    },
    "JavaScript": {
        "extention": ".js",
        "module": "javascript"
    },
    "Java": {
        "extention": ".java",
        "module": "java"
    },
    "C#": {
        "extention": ".cs",
        "module": "csharp"
    }
}

# func for define code language by file extention
def defineLang(fileext):
    for k, v in LANGYAGES.items():
        if v["extention"] == fileext:
            return k, v["module"]

print(defineLang(".py"))