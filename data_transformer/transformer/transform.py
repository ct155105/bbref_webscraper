import json



def append_day_to_season(day, season):
    season['date'].append(str(day['date']['month']) + '/' + str(day['date']['day']) + '/' + str(day['date']['year']))
    
    season['nl_central']['CIN']['wins'].append(day['CIN']['wins'])
    season['nl_central']['CIN']['losses'].append(day['CIN']['losses'])
    season['nl_central']['CIN']['games_back'].append(day['CIN']['games_back'])

    season['nl_central']['MIL']['wins'].append(day['MIL']['wins'])
    season['nl_central']['MIL']['losses'].append(day['MIL']['losses'])
    season['nl_central']['MIL']['games_back'].append(day['MIL']['games_back'])
    
    season['nl_central']['PIT']['wins'].append(day['PIT']['wins'])
    season['nl_central']['PIT']['losses'].append(day['PIT']['losses'])
    season['nl_central']['PIT']['games_back'].append(day['PIT']['games_back'])

    season['nl_central']['STL']['wins'].append(day['STL']['wins'])
    season['nl_central']['STL']['losses'].append(day['STL']['losses'])
    season['nl_central']['STL']['games_back'].append(day['STL']['games_back'])

    season['nl_central']['CHC']['wins'].append(day['CHC']['wins'])
    season['nl_central']['CHC']['losses'].append(day['CHC']['losses'])
    season['nl_central']['CHC']['games_back'].append(day['CHC']['games_back'])


def sort_by_day(item):
    return item['date']['day']


def get_months_results(season, month: int):
    result = list(filter(lambda x: x['date']['month'] == month, season))
    return result


def write_to_json(dict):
    jsonString = json.dumps(dict)
    with open("nl_central_2021.json", "a") as jsonFile:
        jsonFile.write(jsonString)


def process_month(season_json, month_int, season_result):
    month = get_months_results(season_json,month_int)
    month.sort(key=sort_by_day)
    for day in month:
        append_day_to_season(day, season_result) 


def process_season(season_json):

    season_results = {
        "date": [],
        "nl_central": {
            "CIN": {
                "wins": [],
                "losses": [],
                "games_back": []
            },
            "MIL": {
                "wins": [],
                "losses": [],
                "games_back": []
            },
            "STL": {
                "wins": [],
                "losses": [],
                "games_back": []
            },
            "CHC": {
                "wins": [],
                "losses": [],
                "games_back": []
            },
            "PIT": {
                "wins": [],
                "losses": [],
                "games_back": []
            }
        }
    }

    with open('nl_central.json') as json_file:
        season_json = json.load(json_file)
        for month in range(3,11):
            process_month(season_json, month, season_results)

    return season_results

test = process_season('/workspaces/scraper_poc/nl_central.json')
write_to_json(test)