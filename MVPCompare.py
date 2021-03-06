import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize



input = input("Input Year (1985-2021) or All to see every MVP: ")

def Table(): #Takes the table from the website and formats it.
    link = 'https://www.basketball-reference.com/awards/awards_' + input + '.html'
    nba_mvp = pd.read_html(link, match='Most Valuable Player')
    df = nba_mvp[0]
    return df
    

def Sort(): #This is to make anyone who does not fill all of the stats drop out of the list.
    temp = Table()
    i = 0
    while i < temp.shape[0]:
        if np.isnan(temp.at[i,('Shooting', '3P%')]) == True:
            temp.at[i, ('Shooting', '3P%')] = .000
        i+=1
    return temp

def PlayerList():
    list = Sort()
    tempList = [[""]*11 for i in range(list.shape[0])]
    i = 0
    while i < list.shape[0]:
        tempList[i][0] = list.at[i,('Unnamed: 1_level_0', 'Player')]
        tempList[i][1] = list.at[i, ('Unnamed: 0_level_0', 'Rank')]    
        i+=1    
    playerList = pd.DataFrame(tempList)
    playerList.columns = ['Players', 'Rank', 'Points', 'Rebounds', 'Assists', 'Steals', 'Blocks', 'GamesPlayed', 'Winshare', 'WinsharePer', 'MVPScore']
    return playerList

def Winshare():
    temp = Sort()
    playerList = PlayerList()
    i = 0
    while i < temp.shape[0]:
        x = temp.at[i, ('Advanced', 'WS')]
        x = 0.2 * x
        playerList.loc[i, 'Winshare'] = x
        x = 0
        i += 1
    return playerList

def Winshare48():
    temp = Sort()
    playerList = Winshare()
    i = 0
    while i < temp.shape[0]:
        x = temp.at[i, ('Advanced', 'WS/48')]
        x = 0.2 * x
        playerList.loc[i, 'WinsharePer'] = x
        x = 0
        i += 1
    return playerList

def Points():
    temp = Sort()
    playerList = Winshare48()
    i = 0
    while i < temp.shape[0]:
        x = temp.at[i, ('Per Game', 'PTS')]
        x = 0.2 * x
        playerList.loc[i, 'Points'] = x
        x = 0
        i += 1
    return playerList

def Rebounds():
    temp = Sort()
    playerList = Points()
    i = 0
    while i < temp.shape[0]:
        x = temp.at[i, ('Per Game', 'TRB')]
        x = 0.075 * x
        playerList.loc[i, 'Rebounds'] = x
        x = 0
        i += 1
    return playerList

def Assists():
    temp = Sort()
    playerList = Rebounds()
    i = 0
    while i < temp.shape[0]:
        x = temp.at[i, ('Per Game', 'AST')]
        x = 0.075 * x
        playerList.loc[i, 'Assists'] = x
        x = 0
        i += 1
    return playerList

def Steals():
    temp = Sort()
    playerList = Assists()
    i = 0
    while i < temp.shape[0]:
        x = temp.at[i, ('Per Game', 'STL')]
        x = 0.1 * x
        playerList.loc[i, 'Steals'] = x
        x = 0
        i += 1
    return playerList

def Blocks():
    temp = Sort()
    playerList = Steals()
    i = 0
    while i < temp.shape[0]:
        x = temp.at[i, ('Per Game', 'BLK')]
        x = 0.1 * x
        playerList.loc[i, 'Blocks'] = x
        x = 0
        i += 1
    return playerList

def GamesPlayed():
    temp = Sort()
    playerList = Blocks()
    i = 0
    while i < temp.shape[0]:
        x = temp.at[i, ('Unnamed: 8_level_0', 'G')]
        x = 0.05 * x
        playerList.loc[i, 'GamesPlayed'] = x
        x = 0
        i += 1
    return playerList

def MVPScore():
    playerList = GamesPlayed()

    i = 0
    x = 2
    a = 0
    while i < playerList.shape[0]:
        while x <= 8:
            a += playerList.iat[i,x]
            x += 1
        playerList.loc[i, 'MVPScore'] = a
        a = 0
        x = 2
        i += 1
    playerList.sort_values(by='MVPScore', ascending=False, inplace=True)
    return playerList

temp = MVPScore()
data = temp['MVPScore']
data = data[:11]
i = 0
while i < temp.shape[0]:
    temp.iat[i, 0] = temp.iat[i, 0] +" "+ temp.iat[i,1]
    i += 1
labels = temp['Players']
labels = labels[:11]
plt.rc('xtick', labelsize=6)
plt.bar_label(plt.bar(range(len(data)), data, color=['navy']))
plt.xticks(range(len(labels)), labels)
plt.xlabel('Names')
plt.ylabel('Score')
plt.show()