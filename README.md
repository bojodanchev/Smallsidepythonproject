# Smallside Python Project

This tiny script calls the public CoinGecko API, stores the latest USD prices for Bitcoin and Ethereum in a pandas DataFrame, and writes the result to `data.csv`.

## Requirements

- Python 3.9 or newer
- `requests` and `pandas` Python packages (`pip install requests pandas`)

## Usage

```bash
python3 fetch_data.py
```

The script prints the fetched prices and saves them to `data.csv` in the current directory.

## Notes

- The timestamp column is generated in UTC. Swap to `datetime.now(datetime.UTC)` if you prefer timezone-aware values without deprecation warnings.
