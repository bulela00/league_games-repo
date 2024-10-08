# League opponents draw 

#=======importing libraries=======
import pandas as pd 
from numpy import random

#=======Functions=======
# This function recieves the team information for the teams in the leagues 
def league_team(): 
    # confirmation of no. of teams 
    check = input("How many teams are in the league?")
    if check == 36: 
        print('Please enter the team information as prompted')
        for x in 36:
            # accepts teams' name
            team_name = input("Enter the team name")
            # teams' points 
            team_points = input("Enter the team points")
            # teams' location 
            team_location = input("Enter team location")
            with open('teams.txt', 'a+', encoding='utf-8-sig') as team_info:
                info = 0
                for line in team_info:
                    info +=1 

    else:
        print("Invalid number of teams. ")

    return 

# This function splits the league teams into four groups based on the team points
def league_groups(df): 
    contnents =""
    with open('teams.txt', 'r+', encoding='utf-8-sig') as file: 
        for line in file:
          contents = contents + line   

    # sort teams based on points 
    # df is the teams_list 
    df.sort_values('points', ascending=False) 
    # split the sorted list into four groups 
    gr1 = df.iloc[0:8,:]
    gr2 = df.iloc[9:17,:]
    gr3 = df.iloc[18:26,:]
    gr4 = df.iloc[27:35,:]
    return(df,gr1, gr2, gr3, gr4) 

# This function selects a random team from the specified group
def team_selection(df, grp):
    # random team no selection
    len(grp)
    x = random.randint(len-1)
    team = grp[x]

    return(team)


# This function identifies teams in the same location and excludes them for the team
def same_loc(team_location, gr1, gr2, gr3, gr4): 
    mygr1 ={}
    # identify team location
    # identify teams in that location 
    for team in gr1:
        if gr1.iloc[team,1] == team_location:
            print(f'{gr1.iloc[team,1]} has been exculded')
        else:
            mygr1 = mygr1.append(gr1.iloc[team,0])

    for team in gr2:
        if gr2.iloc[team,1] == team_location:
            print(f'{gr2.iloc[team,1]} has been exculded')
        else:
            mygr2 = mygr2.append(gr2.iloc[team,0])

    for team in gr3:
        if gr3.iloc[team,1] == team_location:
            print(f'{gr3.iloc[team,1]} has been exculded')
        else:
            mygr3 = mygr3.append(gr3.iloc[team,0])
        
    for team in gr4:
        if gr4.iloc[team,1] == team_location:
            print(f'{gr4.iloc[team,1]} has been exculded')
        else:
            mygr4 = mygr4.append(gr1.iloc[team,0])
    return(mygr1, mygr2, mygr3, mygr4)

# This function extracts the info for the selected team
def team_info(team):
    team = team.strip()
    team = team.split(",") 
    team_name = team[0]
    team_location = team[1]
    team_group = team[2]
    return (team_name, team_location, team_group)

# This function randomly selects the selcted teams opponents 




# Input the teams in the league 
league_team()    #Input team in the league
(team_df, pot1, pot2, pot3, pot4) = league_groups()    # split teams in 4 pots 
selected_team = team_selection(team_df, pot1)    # Select a team to find the opposition for
(steam_name, steam_location, steam_group) = team_info(selected_team)    # Extract innfo on partner
(my_pot1, my_pot2, my_pot3, my_pot4) = same_loc(steam_location, pot1, pot2, pot3, pot4)    # define options to be opposition
  