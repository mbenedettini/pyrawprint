## Development

`uvicorn main:app --reload --port 8219`

## Build .exe
`pyinstaller -y --clean --additional-hooks-dir=extra-hooks main.py`
