from nose.tools import assert_list_equal

from converter.format import Format
import io
import json

SAMPLE_JSON = """[{"id":1,"first_name":"Hartley","last_name":"Klicher"},
    {"id":2,"first_name":"Shelby","last_name":"Brodest"},
    {"id":3,"first_name":"Marmaduke","last_name":"MacCarter"},
    {"id":4,"first_name":"Terra","last_name":"Trudgeon"},
    {"id":5,"first_name":"Wałker","last_name":"Charles"}]"""

SAMPLE_PY = [{"id":1,"first_name":"Hartley","last_name":"Klicher"},
    {"id":2,"first_name":"Shelby","last_name":"Brodest"},
    {"id":3,"first_name":"Marmaduke","last_name":"MacCarter"},
    {"id":4,"first_name":"Terra","last_name":"Trudgeon"},
    {"id":5,"first_name":"Wałker","last_name":"Charles"}]


class JsonFormat(Format):

    def read(self):
        read = json.load(self.file)
        return read

    def write(self, data):
        write = json.dump(data, self.file)


def test_read():
    f = io.StringIO(SAMPLE_JSON)
    fmt = JsonFormat(f)
    assert_list_equal(fmt.read(), SAMPLE_PY)


def test_write():
    f = io.StringIO()
    fmt = JsonFormat(f)
    fmt.write(SAMPLE_PY)
    f.seek(0)
    assert_list_equal(fmt.read(), SAMPLE_PY)




