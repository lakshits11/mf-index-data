#!/usr/bin/env python3
"""
Single Index Fetcher
Fetch data for a specific Nifty index with automatic cookie handling.
"""

import sys
import json
from automated_index_fetcher import NiftyIndexFetcher

def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_single_index.py <INDEX_NAME>")
        print("Example: python fetch_single_index.py 'NIFTY 50'")
        return
    
    index_name = sys.argv[1]
    
    print(f"🚀 Fetching data for: {index_name}")
    print("=" * 50)
    
    fetcher = NiftyIndexFetcher()
    
    # Get fresh cookies
    if not fetcher.get_fresh_cookies():
        print("Failed to get cookies. Exiting.")
        return
    
    # Load mapping to get trading name
    index_mapping = fetcher.load_index_mapping()
    trading_name = index_mapping.get(index_name.upper(), index_name)
    
    if trading_name != index_name:
        print(f"Using trading name: {trading_name}")
    
    # Fetch the data
    data = fetcher.fetch_index_data(trading_name)
    
    if data:
        if fetcher.save_index_data(index_name, data):
            print(f"✅ Successfully fetched and saved data for {index_name}")
        else:
            print(f"❌ Failed to save data for {index_name}")
    else:
        print(f"❌ Failed to fetch data for {index_name}")

if __name__ == "__main__":
    main() 