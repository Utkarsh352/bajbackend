from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#  Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/bfhl")
async def status_code():
    return {"operation_code": 1}

@app.post("/bfhl")
async def process_data(request: Request):
    try:
        body = await request.json()
        print("Received JSON:", body) 

        if "data" not in body or not isinstance(body["data"], list):
            raise HTTPException(status_code=400, detail="Invalid JSON format")

        data_list = body["data"]
        numbers = [item for item in data_list if item.isdigit()]
        alphabets = [item for item in data_list if item.isalpha()]
        highest_alphabet = [max(alphabets, key=str.upper)] if alphabets else []

        return {
            "is_success": True,
            "user_id": "utkarsh_mahajan_28082004",
            "email": "22bda70022@cuchd.in",
            "roll_number": "22BDA70022",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }

    except Exception as e:
        print("Error:", str(e))  
        raise HTTPException(status_code=500, detail=str(e))


import os
import sys
if os.getenv("VERCEL"):
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

handler = app  
