import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from base64 import b64decode

from pyrawprint import send_raw_data_to_printer
from pyrawprint import get_printers

PORT=8219

class PrintRequest(BaseModel):
    data: str
    printer_name: Optional[str] = None

class PrintersResponse(BaseModel):
    printers: List[str] = []

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
    send_raw_data_to_printer(
        decoded_data, print_request.printer_name
    )

@app.get(
    "/printers",
    response_model=PrintersResponse
)
def printers():
    printers = get_printers()
    printers_response = PrintersResponse()
    printers_response.printers = printers
    return printers_response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8219)
