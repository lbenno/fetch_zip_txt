import requests, zipfile, io

zip_file_url_1 = 'https://pastvtr.elections.nsw.gov.au/SG2301/LA/ballina/SG2301%20LA%20Pref%20Data%20Ballina.zip'

response_headers = {'Content-Type': 'application/x-zip-compressed', 
'Content-Disposition': 'attachment; filename="SG2301 LA Pref Data Ballina.zip"; filename*=UTF-8''SG2301%20LA%20Pref%20Data%20Ballina.zip', 'Cookie': 'visid_incap_638606=LiyVoAlsT0K8vxHuwLNGZEZVbmQAAAAAQUIPAAAAAADM3xePX85Ua7/Ug1Q5SwJS; ARRAffinity=f794eb23c938f00632e133dc73d8b506b2bb21302540b616f9572ec6441496ef; ARRAffinitySameSite=f794eb23c938f00632e133dc73d8b506b2bb21302540b616f9572ec6441496ef; nlbi_926237=jF73UUmNyAtJ6bih/iKhbQAAAADaWP3iVfdQnajXaVCNblQJ; visid_incap_926237=d3isaGwSR8Cc/f302AhGXYXgLmUAAAAAQUIPAAAAAAAW8eaLVbjKso5xA3pP+NfF; incap_ses_1342_926237=I1FXLKCY3AkCAjNPyr6fEongLmUAAAAAQ771XzmLGdCopMHk3qjPmQ==; _gcl_au=1.1.522088715.1697570956; _ga=GA1.1.347557298.1697570956; incap_ses_877_638606=1er1bFflWRtL9P64FLsrDP7gLmUAAAAA5DgrZR4KFOKc+4tJn24YcA==; _ga_2JDS9B9KL5=GS1.1.1697570955.1.1.1697571070.22.0.0; _ga_QPQKP6JF1H=GS1.1.1697570955.1.1.1697571070.0.0.0; incap_ses_1309_638606=1duzYna7Swzz4hdRMYIqEtBoMWUAAAAA3Q/9kUcQwO+wAbQhP43OEA==; incap_ses_1291_926237=N6lfJOrM4SuLos7HmI7qETP6M2UAAAAASDZiN5AJFJyFmqPfac5sJw==; incap_ses_536_638606=I8+jX3WsBVC1Ck1vMkJwB6kgNGUAAAAATU67oIa1XEdH4PdF2qu/Kg=='}

zip2 = requests.get(zip_file_url_1, headers=response_headers, allow_redirects=True, stream=True)

print(zip2.ok)

check = zipfile.is_zipfile(io.BytesIO(zip2.content))
while check:
    z = zipfile.ZipFile(io.BytesIO(zip2.content))
    z.extractall()
else:
    print('false')