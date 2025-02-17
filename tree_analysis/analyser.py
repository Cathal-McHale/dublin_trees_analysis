from typing import Dict, Optional, Set, Tuple
import pandas as pd


class PriceAnalyser:
    def __init__(self, tree_data: Dict, property_data: pd.DataFrame):
        self.tree_data = tree_data
        self.property_data = property_data

    def extract_street_names(self, category: str) -> Set[str]:
        streets = set()
        
        def recursive_extract(data: Dict) -> None:
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, dict):
                        recursive_extract(value)
                    elif isinstance(value, (int, float)):
                        streets.add(key.lower())

        recursive_extract(self.tree_data.get(category, {}))
        return streets if streets else set()


    def compute_average_price(self, street_set: Set[str]) -> Optional[float]:
        prices = self.property_data[
            self.property_data["Street Name"].isin(street_set)
        ]["Price"]
        return prices.mean() if not prices.empty else 0.0

    def analyse(self) -> Tuple[Optional[float], Optional[float]]:
        short_streets = self.extract_street_names("short")
        tall_streets = self.extract_street_names("tall")
        
        return (
            self.compute_average_price(short_streets),
            self.compute_average_price(tall_streets)
        )