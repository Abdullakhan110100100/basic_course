from fastapi import HTTPException

def raise_not_found(resource: str, id: str) -> None:
    raise HTTPException(status_code=404, detail=f"{resource} {id} not found")