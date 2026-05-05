
import json
import pandas as pd
import os

class BaseStorage:
    def save(self, data, filename="data.json", directory=None):
        # ... keep original ...
        try:
            # If directory is specified, create the full path
            if directory:
                # Ensure the directory exists
                os.makedirs(directory, exist_ok=True)
                # Create full path for the file
                filepath = os.path.join(directory, filename)
            else:
                filepath = filename
                
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Data saved successfully to {filepath}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def save_to_csv(self, data, filename="data.csv", directory=None):
        try:
            df = pd.DataFrame(data)
            # If directory is specified, create the full path
            if directory:
                # Ensure the directory exists
                os.makedirs(directory, exist_ok=True)
                filepath = os.path.join(directory, filename)
            else:
                filepath = filename
            df.to_csv(filepath, index=False)
            print(f"Data saved successfully to {filepath}")
        except Exception as e:
            print(f"Error saving data to CSV: {e}")

    def save_to_xlsx(self, data, filename="data.xlsx", directory=None):
        try:
            df = pd.DataFrame(data)
            # If directory is specified, create the full path
            if directory:
                # Ensure the directory exists
                os.makedirs(directory, exist_ok=True)
                filepath = os.path.join(directory, filename)
            else:
                filepath = filename
            df.to_excel(filepath, index=False)
            print(f"Data saved successfully to {filepath}")
        except Exception as e:
            print(f"Error saving data to XLSX: {e}")

    def load(self, filename="data.json", directory=None):
        # ... keep original ...
        try:
            # If directory is specified, create the full path
            if directory:
                filepath = os.path.join(directory, filename)
            else:
                filepath = filename
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"Data loaded successfully from {filepath}")
            return data
        except FileNotFoundError:
            filepath = filename if not directory else os.path.join(directory, filename)
            print(f"File {filepath} not found. Returning empty list.")
            return []
        except Exception as e:
            print(f"Error loading data: {e}")
            return []
