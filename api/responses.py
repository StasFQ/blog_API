

def api_response(result: dict = None, description: str = "", status_code: int = 200):
    return {"ok": True, "description": description, "result": result}, status_code


def api_abort(status_code: int = 400, description: str = ""):
    return {
        "ok": False,
        "description": description,
        "error_code": status_code,
    }, status_code
