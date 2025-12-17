from fastapi import APIRouter

router = APIRouter(prefix="/github", tags=["github"])

@router.get("/repos")
def list_repos():
    return {"repos": ["core", "ai-agent", "infinity-ui"]}

@router.post("/commit")
def commit_change(payload: dict):
    return {"status": "committed", "details": payload}

def register_plugin(app):
    app.include_router(router)
