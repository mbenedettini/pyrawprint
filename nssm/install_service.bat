nssm install "Driza Raw Printer" "main.exe"
nssm set "Driza Raw Printer" AppDirectory %CD%
nssm start "Driza Raw Printer"
del "%~f0"
