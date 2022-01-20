from riotwatcher import *
from datetime import datetime
import numpy as np


class Wrapper:
    """
    Wrapperclass for the Riot Api and riotwatcher
    """

    def __init__(self, api_key, my_region, summoner_name):
        """
        Initialize Wrapper Class
        :param api_key: String
        :param my_region: String
        :param summoner_name: String
        """
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

    def getSmallMatchHistory(self, count=20) -> list:
        """
        Returns the last 'count' GameIDs
        :param count: Int
        :return: list of GameIDs
        """
        matches = self.watcher.match.matchlist_by_puuid('EUROPE', self.getPuuid(), count=count)
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
        try:
            game = self.watcher.match.by_id("EUROPE", game_id)
        except:
            return 0
        unix = game['info']['gameCreation']
        unix = int(unix / 1000)

        date = datetime.fromtimestamp(unix).date()
        return date

    def getAllDates(self, matches) -> np.array:
        """
        Get the Dates of all GameIDs in 'matches'

       :param matches:
       :return: np.array x,y -> X-Axis and Y-Axis for the Plot
       """
        x = np.array([], dtype='datetime64')
        y = np.array([])

        for game_id in matches:
            date = self.getDate(game_id)
            if date != 0:
                if date in x:
                    index = np.where(x == date)
                    y[index] += 1
                else:
                    x = np.append(x, date)
                    y = np.append(y, 1)
        return x, y
