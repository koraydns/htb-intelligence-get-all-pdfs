# htb-intelligence-get-all-pdfs
This Python script downloads PDF files on the Hack The Box Intelligence machine to your local. Filenames follow the structure of YYYY-MM-DD-upload.pdf. The script sends requests to the server for all PDF files containing any date within the date range specified on lines 43 and 44. If the response code is 200, it downloads the PDF file to which directory the script is run.

Before running the script IP address on line 5 should be edited . Optionally, the dates on lines 43 and 44 can be changed.

To access machine walkthrough: https://penetratechacademy.com/htb-intelligence-walkthrough/
