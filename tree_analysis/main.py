import logging
from pathlib import Path
from tree_analysis.data_loader import DataLoader
from tree_analysis.analyser import PriceAnalyser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        data_loader = DataLoader(
            Path("dublin-trees.json"),
            Path("dublin-property.csv")
        )
        
        tree_data = data_loader.load_tree_data()
        property_data = data_loader.load_property_data()
        
        analyser = PriceAnalyser(tree_data, property_data)
        short_avg, tall_avg = analyser.analyse()
        
        logger.info(f"Average property price on short tree streets: €{short_avg:,.2f}")
        logger.info(f"Average property price on tall tree streets: €{tall_avg:,.2f}")

        
    except Exception as e:
        # log the error and raise it with traceback
        logger.error(f"Analysis failed: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
