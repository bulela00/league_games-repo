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
        # Write the default contents onto the teams.txt file 
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

    # Convert team points column into numeric values
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


def team_fixtures(gr1,gr2,gr3,gr4,df):
    grps = (gr1,gr2,gr3,gr4)    # Create a list of the grps             
    for grp in grps:    # Looping through the groups

        while grp.shape[0] > 0: 
            (selected_team, selected_location) = team_selection(grp)  # Select a random team from pot 1 
            indexTeam = grp[grp['Team'] == selected_team].index
            grp.drop(indexTeam, inplace=True)     # Remove the selected team from the group returned by the function
            # (opps)=team_draw(gr1,gr2,gr3,gr4, selected_team)
            #print(f'Selected Team: {selected_team}')
            #print(f'Opposition: {opps}')
        #print('\n\n\n\n')
        #print(f'Remaining group: {grp}')


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

               

def group_selection(grp_no, gr1, gr2, gr3, gr4): 
    # Allocating each group to a list 

    if grp_no[2] == '1' :
        x = gr1 

    elif grp_no[2] == '2':
        x = gr2

    elif grp_no[2] == '3':
        x = gr3

    elif grp_no[2] == '4':
        x = gr4
    
    return(x)

def opp_check(team, team_grp, opp, curr_col, current_schedule ):
    # This function is used to check if the team drawn as opposition is available for the fixture
    opp # This is the opposition team being investigated
    if curr_col[4] == 'h':
        opp_col = "_".join([team_grp,"away"]) # Variable used to check the opponenants availability
    else:
        opp_col = "_".join([team_grp,"home"])
    
    print(f'opp_col : {opp_col}')

    if pd.isna(current_schedule.loc[opp,opp_col]) :   # Check if the match is open
        if team not in current_schedule.loc[opp].values:  # If the teams haven't already been matched up
            current_schedule.loc[opp,opp_col] = team
            current_schedule.loc[team,curr_col] = opp
        else :
            print('Redraw')

    
    else:         
        print('Redraw')
        




    
    

def schedule(gr1,gr2,gr3,gr4,fixtures, teams_df):

    matches = ['Gr1_home','Gr1_away','Gr2_home','Gr2_away','Gr3_home', 'Gr3_away','Gr4_home' ,'Gr4_away'] # A list of columns fixture df
    
    # Loop through all the teams in teams_df 
    for team in gr1['Team']:
        grp_no = fixtures.loc[team,'Group']   # Get the group number for team 
        team_grp = ''.join(['Gr', str(grp_no)])   # Add 'Gr' in front of the number as a string 

        # Loop through the columns excluding the 'Group' column 
        for col in matches:

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
# Selection between the default data set and input



# read in default.txt league data 
# default_contents used if no new data is given 
default_contents = ""
with open('default.txt', 'r+') as f: # Open the file again, this time using the 'with' syntax
        for line in f:
                default_contents = default_contents + line    


# League teams group stage draw for  opposition
league_team()   # Input teams in the league

(teams_df) = read_teams()    # Put the team information into a DataFrame
print("League teams' information")  
print(teams_df)

(teams_df,pot1, pot2, pot3, pot4) = league_groups(teams_df)    # Split teams into 4 groups by team points

team_list = list(teams_df['Team'])   # Create a new list with all the team names

# Printing the groups
print('\nThese are the groups:')  
gr1_list = list(pot1['Team']) # Creates a list of the teams in the group
gr2_list = list(pot2['Team'])
gr3_list = list(pot3['Team'])
gr4_list = list(pot4['Team'])

print('Group 1:')
print(*gr1_list)
print('Group 2:')
print(*gr2_list)
print('Group 3:')
print(*gr3_list)
print('Group 4:')
print(*gr4_list)        

# Create a dataframe for the fixtures in the group stage 
fixtures = pd.DataFrame(index=list(teams_df['Team']) ,columns=['Group','Gr1_home','Gr1_away','Gr2_home','Gr2_away','Gr3_home', 'Gr3_away','Gr4_home' ,'Gr4_away'])

# Add the group number in the 'Group' column in the fixtures dataframe 
for i in teams_df['Team']:
    k = teams_df[teams_df['Team'] == i].index   # Get the index for the team i in the teams_df dataframe 
    fixtures.loc[i,'Group'] = teams_df.iloc[k[0],-1]   # Get the group number for team i using the index found and placed in k   


# Team draw for fixtures

# A team from the entire league is selected at random
while fixtures.isna().any().any():
    team_select = random.choice(team_list)
    team_select_grp = 'Gr' + str(fixtures.loc[team_select,'Group']) 
    fixture_cols = ['Gr1_home','Gr1_away','Gr2_home','Gr2_away','Gr3_home', 'Gr3_away','Gr4_home' ,'Gr4_away']

    col_index = 0
    while col_index < 8: 

        team_col = fixture_cols[col_index]
        grp_list = group_selection(team_col, gr1_list, gr2_list, gr3_list, gr4_list)   # Retrieve the correct group list for column
        while pd.isna(fixtures.loc[team_select,team_col]):
            opp_select = random.choice(grp_list)
            opp_check(team_select, team_select_grp, opp_select, team_col, fixtures)
            #grp_list.remove(opp_select)
        col_index +=1

    team_list.remove(team_select) # Remove team from selection options



#fixtures.loc[team_select]   # Selects the fixtures of the selected team



print(fixtures)



# print(len(team_list)) Confirmation of team left (Condition to stop the for loop)
print('done')