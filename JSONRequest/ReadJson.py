import json
def ReadJson(fname):
    with open(fname) as feedsjson:
        feeds = json.load(feedsjson)
    return feeds