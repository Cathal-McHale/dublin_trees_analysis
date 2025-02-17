from pathlib import Path
import json
import pandas as pd
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class DataLoader:
    """
    DataLoader is responsible for loading tree and property data from specified file paths.
    """
    def __init__(self, trees_path: Path, properties_path: Path):
        self.trees_path = trees_path
        self.properties_path = properties_path

    def load_tree_data(self) -> Dict:
        """
        Load tree data from a JSON file.
        
        Returns:
            Dict: The loaded tree data.
        """
        try:
            with open(self.trees_path) as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logger.error(f"Failed to load tree data: {e}")
            raise

    def load_property_data(self) -> pd.DataFrame:
        """
        Load property data from a CSV file and preprocess it.
        
        Returns:
            pd.DataFrame: The preprocessed property data.
        """
        try:
            df = pd.read_csv(self.properties_path, encoding='ISO-8859-1')
            df.columns = df.columns.str.strip()
            df["Street Name"] = df["Street Name"].str.strip().str.lower()
            df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)
            return df
        except Exception as e:
            logger.error(f"Failed to load property data: {e}")
            raise