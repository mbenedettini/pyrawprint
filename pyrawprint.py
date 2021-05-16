import os, sys
import win32print

def send_raw_data_to_printer(raw_data, printer_name):
    print(f">>> arg printer name: {printer_name}")
    if not printer_name:
        printer_name = win32print.GetDefaultPrinter()
    print(f">>> Using printer {printer_name}")

    hPrinter = win32print.OpenPrinter(printer_name)
    try:
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, "RAW"))
        try:
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, raw_data)
            win32print.EndPagePrinter(hPrinter)
        except:
            e = sys.exc_info()[0]
            print(e)
        finally:
            win32print.EndDocPrinter(hPrinter)
    except:
        e = sys.exc_info()[0]
        print(e)
    finally:
        win32print.ClosePrinter(hPrinter)


def get_printers():
    return [
        p[2] for p in
        win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
    ]
