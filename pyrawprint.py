import os, sys
import win32print

def send_raw_data_to_printer(raw_data):
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
