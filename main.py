from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)


class RequestData(BaseModel):
    data: List[str]

@app.get("/bfhl")
async def status_code():
    return {"operation_code": 1}

@app.post("/bfhl")
async def process_data(request_data: RequestData):
    try:
        data_list = request_data.data

        # Separate numbers and alphabets
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
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
