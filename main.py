from riotwatcher import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_key = 'RGAPI-fe303f41-5b90-4557-b506-580a8d5c4801'
    watcher = LolWatcher(api_key)
    my_region = 'euw1'

    me = watcher.summoner.by_name(my_region, 'LukyLucc')
    changing = True
    i = 0
    matches = []
    while changing:
        match = watcher.match.matchlist_by_puuid('EUROPE', me['puuid'], start=i, count=100)
        matches.append(match)
        if len(match) < 100:
            changing = False
        i += 100


    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
