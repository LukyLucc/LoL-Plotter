from Wrapper import *
from Plotter import *


def plotSmall(api_key, my_region, name, count=20):
    """
    Plots small sample size
    :param api_key:
    :param my_region:
    :param name:
    :return:
    """
    wrapper = Wrapper(api_key, my_region, name)
    matches = wrapper.getSmallMatchHistory(count)
    x, y = wrapper.getAllDates(matches)
    plotNormal(x, y)


def plotBig(api_key, my_region, name):
    """
    Plots all Data found
    :param api_key:
    :param my_region:
    :param name:
    :return:
    """
    wrapper = Wrapper(api_key, my_region, name)
    matches = wrapper.getMatchHistory()
    x, y = wrapper.getAllDates(matches)
    plotTrendLine(x, y)


if __name__ == '__main__':
    api_key = 'RGAPI-10ca454b-824a-4f06-9040-09015b569dcb'
    my_region = 'euw1'
    name = 'LukyLucc'

    plotBig(api_key, my_region, name)
