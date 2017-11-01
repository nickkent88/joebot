import pytest

import joebot.utilities.conversion as conv

@pytest.fixture
def json():
    return unicode('{"glossary": {"title": "example glossary", "GlossDiv": {"title": "S", "GlossList": {"GlossEntry": {"ID": "SGML", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"]}, "GlossSee": "markup"}}}}}')


@pytest.fixture
def yaml():
    return unicode("glossary:\n  title: example glossary\n  GlossDiv:\n    title: S\n    GlossList:\n      GlossEntry:\n        ID: SGML\n        SortAs: SGML\n        GlossTerm: Standard Generalized Markup Language\n        Acronym: SGML\n        Abbrev: ISO 8879:1986\n        GlossDef:\n          para: A meta-markup language, used to create markup languages such as DocBook.\n          GlossSeeAlso:\n          - GML\n          - XML\n        GlossSee: markup\n")
    

def test_json_to_yaml(json, yaml):
    assert conv.json_to_yaml(json) == yaml
