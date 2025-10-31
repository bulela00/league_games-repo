# League opponents draw 
# This project is used to determine the schedule of a sports tournament 
# Each team must face 8 unique opponents. 
# The 8 opponents will be 2 teams from each group 

# Order of operation 
# The qualifying teams information must be input by the user
# The input data must then be sorted by team points and split into groups 

#=======importing libraries=======
import pandas as pd 
import numpy as np
from numpy import random
import math
  
#=======Functions=======
# This function recieves the team information for the teams in the leagues 
def league_team(): 
    # confirmation of no. of teams 
    check = input("Do you have a full list of 36 teams? (Yes or No) ")  

    if len(check) == 3:    # Checking if its a yes or no using length
        teams = ""
        print('Please enter the team information as prompted:')
        for x in range(1,37):
            print(f'Team {x}:')
            # accepts teams' name  
            team_name = input(f"Enter the team name: ")
            # teams' location 
            team_location = input("Enter team location: ")
            # teams' points 36
            team_points = input("Enter the team points: ")
            team_info = ",".join([team_name,team_location,team_points])
            teams = teams + team_info + '\n'
            
        with open('teams.txt', 'w+', encoding='utf-8-sig') as file:
            file.write(teams)
   
    else:  
        with open('teams.txt', 'w+', encoding='utf-8-sig') as file:
            file.write(default_contents)       
        print("The default list of teams will be used \n ")

    return 

# This function splits the league teams into four groups based on the team points
def read_teams(): 
    team_name = []
    team_location = []
    team_points = []
    # Read league teams 
    with open('teams.txt', 'r+', encoding='utf-8-sig') as file: 
        for line in file:
            temp = line.strip()
            temp = temp.split(",")    # Split the line of team info 
            team_name.append(temp[0])    # Add the team name to the team list
            team_location.append(temp[1])    # Add the team location into the locations list
            team_points.append(int(temp[2]))  # Add the teams points into the team points list
 
    # Create a dictionary of team info lists
    team_info = {'Team': team_name,
                 'Team_location': team_location, 
                 'Team_points': team_points}
    
    df = pd.DataFrame(team_info)    # Convert the team info into a DataFrame

    return(df)


# This function splits the teams in the league into 4 groups 
def league_groups(df):

    # df is the teams_list 
    df['Team_points'] = pd.to_numeric(df['Team_points'])

    # sort teams by team points 
    df = df.sort_values(by='Team_points', ascending=False).reset_index(drop=True) 
    df['Group'] = df['Team_points']   # Additional column for group number

    # split the sorted list into four groups 
    gr1 = df.iloc[0:9,:].copy()    # group 1
    gr2 = df.iloc[9:18,:].copy()    # group 2
    gr3 = df.iloc[18:27,:].copy()    # group 3
    gr4 = df.iloc[27:36,:].copy()    # group 4

    # Adding the group numbers to the dataframe 
    df.iloc[0:9,-1] = 1
    df.iloc[9:18,-1] = 2
    df.iloc[18:27,-1] = 3
    df.iloc[27:36,-1] = 4
  
    return(df,gr1, gr2, gr3, gr4)


# This function selects a random team from the specified group
def team_selection(grp):
    team = random.choice(grp.iloc[:,0])    # Select a random team from the group
    team_location = grp[grp['Team'] == team]['Team_location'].iloc[0]
    return(team, team_location)

def team_fixtures(gr1,gr2,gr3,gr4,df):
    grps = (gr1,gr2,gr3,gr4)    # Create a list of the grps             
    for grp in grps:    # Looping through the goofs

        while grp.shape[0] > 0: 
            (selected_team, selected_location) = team_selection(grp)  # Select a random team from pot 1 
            indexTeam = grp[grp['Team'] == selected_team].index
            grp.drop(indexTeam, inplace=True)     # Remove the selected team from the group returned by the function
            # (opps)=team_draw(gr1,gr2,gr3,gr4, selected_team)
            #print(f'Selected Team: {selected_team}')
            #print(f'Opposition: {opps}')
        #print('\n\n\n\n')
        #print(f'Remaining group: {grp}')
        

           

