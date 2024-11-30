
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for simplicity in development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the model for user profile
class UserProfile(BaseModel):
    name: str
    email: str
    dob: str  # Date in YYYY-MM-DD format
    country_code: str
    phone_number: str

# Endpoint to receive and store user profile data
@app.post("/submit-profile/")
async def submit_profile(user_profile: UserProfile):
    # In a real app, you'd save this data to a database
    return {"message": "Profile submitted successfully!", "data": user_profile}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
