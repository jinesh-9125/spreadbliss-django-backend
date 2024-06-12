def success_response(data, message="Success", status=200):
    return {"data": data, "message": message, "success": True, "status": status}


def error_response(message="Error", status=400):
    return {"error": message, "status": status, "success": False}
    