# schemas/pet_schema.py

pet_schema = {
    "type": "object",
    "required": ["id", "name", "status"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "status": {"type": "string"}
    }
}
