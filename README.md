# Dublin Property & Trees Price Analysis

This project analyses whether houses on streets with tall trees are more expensive than those with short trees.

## Installation  

1. Ensure you have Python 3.11.5 installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository or download the source code.
    - https://github.com/Cathal-McHale/dublin_trees_analysis
3. Install the required dependencies:
    'pip install -r requirements.txt'
    
## Running the Script

To run the analysis script, use the following command:

python -m tree_analysis.main

## Running the Tests

To run the unit tests, use the following command:

python -m unittest discover -s tests


## Project Structure

- `tree_analysis/`
  - `main.py`: Main script to run the analysis.
  - `data_loader.py`: Contains the `DataLoader` class for loading tree and property data.
  - `analyser.py`: Contains the `PriceAnalyser` class for analysing property prices.
- `tests/`
  - `test_analysis.py`: Unit tests for the `DataLoader` and `PriceAnalyser` classes.

## Data Files

- `dublin-trees.json`: JSON file containing tree data.
- `dublin-property.csv`: CSV file containing property data.

## Logging

The script uses Python's built-in logging module to log information and errors. Logs are printed to the console.

## Error Handling

The script includes error handling to log and raise exceptions if data loading or analysis fails.