import re
def slugify(t):
    return re.sub(r"[^a-z0-9]+","-",t.lower())
