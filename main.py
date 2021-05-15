import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from base64 import b64decode

from pyrawprint import send_raw_data_to_printer

class PrintRequest(BaseModel):
    data: str
    printer_name: Optional[str] = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/print")
def send_to_printer(print_request: PrintRequest):
    decoded_data = b64decode(print_request.data)
    send_raw_data_to_printer(decoded_data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
