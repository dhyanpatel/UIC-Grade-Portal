import pdftables_api

def create_xlsx(pdf_path ,api_key):
    try:
        c = pdftables_api.Client(api_key)
        c.xlsx(pdf_path, 'output')
    except FileNotFoundError:
        print("PDF Path is Invalid")
    except pdftables_api.pdftables_api.APIException:
        print("API Key was Invalid")