import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

def Table(): #Takes the table from the website and formats it.
    nba_mvp = pd.read_html('https://www.basketball-reference.com/awards/mvp.html#all_mvp_NBA', match='NBA Winners')
    df = nba_mvp[0]
    df.drop(columns='Unnamed: 1_level_0')
    row_count = df.shape[0]
    table = df.head(row_count)
    lg = table.drop('Unnamed: 1_level_0', axis=1)
    return lg

def Sort(): #This is to make anyone who does not fill all of the stats drop out of the list.
    temp = Table()
    i = 0
    while i < temp.shape[0]:
        if np.isnan(temp.at[i,('Shooting', '3P%')]) == True:
            temp.drop(temp.index[i:temp.shape[0]], 0, inplace=True)
            i+=1
        i+=1
    return temp

def WS10():
    temp = Sort()
    temp.sort_values(by=[('Advanced', 'WS')], ascending=False, inplace=True)
    temp.drop(temp.index[11:temp.shape[0]], 0, inplace=True)
    return temp

def WS48():
    temp = Sort()
    temp.sort_values(by=[('Advanced', 'WS/48')], ascending=False, inplace=True)
    temp.drop(temp.index[11:temp.shape[0]], 0, inplace=True)
    return temp

def PTS10():
    temp = Sort()
    temp.sort_values(by=[('Per Game', 'PTS')], ascending=False, inplace=True)
    temp.drop(temp.index[11:temp.shape[0]], 0, inplace=True)
    return temp

def REB10():
    temp = Sort()
    temp.sort_values(by=[('Per Game', 'TRB')], ascending=False, inplace=True)
    temp.drop(temp.index[11:temp.shape[0]], 0, inplace=True)
    return temp

def AST10():
    temp = Sort()
    temp.sort_values(by=[('Per Game', 'AST')], ascending=False, inplace=True)
    temp.drop(temp.index[11:temp.shape[0]], 0, inplace=True)
    return temp

def STL10():
    temp = Sort()
    temp.sort_values(by=[('Per Game', 'STL')], ascending=False, inplace=True)
    temp.drop(temp.index[11:temp.shape[0]], 0, inplace=True)
    return temp

def BLK10():
    temp = Sort()
    temp.sort_values(by=[('Per Game', 'BLK')], ascending=False, inplace=True)
    temp.drop(temp.index[11:temp.shape[0]], 0, inplace=True)
    return temp

def GP10():
    temp = Sort()
    temp.sort_values(by=[('Unnamed: 6_level_0', 'G')], ascending=False, inplace=True)
    temp.drop(temp.index[11:temp.shape[0]], 0, inplace=True)
    return temp


def PlayerList():
    list = Sort()
    tempList = [[""]*3 for i in range(list.shape[0])]
    i = 0
    while i < list.shape[0]:
        tempList[i][0] = list.at[i,('Unnamed: 2_level_0', 'Player')]
        tempList[i][1] = list.at[i, ('Unnamed: 0_level_0', 'Season')]    
        i+=1    
    playerList = pd.DataFrame(tempList)
    playerList.columns = ['Players', 'Season', 'Points']
    return playerList

def PointsList():
    winShare = WS10()
    winShare48 = WS48()
    points = PTS10()
    rebounds = REB10()
    assists = AST10()
    steals = STL10()
    blocks = BLK10()
    gamesPlayed = GP10()
    playerList = PlayerList()
    i = 0
    x = 0
    temp = 0
    while x < playerList.shape[0]:
        if playerList.at[x, "Players"] == (winShare.at[i,('Unnamed: 0_level_0', 'Season')]):
            playerList.loc[x, 2] = 20 - (i * 2)
            i += 1
        if i == 9:
            x = playerList.shape[0]
        x+=1
    return playerList

temp = PointsList()
print(temp)
        
            