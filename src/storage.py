
import json

class BaseStorage:
    def save(self, data, filename="data.json"):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Data saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load(self, filename="data.json"):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"Data loaded successfully from {filename}")
            return data
        except FileNotFoundError:
            print(f"File {filename} not found. Returning empty list.")
            return []
        except Exception as e:
            print(f"Error loading data: {e}")
            return []
