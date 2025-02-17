import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from pathlib import Path
from tree_analysis.data_loader import DataLoader
from tree_analysis.analyser import PriceAnalyser

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.trees_path = Path("test_trees.json")
        self.properties_path = Path("test_properties.csv")
        self.loader = DataLoader(self.trees_path, self.properties_path)

    @patch("builtins.open", new_callable=mock_open, 
           read_data='{"short":{"test":{"street":{"test street":5}}}}')
    def test_load_tree_data(self, mock_file):
        data = self.loader.load_tree_data()
        self.assertIn("short", data)
        mock_file.assert_called_once_with(self.trees_path)

    def test_load_property_data(self):
        mock_df = pd.DataFrame({
            "Street Name": [" Test Street "],
            "Price": ["€300,000.00"]
        })
        with patch("pandas.read_csv", return_value=mock_df):
            df = self.loader.load_property_data()
            self.assertEqual(df["Street Name"].iloc[0], "test street")
            self.assertEqual(df["Price"].iloc[0], 300000.00)

class TestPriceAnalyser(unittest.TestCase):
    def setUp(self):
        self.tree_data = {
            "short": {"road": {"oak": {"oak road": 5}}},
            "tall": {"avenue": {"pine": {"pine avenue": 15}}}
        }
        self.property_data = pd.DataFrame({
            "Street Name": ["oak road", "pine avenue"],
            "Price": [300000.0, 500000.0]
        })
        self.analyser = PriceAnalyser(self.tree_data, self.property_data)

    def test_extract_street_names(self):
        short_streets = self.analyser.extract_street_names("short")
        self.assertIn("oak road", short_streets)

    def test_compute_average_price(self):
        avg_price = self.analyser.compute_average_price({"oak road"})
        self.assertEqual(avg_price, 300000.0)

    def test_analyse(self):
        short_avg, tall_avg = self.analyser.analyse()
        self.assertEqual(short_avg, 300000.0)
        self.assertEqual(tall_avg, 500000.0)

if __name__ == "__main__":
    unittest.main()