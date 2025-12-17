from fastapi import FastAPI
import os

# =========================
# DEPENDENCY GUARD (FAIL FAST)
# =========================
REQUIRED_MODULES = ["httpx"]
for module in REQUIRED_MODULES:
    try:
        __import__(module)
    except ImportError as e:
        raise RuntimeError(
            f"Missing required dependency: {module}. "
            f"Ensure it is listed in requirements.txt"
        ) from e

import httpx  # guaranteed present if execution continues

# =========================
# APP INITIALIZATION
# =========================
app = FastAPI(
    title="Infinity Orchestrator",
    version="1.0.0",
    description="Central orchestration service for Infinity XOS"
)

# =========================
# HEALTH CHECKS (MANDATORY)
# =========================
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    return {"ready": True}

# =========================
# ROOT
# =========================
@app.get("/")
def root():
    return {
        "service": "orchestrator",
        "status": "running"
    }
