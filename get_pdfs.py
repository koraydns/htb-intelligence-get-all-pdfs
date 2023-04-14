from datetime import date, timedelta
import requests
import urllib.request

"""
Get All Days Between Given Interval
"""
def get_all_dates(start_date, end_date):
    dates = []
    delta = end_date - start_date
    for i in range(delta.days + 1):
        date = start_date + timedelta(days=i)
        dates.append(date)
    return dates

"""
Detect PDFs on Intelligence Server
"""
def get_pdfs(dates):
    pdfs = []
    for dt in dates:
        dt_format = dt.strftime("%Y-%m-%d-upload.pdf")
        pdf_req = requests.get('http://10.10.10.248/documents/'+dt_format)
        if pdf_req.status_code == 200:
            pdfs.append(dt_format)
            print('http://10.10.10.248/documents/'+dt_format)
    return pdfs

"""
Download PDFs on Intelligence Server
"""
def downlad_pdfs(pdfs):
    for pdf in pdfs:
        with urllib.request.urlopen("http://10.10.10.248/documents/"+pdf) as response, open(pdf, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

"""
MAIN
"""
start_date = date(2020, 1, 1) 
end_date = date(2020, 12, 31)   
dates = get_all_dates(start_date, end_date) 
pdfs = get_pdfs(dates)
print("Downloading detected pdfs...")
downlad_pdfs(pdfs)
