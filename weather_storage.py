from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "tranquil-lotus-368022",
  "private_key_id": "288664fb37839552b19418add575c0703c6ac3d7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQmHIUJW/Hn/TK\nojQNT7opRhLtfn63ju7vjDL/vw1qq0JAW+jBZtL9pUf9CMuScf9ptZokYLIXLheE\nWJ6tYsEjeGxVN9u5a+AmvlMSrYx1p14QAA5yYUid21Z4v0H1c+dMwS0q1lQAb1o2\nYJThGiHRqeiL5Z6JkZZCcKN3zbFnG2WJmWBvWWdkXGwjJH37QS6BB39Qt8RdkOCB\nl9z3Ryjgn5urV9FzxVtV87Snm4agt3fDMJ2aTXnUps/RNysyds1Ml4zywxxPQ0PI\nwVdFerS9Qm3VhDHWwYRjKQqLHSU0FDmGMfCE+BsmVizLk86kaLf8uneAtDuJ4ZCv\nwiCVF3Q3AgMBAAECggEAA+SEZHnaXyhOAiYKwKDXQYPsQIBWzwgcz12XagxfrLjr\ncJYGfu1zTIZ0FHXAjsgP0yIvcTRYvnP+vlqFA4lPP2E07FYxhIFN2os8s6GHeH6a\nE8RcgKfuGfwI3hH7oh/6lgUY2a7MPIHXdiJRRO4e6XG5RDsRvVF5M140vryY7eqd\nTR2t2TbCi2JI0QUpg0ssuDAKO9GH5XsDfhLyXdtnDjljbG5ZR0ERidcGg4+Q5FVB\nuIL4K//b52605AFoWviCI+FXnkB3VQ1zdL+/M5LbEYA8UIDtdFTcWB9bsMpfymxa\nuY/jKc46P30muCcob49o5h2QDQh1GvwlES6vwzyhqQKBgQD+oUoc5nqfgdOvNRal\n54b9JyAwIBiFGepMqBOUToB2Ec30DVy9YpIaXI6F1YkSgEu963I5WEGHFm4rhwlX\nfZIzlpKgmTg4jMVBM3/sZB9M9vnKwDcLU3GNLrN8ypJMgdEVKmZ7a2OksGSQrFht\nvu+uw1QGZmPnonW0VP5wtFT5bQKBgQDRt8BOBerDP+1hLvK64s/ACFGOb0Iop7mh\npYNas7WNauE34Je2Kj8E6wsZxAfkjafKN+MW0MwgGtKid1R51BxBtvcA8r+EM1yf\nHRAHLR6RWtaYdmA1HHg5JQgeJxilCU9AbNS5nL4bQYemUKhPyoCvUL9eWTaNX/Ak\nFVI/Ed4hswKBgQCiJwZyZxf50gyDTBSTLGEbf7oQy6+xu3IoxPRLAr7t8aKtY4EG\nneoa3YxpkDWNUaRqWrDP8fMw2sjn8UOysqXTMnVHzqst3/+R6QDzAkOomLM0OboT\n/VyXowDsXHhUPmtuxiSjPh0jeK1iME7T/L7YFU3CEZxXm27Hm0S5cy2V9QKBgQCd\nelnRPOg4jXx3CYYDh+Vw0c5MIoePd8MQ+vRT27Zs5uEP0Hqbs8V2r/i59FXo7eYd\nFzJTI57kTL/2d5zbjsdZIUcBU0c0wky+vlgWy260v319Jwa/Ww17+67I1ZrP8tms\nCw0CBA1M8jwmS1LX97wB6aSJ+HvaVTxCHDCSY5xluQKBgEgtdJypjVyq7GlFs291\n/+ygF17mN2dmSnNF1pUbVLL2XDTD4EGZWwmszjpfWaWHA4FYpPiysRzqMX/QdFjS\n9WrBULi+R5jV1DG9Zrv+5FFj7UM5OhLrlrvmj7quL1OGORBieYGBUSx5OsVFTjCI\naRk2pxahEJ7Dq2210veTS2dP\n-----END PRIVATE KEY-----\n",
  "client_email": "myaccount@tranquil-lotus-368022.iam.gserviceaccount.com",
  "client_id": "113062977233857615563",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/myaccount%40tranquil-lotus-368022.iam.gserviceaccount.com"
}

try:
  res = requests.get(
  f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

  print("Loading...")

  soup = BeautifulSoup(res.text, 'html.parser')

  info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()

  print(info)

  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('weather_sp')
  blob = bucket.blob('weather_info.txt')

  blob.upload_from_string(info + '\n')

  print('File uploaded.')

  print("Finished.")
except Exception as ex:
  print(ex)