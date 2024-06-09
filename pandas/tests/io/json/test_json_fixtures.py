import json

from pandas import (
    DataFrame,
    read_json,
)
import pandas._testing as tm


def test_read_json_fixtures():
    json_fixtures = json.dumps(
        [
            {"model": "app.model", "pk": 1, "fields": {"name": "Tom", "age": 5}},
            {"model": "app.model", "pk": 2, "fields": {"name": "Jerry", "age": 3}},
            {"model": "app.model", "pk": 3, "fields": {"name": "Spike", "age": 2}},
        ]
    )

    expected_df = DataFrame(
        {
            "model": ["app.model", "app.model", "app.model"],
            "pk": [1, 2, 3],
            "name": ["Tom", "Jerry", "Spike"],
            "age": [5, 3, 2],
        }
    )

    result_df = read_json(json_fixtures, orient="fixtures")

    tm.assert_frame_equal(result_df, expected_df)
