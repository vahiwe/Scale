import logging
from bs4 import BeautifulSoup
from django.conf import settings
import requests
from requests import exceptions
import datetime
from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)


class RemoteOKAPIClient():

    BASE_URL = 'https://remoteok.io/api?ref=producthunt'

    def __init__(self):
        pass

    def headers(self):
        return {
            'cache-control': 'no-cache',
        }

    def getjobs(self):
        retries_count = 3
        retry = 0
        while True:
            logger.debug(f'Sending request: {self.BASE_URL}')
            resp = requests.get(
                    self.BASE_URL, headers=self.headers())
            if not resp.ok:
                try:
                    resp.raise_for_status()
                except exceptions.HTTPError as error:
                    if retry < retries_count:
                        retry += 1
                        logger.debug(f'Sending the request again. Retry count: {retry}')
                        continue
                    else:
                        logger.debug(f'Retries are exceeded')
                        raise
                            
            else:
                resp = resp.json()
                break
        return resp


class IndeedAPIClient():

    BASE_URL = 'https://www.indeed.com/jobs?q=javascript&l=New+York+City&start='

    def __init__(self):
        pass

    def get_past_date(self, str_days_ago):
        TODAY = datetime.date.today()
        splitted = str_days_ago.split()
        if len(splitted) == 1 and splitted[0].lower() == 'today':
            return str(TODAY.isoformat())
        elif len(splitted) == 1 and splitted[0].lower() == 'yesterday':
            date = TODAY - relativedelta(days=1)
            return str(date.isoformat())
        elif splitted[1].lower() in ['hour', 'hours', 'hr', 'hrs', 'h']:
            date = datetime.datetime.now() - relativedelta(hours=int(splitted[0]))
            return str(date.date().isoformat())
        elif splitted[1].lower() in ['day', 'days', 'd']:
            date = TODAY - relativedelta(days=int(splitted[0]))
            return str(date.isoformat())
        elif splitted[1].lower() in ['wk', 'wks', 'week', 'weeks', 'w']:
            date = TODAY - relativedelta(weeks=int(splitted[0]))
            return str(date.isoformat())
        elif splitted[1].lower() in ['mon', 'mons', 'month', 'months', 'm']:
            date = TODAY - relativedelta(months=int(splitted[0]))
            return str(date.isoformat())
        elif splitted[1].lower() in ['yrs', 'yr', 'years', 'year', 'y']:
            date = TODAY - relativedelta(years=int(splitted[0]))
            return str(date.isoformat())
        else:
            return str(TODAY.isoformat())

    def getjobs(self):
        items = []
        page = 0
        page_size = 10
        retries_count = 3
        retry = 0
        escapes = ''.join([chr(char) for char in range(1, 32)])
        translator = str.maketrans('', '', escapes)
        while True:
            logger.debug(f'Sending request: {self.BASE_URL}')
            resp = requests.get(
                    f'{self.BASE_URL}{10*page}')
            if not resp.ok:
                try:
                    resp.raise_for_status()
                except exceptions.HTTPError as error:
                    if retry < retries_count:
                        retry += 1
                        logger.debug(f'Sending the request again. Retry count: {retry}')
                        continue
                    else:
                        logger.debug(f'Retries are exceeded')
                        raise
                            
            else:
                soup = BeautifulSoup(resp.content, features="lxml") 
                jobs = soup.find_all("div", class_="jobsearch-SerpJobCard")
                for job in jobs:

                    if job.find_all("h2", class_="title")[0].string is None:
                        position = job.find_all("h2", class_="title")[0].a.get_text()
                        position = position.translate(translator)
                        url = "https://www.indeed.com" + job.find_all("h2", class_="title")[0].a.get('href')
                    else:
                        position = job.find_all("h2", class_="title")[0].string
                        position = position.translate(translator)

                    if job.find_all("span", class_="company")[0].string is None:
                        company = job.find_all("span", class_="company")[0].a.get_text()
                        company = company.translate(translator)
                    else:
                        company = job.find_all("span", class_="company")[0].string
                        company = company.translate(translator)

                    description = ''
                    if job.find_all("div", class_="summary")[0].ul is not None:
                        if job.find_all("div", class_="summary")[0].ul.children is not None:
                            for child in job.find_all("div", class_="summary")[0].ul.children:
                                if child.string is not None:
                                    description += child.string
                            description = description.translate(translator)
                   

                    id = job.get('data-jk')

                    date = job.find_all("span", class_="date")[0].string
                    date = date.replace('+','')
                    date = self.get_past_date(date)
                    try:
                        location = job.find_all("span", class_="location")[0].string
                    except IndexError:
                        location = ''

                    item = {'position': position, 'url': url, 'company': company, 'description': description, 'id': id, 'date': date, 'location': location}
                    items.append(item)
            if page >= page_size:
                break
            page += 1
        return items
