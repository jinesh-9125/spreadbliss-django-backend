def validator(provided_fields, required_fields):
    """
    Validates the request object to ensure that all the required fields are present.
    """
    missing = []
    if required_fields == None:
        return {"success": True}
    for required_field in required_fields:
        if required_field not in provided_fields:
            missing.append(required_field)
    if missing:
        return {
            "error": f"Missing required fields: {', '.join(missing)}",
            "success": False,
        }
    return {"success": True}
