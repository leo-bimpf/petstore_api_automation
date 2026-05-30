pet_schema = {
    "type": "object",
    "required": ["id", "name", "photoUrls", "status"],
    "properties": {
        "id": {"type": "integer"},

        "category": {
            "type": "object",
            "required": ["id", "name"],
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}
            }
        },

        "name": {"type": "string"},

        "photoUrls": {
            "type": "array",
            "items": {"type": "string"}
        },

        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "name"],
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                }
            }
        },

        "status": {"type": "string"}
    }
}