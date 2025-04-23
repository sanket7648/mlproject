from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import auth, recommendations, feedback, search
from config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
app.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
app.include_router(search.router, prefix="/search", tags=["search"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM Product Recommendation System"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)