import io
from converter.csvformat import Csv
from nose.tools import assert_list_equal

SAMPLE_DATA = """id,first_name,last_name
1,Fanechka,Spare
2,Jozef,Sucre"""

SAMPLE_PARSED = [
        {'id': '1', 'first_name': 'Fanechka', 'last_name': 'Spare'},
        {'id': '2', 'first_name': 'Jozef', 'last_name': 'Sucre'},
    
    ]

def test_read():
    f = io.StringIO(SAMPLE_DATA)
    format = Csv(f)
    data = format.read()
    assert_list_equal(data, SAMPLE_PARSED)
    

def test_write():
    f = io.StringIO()
    format = Csv(f)
    format.write(SAMPLE_PARSED)
    f.seek(0)
    assert_list_equal(format.read(), SAMPLE_PARSED)
