import requests
from bs4 import BeautifulSoup

URL = "https://www.ezpassva.com/Login/Login.aspx"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
USERNAME = ''
PASSWORD = ''


def main():
    with requests.Session() as session:
        session.headers.update(HEADERS)

        request = session.get(URL)
        soup = BeautifulSoup(request.content, 'html.parser')

        payload = {
            '__VIEWSTATE': soup.find(id='__VIEWSTATE')['value'],
            '__VIEWSTATEGENERATOR': soup.find(id='__VIEWSTATEGENERATOR')['value'],
            '__EVENTVALIDATION': soup.find(id='__EVENTVALIDATION')['value'],
            'ctl00$VDOTContentPlaceHolder$txtUserName': USERNAME,
            'ctl00$VDOTContentPlaceHolder$txtPassword': PASSWORD,
            'ctl00$VDOTContentPlaceHolder$btnLogin': 'Login'
        }

        request = session.post(URL, data=payload)
        soup = BeautifulSoup(request.content, 'html.parser')
        print(soup.select_one('#ctl00_VDOTContentPlaceHolder_grdAccountInfo').select('tr')[5].select('td')[1].text)


if __name__ == '__main__':
    main()
