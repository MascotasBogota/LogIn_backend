from datetime import datetime
from bson import ObjectId
def serialize_response(response):
    print("serializin")
    if hasattr(response, "to_mongo"):
        doc = response.to_mongo().to_dict()
    else:
        doc = dict(response)
    
    print(doc)

    # Reemplazar _id por id
    doc["id"] = str(doc.pop("_id"))

    def convert(value):
        if isinstance(value, ObjectId):
            return str(value)
        elif isinstance(value, datetime):
            return value.isoformat()
        elif isinstance(value, list):
            return [convert(item) for item in value]
        elif isinstance(value, dict):
            return {k: convert(v) for k, v in value.items()}
        else:
            return value

    return {k: convert(v) for k, v in doc.items()}