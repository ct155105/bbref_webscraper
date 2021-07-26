import scrapy
import json
from calendar import monthrange
from urllib.parse import urlencode


class QuotesSpider(scrapy.Spider):
    name = "nl_central"


    def write_to_json(self, dict):
        jsonString = json.dumps(dict)
        with open("nl_central.json", "a") as jsonFile:
            jsonFile.write(jsonString)


    def generate_urls(self):
        
        base_url = 'https://www.baseball-reference.com/boxes/'
        urls = []
        year = 2021
        for i in range(3,11):
            month = i
            for day in range(monthrange(year,month)[1]):
                dt = { "year" : year, "month" : month, "day" : day + 1 }
                url = base_url + "?" + urlencode(dt)
                urls.append({ "date" : dt, "url" : url } )

        return urls


    def start_requests(self):

        urls = self.generate_urls()
        for url in urls:
            yield scrapy.Request(url=url['url'], callback=self.parse, cb_kwargs=dict(dt=url['date']))


    def parse(self, response, dt):

        date = {
            "date": dt,
            "CIN": {
                "wins": 0,
                "losses": 0,
                "games_back": 0
            },
            "MIL": {
                "wins": 0,
                "losses": 0,
                "games_back": 0
            },
            "CHC": {
                "wins": 0,
                "losses": 0,
                "games_back": 0
            },
            "STL": {
                "wins": 0,
                "losses": 0,
                "games_back": 0
            },
            "PIT": {
                "wins": 0,
                "losses": 0,
                "games_back": 0
            }
        }

        rows = response.xpath('//table[@id="standings-upto-NL-C"]/tbody//tr')
        for row in rows:
            print(row)
            team = row.xpath('th//text()').get()
            wins = row.xpath('td[@data-stat="W"]/text()').get()
            losses = row.xpath('td[@data-stat="L"]/text()').get()
            games_back = row.xpath('td[@data-stat="games_back"]/text()').get()

            try:
                date[team]["wins"] = float(wins)
            except Exception:
                pass
            try:
                date[team]["losses"] = float(losses)
            except Exception:
                pass
            try:
                date[team]["games_back"] = float(games_back)
            except Exception:
                pass

        self.write_to_json(date)
