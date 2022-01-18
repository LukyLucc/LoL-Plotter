from riotwatcher import *
from datetime import datetime
from collections import defaultdict


class Wrapper:
    """

    """

    def __init__(self, api_key, my_region, summoner_name):
        self.api_key = api_key
        self.my_region = my_region
        self.summoner_name = summoner_name
        self.watcher = LolWatcher(api_key)

    def getMatchHistory(self) -> list:
        """
        Methode to get all available GameIDs
        :return: list of GameIDs
        """
        changing = True
        i = 0
        matches = []
        while changing:
            match = self.watcher.match.matchlist_by_puuid('EUROPE', self.getPuuid(), start=i, count=100)
            matches.extend(match)
            if len(match) < 100:
                changing = False
            i += 100

        return matches

    def getSummoner(self):
        """
        Methode to get a Specific Summoner
        :return:
        """
        return self.watcher.summoner.by_name(self.my_region, self.summoner_name)

    def getPuuid(self) -> str:
        """
        Methode to get the Puuid of an Account
        :return: string 'Puuid'
        """
        return self.getSummoner()['puuid']

    def getDate(self, game_id) -> datetime.date:
        """
        Methode to get the Date when a Game was played
        :return: Date Object YYYY-MM-DD
        """
        game = self.watcher.match.by_id("EUROPE", game_id)
        unix = game['info']['gameCreation']
        unix = int(unix / 1000)

        date = datetime.fromtimestamp(unix)
        return date

    def getAllDates(self) -> list:
        """

        :return: list of datetime
        """
        #matches = self.getMatchHistory()
        sampel_matches = ['EUW1_5675455489', 'EUW1_5675378816', 'EUW1_5675402656', 'EUW1_5673282942', 'EUW1_5669648539',
                          'EUW1_5669620635', 'EUW1_5667456956', 'EUW1_5665085560', 'EUW1_5665080642', 'EUW1_5663575630',
                          'EUW1_5663433898'
                          ]
        dict = defaultdict(int)

        for game_id in sampel_matches:
            date = self.getDate(game_id)
            dict[date.strftime("%d")] += 1
        return dict
