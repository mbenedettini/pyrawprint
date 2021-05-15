## Development

`uvicorn main:app --reload`

## Build .exe
`pyinstaller -y --clean --additional-hooks-dir=extra-hooks main.py`
