# League opponents draw 

#=======importing libraries=======
import pandas as pd 
from numpy import random

#=======Functions=======
# This function recieves the team information for the teams in the leagues 
def league_team(): 
    # confirmation of no. of teams 
    check = int(input("How many teams are in the league? "))
    if check == 36: 
        teams = ""
        print('Please enter the team information as prompted:')
        for x in range(1,37):
            print(f'Team {x}:')
            # accepts teams' name
            team_name = input(f"Enter the team name: ")
            # teams' location 
            team_location = input("Enter team location: ")
            # teams' points 
            team_points = int(input("Enter the team points: "))
            team_info = ",".join([team_name,team_location,team_points])
            teams = teams + team_info + '\n'
            
        with open('teams.txt', 'w+', encoding='utf-8-sig') as file:
            file.write(teams)
   
    else:
        print("Invalid number of teams. ")

    return 

# This function splits the league teams into four groups based on the team points
def read_teams(): 
    team = []
    team_location = []
    team_points = []
    # Read league teams 
    with open('teams.txt', 'r+', encoding='utf-8-sig') as file: 
        for line in file:
            temp = line.strip()
            temp = temp.split(",")    # Split the line of team info 
            team.append(temp[0])    # Add the team name to the team list
            team_location.append(temp[1])    # Add the team location into the locations list
            team_points.append(temp[2])    # Add the teams points into the team points list 


    # Create a dictionary of team info lists
    team_info = {'Team': team,
                 'Team_location': team_location, 
                 'Team_points': team_points}
    
    df = pd.DataFrame(team_info)    # Convert the team info into a DataFrame
    league_groups(df)

# This function splits the teams in the league into 4 groups 
def league_groups(df):
    # df is the teams_list 
    df['Team_points'] = pd.to_numeric(df['Team_points'])
    # sort teams by team points 
    df = df.sort_values('Team_points') 

    # split the sorted list into four groups 
    gr1 = df.iloc[0:8,:]    # group 1
    gr2 = df.iloc[9:17,:]    # group 2
    gr3 = df.iloc[18:26,:]    # group 3
    gr4 = df.iloc[27:35,:]    # group 4
 
    return(df,gr1, gr2, gr3, gr4)


# This function selects a random team from the specified group
def team_selection(grp):
    # random team no selection
    len(grp)
    x = random.randint(len-1)
    team = grp[x]
    del grp['team']

    return(team, grp)


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


def team_draw(my_groups, team):
    teams = []
    # random team no selection
    for grp in my_groups:
        len(grp)
        x = random.randint(len-1)
        team = grp[x]
        del grp['team']

    return (teams)





# Input the teams in the league 
#league_team()    #Input team in the league
#(team_df, pot1, pot2, pot3, pot4) = league_groups()    # split teams in 4 pots 
read_teams()
'''(selected_team, new_pot1) = team_selection( pot1)    # Select a team to find the opposition for
(steam_name, steam_location, steam_group) = team_info(selected_team)    # Extract innfo on partner
(my_pot1, my_pot2, my_pot3, my_pot4) = same_loc(steam_location, pot1, pot2, pot3, pot4)    # define options to be opposition
my_options = [my_pot1, my_pot2, my_pot3, my_pot4]
(opposition_teams) = team_draw(my_options, selected_team)'''
