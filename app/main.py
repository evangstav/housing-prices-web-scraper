from fastapi import FastAPI
from app import scraper, dashboard

app = FastAPI()

app.include_router(scraper.router)
app.include_router(dashboard.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
