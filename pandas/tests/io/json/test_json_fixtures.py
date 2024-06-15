import io
import json

from pandas import (
    DataFrame,
    read_json,
)
import pandas._testing as tm


def test_read_json_fixtures():
    json_fixtures = [
            {"model": "app.model", "pk": 1, "fields": {"name": "Tom", "age": 5}},
            {"model": "app.model", "pk": 2, "fields": {"name": "Jerry", "age": 3}},
            {"model": "app.model", "pk": 3, "fields": {"name": "Spike", "age": 2}},
        ]

    str_fixtures = json.dumps(json_fixtures)
    bytes_fixtures = io.BytesIO(str_fixtures.encode())

    expected_df = DataFrame(
        {
            "model": ["app.model", "app.model", "app.model"],
            "pk": [1, 2, 3],
            "name": ["Tom", "Jerry", "Spike"],
            "age": [5, 3, 2],
        }
    )

    result_df = read_json(bytes_fixtures, orient="fixtures")

    tm.assert_frame_equal(result_df, expected_df)
