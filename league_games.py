# League opponents draw 
# This project is used to determine the schedule of a sports tournament 
# Each team must face 8 unique opponents. 
# The 8 opponents will be 2 teams from each group 

# Order of operation 
# The qualifying teams information must be input by the user
# The input data must then be sorted by team points and split into groups 

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
            team_points = input("Enter the team points: ")
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
            team_points.append(int(temp[2]))  # Add the teams points into the team points list
 
    # Create a dictionary of team info lists
    team_info = {'Team': team,
                 'Team_location': team_location, 
                 'Team_points': team_points}
    
    df = pd.DataFrame(team_info)    # Convert the team info into a DataFrame

    print(df.dtypes)
    return(df)


# This function splits the teams in the league into 4 groups 
def league_groups(df):

    # df is the teams_list 
    df['Team_points'] = pd.to_numeric(df['Team_points'])
    # sort teams by     team points 
    df = df.sort_values('Team_points').reset_index(drop=True) 

    # split the sorted list into four groups 
    gr1 = df.iloc[0:9,:]    # group 1
    gr2 = df.iloc[9:18,:]    # group 2
    gr3 = df.iloc[18:27,:]    # group 3
    gr4 = df.iloc[27:36,:]    # group 4

    print('Group 1:\n' , gr1 , '\n')
    print('Group 2:\n' , gr2 , '\n')
    print('Group 3:\n' , gr3 , '\n')
    print('Group 4:\n' , gr4 , '\n')

    matches = {} # creating a dictionary to save each teams opposition
 
    return(df,gr1, gr2, gr3, gr4, matches)


# This function produces a dataframe for the away and home games 
def home_away(gr1, gr2, gr3, gr4):
    home_teams = {'group1h': gr1.iloc[:,0].to_list(),  # Creates a list of the team names from each group
                  'group2h': gr2.iloc[:,0].to_list(),
                  'group3h': gr3.iloc[:,0].to_list(),
                  'group4h': gr4.iloc[:,0].to_list()}
    away_teams = {'group1a': gr1.iloc[:,0].to_list(),
                  'group2a': gr2.iloc[:,0].to_list(),
                  'group3a': gr3.iloc[:,0].to_list(),
                  'group4a': gr4.iloc[:,0].to_list()}

    return (home_teams, away_teams)


# This function selects a random team from the specified group
def team_selection(grp):
    team = random.choice(grp.iloc[:,0])    # Select a random team from the group
    team_location = grp[grp['Team'] == team]['Team_location'].iloc[0]
    grp.drop(grp[grp['Team'] == team].index, inplace=True)    # Remove the selected team from the group returned by the function

    return(team, team_location, grp)

###################################################################################################################
# This function identifies teams in the same location and excludes them for the team
def same_loc(team_location, gr1, gr2, gr3, gr4): 
    # The groups i.e. gr1, gr2, gr3 and gr4 are dataframes in this case and not lists 

    grps = (gr1, gr2, gr3, gr4)
    # identify team location
    # identify teams in that location 
    gr1.loc[gr1['Team_location']==team_location,:]
    '''for x in range(len(grp)):
        if grp.loc['Team_location',x] == team_location:
            print(grp.loc)
        else:
            print('not the same location')
    
    for grp in grps:    # Loops through each group
        for team in grp:
            if team.loc['Team_location'] == team_location:
                print(f'{grp.loc[team,'Team']} has been excluded')
                del grp[grp.loc[team,:]]'''

    gr1 = gr1.iloc[0,:]
    gr2 = gr2.iloc[0,:]
    gr3 = gr3.iloc[0,:]
    gr4 = gr4.iloc[0,:]

    return(gr1,gr2,gr3,gr4)
##########################################################################################################

# This function randomly selects the opponents 
def team_draw(gr1,gr2,gr3,gr4, team):
    # gr1 , gr2 ,gr3 and gr4 in this case should be lists and not a dataframe
    gr1.iloc[:,0].to_list()
    gr2.iloc[:,0].to_list()
    gr3.iloc[:,0].to_list()
    gr4.iloc[:,0].to_list()

    # team is a string 
    #del gr1[gr1.index(team)]
    opponents = []
    my_grps = (gr1,gr2,gr3,gr4)
    # random team no selection
    for grp in my_grps:
        team1 = random.choice(grp.iloc[:,0])    # Select a random team from the group
        #grp.remove(team1)   # Delete the selected team from the group
        opponents.append(team1)   # Add the selected team into the list of opposition for the selected team
        team2 = random.choice(grp.iloc[:,0])   # Select a second team from the group. Each team must play 2 teams from each group
        #grp.remove(team2)
        opponents.append(team2)
    
    return (opponents)

def matchschedule(matches):
    matches 

    return matches

def opposition_selection(gr1,gr2,gr3,gr4):
    # Converting the groups into a list 
    gr1_list = gr1.iloc[:,0].to_list()   
    gr2_list = gr2.iloc[:,0].to_list()
    gr3_list = gr3.iloc[:,0].to_list()
    gr4_list = gr4.iloc[:,0].to_list()

    # List of groups 
    grps = (gr1_list, gr2_list, gr3_list, gr4_list)
    
    # Selection must be done for each groups set of teams 
    for grpi in grps:
        #Selection must be done with each team in the group
        print(grpi)
        print('\n\n')
        '''len_grp = 9 
        while len_grp >= 3:
            (team_select, select_location, grpi) = team_selection(grpi)
            (team_opponents) = team_draw(gr1,gr2,gr3,gr4, team_select)
            print(f'The {team_select} opponents are {team_opponents}')     
            len_grp = len(grpi)'''

    return
 
# League teams group stage draw for opposition
#league_team()   # Input team in the league
(teams_df) = read_teams()    # Put the team information into a DataFrame 
(teams_df,pot1, pot2, pot3, pot4,games) = league_groups(teams_df)    # Split teams into 4 groups by team points
(home, away) = home_away(pot1, pot2, pot3, pot4)
(team_select, select_location, pot1) = team_selection(pot1)  # Select a random team from pot 1 
print(team_select)
print(pot1)
print(len(pot1))
(team_opponents) = team_draw(pot1,pot2,pot3,pot4, team_select)
print(team_opponents)

opposition_selection(pot1,pot2,pot3,pot4)
#(pot1, pot2, pot3, pot4) = same_loc(select_location, pot1, pot2, pot3, pot4)  # Search all pots to exculde any teams from the same location 
#(team_opponents) = team_draw(pot1,pot2,pot3,pot4, team_select)   # Select a team from each pot for home opposition and another for away opposition 

# Work out exclusions then if the team returned is one of those search for the next team 