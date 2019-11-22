import requests as r


class requests:

    URL = "https://br1.api.riotgames.com/lol/"  # URL BASE
    PARAMS = {'api_key': 'RGAPI-2d230ebe-a5e9-4e49-ba01-da132a9198c1'}

    def __init__(self, SummonerName):
        full_URL = self.URL + "summoner/v4/summoners/by-name/"
        self.summoner = r.get(url=full_URL+SummonerName,
                              params=self.PARAMS).json()

        full_URL = self.URL + "match/v4/matchlists/by-account/"
        self.matchList = r.get(url=full_URL+self.summoner['accountId'],
                               params=self.PARAMS).json()

        full_URL = self.URL + "champion-mastery/v4/champion-masteries/by-summoner/"
        self.masteryChampions = r.get(url=full_URL+self.summoner['id'],
                                      params=self.PARAMS).json()


def main():
    SummonerName = input("Entre com o Summoner Name: ")
    user = requests(SummonerName)

    print(user.summoner)


main()
