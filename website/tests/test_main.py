from fastapi.testclient import TestClient

from app.main import app
from tests.utils import get_json_input_files, get_json_output_files

client = TestClient(app)


def test_post_main():
    input_json = dict(sorted(get_json_input_files().items()))
    output_json = dict(sorted(get_json_output_files().items()))
    test_list = zip(input_json.values(), output_json.values())
    for injson, outjson in test_list:
        response = client.post(app.url_path_for("stocks"), json=injson)
        assert response.json() == outjson
        assert response.status_code == 200
