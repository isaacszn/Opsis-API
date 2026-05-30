from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Get API key from .env file and configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Initialize the Gemini 1.5 Flash Model 
model = genai.GenerativeModel("gemini-2.5-flash")

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "Opsis back-end running!!"}

# Main endpoint that receives images and returns description
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    """
    Receives an image file, sends it to Gemini, gets description back
    """
    try:
        # Read the image file data into memory
        image_data = await file.read()

        # Create prompt
        prompt = "Describe this image to me, I don't know what it is. Be brief and make it  suit someone very curious. Maximum of one paragraph only, no much big grammar but also make it detailed and informative. Make it suitable for a novice. Make sure you begin the description with 'this appears to be' or 'this is' rather than 'this image...'."
        
        # Send image and prompt to Gemini
        response = model.generate_content([
            prompt,
            {
                "mime_type": file.content_type,
                "data": image_data
            }
        ])

        description = response.text

        print(description)

        return {
            "success": True,
            "description": description,
            "filename": file.filename
        }
    
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"success": False, "error": str(e)}
        )
