from typing import Dict, Optional, Set, Tuple
import pandas as pd

class PriceAnalyser:
    """
    PriceAnalyser is responsible for analysing property prices based on tree data.
    """
    def __init__(self, tree_data: Dict, property_data: pd.DataFrame):
        self.tree_data = tree_data
        self.property_data = property_data

    def extract_street_names(self, category: str) -> Set[str]:
        """
        Extract street names from the tree data for a given category.
        
        Args:
            category (str): The category of trees (e.g., "short", "tall").
        
        Returns:
            Set[str]: A set of street names.
        """
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
        """
        Compute the average property price for a set of street names.
        
        Args:
            street_set (Set[str]): A set of street names.
        
        Returns:
            Optional[float]: The average property price, or 0.0 if no prices are found.
        """
        prices = self.property_data[
            self.property_data["Street Name"].isin(street_set)
        ]["Price"]
        return prices.mean() if not prices.empty else 0.0

    def analyse(self) -> Tuple[Optional[float], Optional[float]]:
        """
        Analye the average property prices for streets with short and tall trees.
        
        Returns:
            Tuple[Optional[float], Optional[float]]: The average prices for short and tall tree streets.
        """
        short_streets = self.extract_street_names("short")
        tall_streets = self.extract_street_names("tall")
        
        return (
            self.compute_average_price(short_streets),
            self.compute_average_price(tall_streets)
        )