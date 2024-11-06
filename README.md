# pyrawprint

Http server intended for Windows that can interact with local printers, return a list of them and accept a print payload that is then sent to the printer, all using `win32print`.

My personal use case was allowing JavaScript code on browsers on a local network to send print requests to a thermal printer connected to a specific computer.

Includes the necessary files to create a Windows service for it using [NSSM](https://nssm.cc/) and an installer using [Inno Setup](https://jrsoftware.org/isinfo.php).

## Development

`uvicorn main:app --reload --port 8219`

## Build .exe
`pyinstaller -y --clean --additional-hooks-dir=extra-hooks main.py`
