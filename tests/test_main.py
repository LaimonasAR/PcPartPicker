import unittest
from unittest.mock import patch
from main import Part

class TestPart(unittest.TestCase):
    @patch("main.app.find_part")
    def test_get_all_parts(self, mock_find_part):
        # Mock the find_part function to return some sample data
        mock_find_part.return_value = [
            {
                "part_type": "CPU",
                "name": "Intel Core i7",
                "cores": 8,
            },
        ]

        part = Part("CPU")
        result = part.get_all_parts()

        self.assertEqual(
            result,
            "CPU {'part_type': 'CPU', 'name': 'Intel Core i7', 'cores': 8}",
        )

    @patch("main.app.find_part")
    def test_get_property(self, mock_find_part):
        mock_find_part.return_value = [
            {
                "part_type": "CPU",
                "name": "Intel Core i7",
                "cores": 8,
            },
        ]
        part = Part(part_type="CPU", property="cores")
        result = part.get_property()

        self.assertEqual(
            result,
            "CPU Intel Core i7, 8 cores",
        )

    @patch("main.app.find_part")
    def test_get_all_properties(self, mock_find_part):
        mock_find_part.return_value = [
            {
                "part_type": "CPU",
                "name": "Intel Core i7",
                "cores": 8,
            },
            {
                "part_type": "CPU",
                "name": "AMD Ryzen 5",
                "cores": 16,
            },
        ]
        part = Part(part_type="CPU")
        result = part.get_all_properties()

        self.assertEqual(
            result,
            ["part_type", "name", "cores"],
        )


if __name__ == "__main__":
    unittest.main()
