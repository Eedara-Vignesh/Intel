import json

def load_shipments(path="data/shipments.json"):
    """
    Loads and returns compressed shipment data
    """
    with open(path, "r") as file:
        data = json.load(file)
    return data