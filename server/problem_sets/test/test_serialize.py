from unittest import TestCase

from problem_sets import Widget, TextWidgetOptions
from problem_sets.serialization import serialize_recursive, Serializable


class TestSerialize(TestCase):
    mock_widget = Widget(TextWidgetOptions("test"))
    mock_widget_serialized = mock_widget.serialize()

    class ExampleSerializable(Serializable):

        def __init__(self, number: int, string: str):
            self.number = number
            self.string = string

        def serialize(self) -> dict:
            return {
                "number": self.number,
                "string": self.string
            }

    mock_data = {
        "widget": mock_widget,
        "list": [ExampleSerializable(1, "test")] * 5,
        "test": 5
    }

    mock_expected_data = {
        "widget": mock_widget_serialized,
        "list": [ExampleSerializable(1, "test").serialize()] * 5,
        "test": 5
    }

    def test_serialize_recursive(self):
        # print(self.mock_expected_data)
        serialized = serialize_recursive(self.mock_data)
        assert serialized == self.mock_expected_data