# This function identifies teams in the same location and excludes them for the team
def same_loc(location, gr1, gr2, gr3, gr4): 
    grps = (gr1,gr2,gr3,gr4)
    excl_teams = []
    for grp in grps:
        grp.query('Team_location == location', inplace=True) 
        excl_teams.append(grp['Team'])

    return(excl_teams)


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
    i = 0
    for grp in my_grps:
        team1 = random.choice(grp.iloc[:,0])    # Select a random team from the group

        #print(grp.iloc[:,0])
        #grp.remove(team1)   # Delete the selected team from the group
        opponents.append(team1)   # Add the selected team into the list of opposition for the selected team
        team2 = random.choice(grp.iloc[:,0])   # Select a second team from the group. Each team must play 2 teams from each group
        #grp.remove(team2)  

        opponents.append(team2)
  
    
    return (opponents)

def fixture_matchup(gr1,gr2,gr3,gr4,fixtures, teams_df):

    matchups = fixtures.columns.to_list()  # A list of the columns names of the fixtures dataframe
    mathcups = matchups.remove('Group')   # Creating a list of the matchups of the fixtures  
    
    # Loop through all the teams in teams_df 
    for team in gr1['Team']:
        grp_no = fixtures.loc[team,'Group']   # Get the group number for team 
        team_grp = ''.join(['Gr', str(grp_no)])   # Add 'Gr' in front of the number as a string 

        # Loop through the columns excluding the 'Group' column 
        for col in matchups:

            # if the value at row = team and col = col is NaN
            if pd.isna(fixtures.loc[team,col]):
                x = group_selection(col,gr1,gr2,gr3,gr4)   # Return the group corresponding to the column
        
                opp_team = random.choice(x)    # Select a random team from the group in x
                #fixtures.loc[team,col] = opp_team   # Store the randomly selected team in at [team, col]  

                if col[4] == 'a':
                    new_col = ''.join([team_grp, '_home'])
                elif col[4] == 'h':
                    new_col = ''.join([team_grp, '_away'])

                if pd.isna(fixtures.loc[opp_team,new_col]):
                    fixtures.loc[team,col] = opp_team   # Store the randomly selected team in at [team, col] 
                    fixtures.loc[opp_team,new_col] = team   # Add the team on the fixture list for the opposition
                else:
                   
                    continue

               

def group_selection(selection,gr1,gr2,gr3,gr4): 
    # Allocating each group to a list 
    gr1_list = gr1.iloc[:,0].copy().to_list()
    gr2_list = gr2.iloc[:,0].copy().to_list()
    gr3_list = gr3.iloc[:,0].copy().to_list()
    gr4_list = gr4.iloc[:,0].copy().to_list()

    if selection in ('Gr1_home', 'Gr1_away') :
        x = gr1_list 

    elif selection in ('Gr2_home', 'Gr2_away'):
        x = gr2_list

    elif selection in ('Gr3_home', 'Gr3_away'):
        x = gr3_list

    elif selection in ('Gr4_home', 'Gr4_away'):
        x = gr4_list
    
    return(x)



