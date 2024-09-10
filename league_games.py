# League opponents draw 

#=======importing libraries=======
import pandas as pd 

#=======Functions=======
# This function recieves the team information for the teams in the leagues 
def league_team(): 
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

    return 

# This function splits the league teams into four groups based on the team points
def league_groups(df): 
    with open('teams.txt', 'r+', encoding='utf-8-sig') as file: 
        for line in file:
          pass   

    # sort teams based on points 
    # df is the teams_list 
    df.sort_values('points', ascending=False) 
    # split the sorted list into four groups 
    gr1 = df.iloc[0:8,:]
    gr2 = df.iloc[9:17,:]
    gr3 = df.iloc[18:26,:]
    gr4 = df.iloc[27:35,:]
    return(df,gr1, gr2, gr3, gr4) 

# This function identifies teams in the same location 
def same_loc(team): 
    # identify team location 
    # identify teams in that location 
    return 

# This function extracts the info for the selected team
def team_info(team):
    team = team.strip()
    team = team.split(",") 
    team_name = team[0]
    team_location = team[1]
    team_group = team[2]
    return


# Define teams in the league 
# Accept input of team data for teams that have qualified for the team 
# Team data includes: team location, team grouping 


# Define constraints 



# Define function that selects teams eligible to be opponents to selected team



# Define order of the draw 


# Accept random number for team selection 

# Find out which oponents each team already has 



# Create case for team selection of each group 
