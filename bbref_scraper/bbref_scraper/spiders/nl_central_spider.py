import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "nl_central"

    def write_to_json(self, dict):
        jsonString = json.dumps(dict)
        with open("nl_central.json", "a") as jsonFile:
            jsonFile.write(jsonString)

    def start_requests(self):
        urls = [
            'https://www.baseball-reference.com/boxes/?year=2021&month=04&day=15'
            # 'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        date = {
            "date": 20210714,
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
            print('here')
            print(row)
            team = row.xpath('th//text()').get()
            wins = row.xpath('td[@data-stat="W"]/text()').get()
            losses = row.xpath('td[@data-stat="L"]/text()').get()
            games_back = row.xpath('td[@data-stat="games_back"]/text()').get()

            print(team)
            print(wins)
            print(losses)
            print(games_back)

            date[team]["wins"] = wins
            date[team]["losses"] = losses
            date[team]["games_back"] = games_back

        self.write_to_json(date)