def schedule(gr1,gr2,gr3,gr4,fixtures, teams_df):

    matchups = fixtures.columns.to_list()  # A list of the columns names of the fixtures 
    matchups.remove(matchups[0])   # Creating a list of the matchups of the fixtures
    
    # Loop through all the teams in teams_df 
    for team in gr1['Team']:
        grp_no = fixtures.loc[team,'Group']   # Get the group number for team 
        team_grp = ''.join(['Gr', str(grp_no)])   # Add 'Gr' in front of the number as a string 

        # Loop through the columns excluding the 'Group' column 
        for col in matchups:

            # if the value at row = team and col = col is NaN
            if pd.isna(fixtures.loc[team,col]):
                x = group_selection(col,gr1,gr2,gr3,gr4)   # Return the group corresponding to the column
        
                opp_team = random.choice(x)    # Select a random team from the group in x
                #fixtures.loc[team,col] = opp_team   # Store the randomly selected team in at [team, col]  

                opp_colh = ''.join([team_grp, '_home'])
                opp_cola = ''.join([team_grp, '_away'])

                if col[4] == 'a':
                    opp_col = opp_colh
                elif col[4] == 'h':
                    opp_col = opp_cola

                if pd.isna(fixtures.loc[opp_team,opp_col]):
                    fixtures.loc[team,col] = opp_team   # Store the randomly selected team in at [team, col] 
                    fixtures.loc[opp_team,opp_col] = team   # Add the team on the fixture list for the opposition
                else:
                    continue

                check_nan = fixtures.isnull().values.any()
                print(check_nan)




#=========Operations=======
# read in default league data 
default_contents = ""
with open('default.txt', 'r+') as f: # Open the file again, this time using the 'with' syntax
        for line in f:
                default_contents = default_contents + line               
 
# League teams group stage draw for opposition
league_team()   # Input teams in the league

(teams_df) = read_teams()    # Put the team information into a DataFrame
print("League teams' information")  
print(teams_df)

(teams_df,pot1, pot2, pot3, pot4) = league_groups(teams_df)    # Split teams into 4 groups by team points
# Printing the groups
print('\nThese are the groups:')
print('Group 1:\n' , pot1.drop(['Group'], axis=1) , '\n')
print('Group 2:\n' , pot2.drop(['Group'], axis=1) , '\n')
print('Group 3:\n', pot3.drop(['Group'], axis=1) , '\n')
print('Group 4:\n' , pot4.drop(['Group'], axis=1), '\n')

# Create a dataframe for the fixtures in the group stage 
fixtures = pd.DataFrame(index=list(teams_df['Team']) ,columns=['Group','Gr1_home','Gr1_away','Gr2_home','Gr2_away','Gr3_home', 'Gr3_away','Gr4_home' ,'Gr4_away'])

# Add the group number in the 'Group' column in the fixtures dataframe 
for i in teams_df['Team']:
    k = teams_df[teams_df['Team'] == i].index   # Get the index for the team i in the teams_df dataframe 
    fixtures.loc[i,'Group'] = teams_df.iloc[k[0],-1]   # Get the group number for team i using the index found and placed in k   

# Team draw 
team_list = list(teams_df['Team'])   # Create a new list with the team names
for k in range(36):
    selected_team = random.choice(team_list)   # Select a random team from the team list
    team_list.remove(selected_team) # Remove selected team from team list 
    #print(fixtures.loc[selected_team,:])   # print the randomly selected team 

    # In the match up draw 2 checks must be made 
    # 1. Is there an empty slot in the selected teams schedule? (if there is no opening pass that slot)
    # 2. Does the team drawn already have a team in the spot you would occupy (If the drawn team already has a team then draw a new opponent )
    team_grp = fixtures.loc[selected_team,'Group']
    matches = ['Gr1_home','Gr1_away','Gr2_home','Gr2_away','Gr3_home', 'Gr3_away','Gr4_home' ,'Gr4_away']
    for match in matches:
        opposition = fixtures.loc[selected_team, match]
        if math.isnan(opposition):
            ##fixtures.loc[selected_team, match] = 'newteam'
            if match[2] == '1':
                fixtures.loc[selected_team, match] = 'gr1team'
            elif match[2] == '2':
                fixtures.loc[selected_team, match] = 'gr2team'
            elif match[2] == '3':
                fixtures.loc[selected_team, match] = 'gr3team'
            elif match[2] == '4':
                fixtures.loc[selected_team,match] = 'gr4team'
            
        else:
            break


print(fixtures)


