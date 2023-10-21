import requests, zipfile, io

zip_file_url_1 = 'https://pastvtr.elections.nsw.gov.au/SG2301/LA/ballina/SG2301%20LA%20Pref%20Data%20Ballina.zip'

response_headers = {'Content-Type': 'application/x-zip-compressed', 
'Content-Disposition': 'attachment; filename="SG2301 LA Pref Data Ballina.zip"; filename*=UTF-8''SG2301%20LA%20Pref%20Data%20Ballina.zip', 'Cookie': 'various cookies'}

zip2 = requests.get(zip_file_url_1, headers=response_headers, allow_redirects=True, stream=True)

print(zip2.ok)

check = zipfile.is_zipfile(io.BytesIO(zip2.content))
while check:
    z = zipfile.ZipFile(io.BytesIO(zip2.content))
    z.extractall()
else:
    print('false')
