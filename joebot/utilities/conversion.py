import collections
import json

import pyaml

def json_to_yaml(json_string):
    loaded_json = json.loads(json_string, object_pairs_hook=collections.OrderedDict)
    return pyaml.dumps(loaded_json, safe=True)
