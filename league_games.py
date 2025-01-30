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

    #print(df.dtypes)  # Printing the data types 
    return(df)


# This function splits the teams in the league into 4 groups 
def league_groups(df):

    # df is the teams_list 
    df['Team_points'] = pd.to_numeric(df['Team_points'])
    # sort teams by     team points 
    df = df.sort_values(by='Team_points', ascending=False).reset_index(drop=True) 
    df['Group'] = df['Team_points']

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
    
    # Printing the groups
    '''print('Group 1:\n' , gr1 , '\n')
    print('Group 2:\n' , gr2 , '\n')
    print('Group 3:\n' , gr3 , '\n')
    print('Group 4:\n' , gr4 , '\n')'''
 
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


 
# League teams group stage draw for opposition
#league_team()   # Input team in the league
(teams_df) = read_teams()    # Put the team information into a DataFrame 
(teams_df,pot1, pot2, pot3, pot4) = league_groups(teams_df)    # Split teams into 4 groups by team points

fixtures = pd.DataFrame(index=list(teams_df['Team']) ,columns=['Group','Gr1_home','Gr1_away','Gr2_home','Gr2_away','Gr3_home', 'Gr3_away','Gr4_home' ,'Gr4_away'])
for i in teams_df['Team']:
    k = teams_df[teams_df['Team'] == i].index
    fixtures.loc[i,'Group'] = teams_df.iloc[k[0],-1]

#print(fixtures)
opps = team_draw(pot1,pot2,pot3,pot4, 'RMI')
opps.insert(0,1)


#print(opps)

fixtures.loc['RMI'] = opps
#print(fixtures)


#team_fixtures(pot1,pot2,pot3,pot4,teams_df )

print(fixtures)

# Allocating each group to a home and away list 
gr1_h = pot1.iloc[:,0].copy().to_list()
gr1_a = pot1.iloc[:,0].copy().to_list()
gr2_h = pot2.iloc[:,0].copy().to_list()
gr2_a = pot2.iloc[:,0].copy().to_list()
gr3_h = pot3.iloc[:,0].copy().to_list()
gr3_a = pot3.iloc[:,0].copy().to_list()
gr4_h = pot4.iloc[:,0].copy().to_list()
gr4_a = pot4.iloc[:,0].copy().to_list()

x = fixtures.loc['RMI','Gr2_home']
print(x)
fixtures.loc[x,'Gr1_away'] = 'RMI'

matchups = fixtures.columns.to_list()  # A list of the columns names of the fixtures dataframe
mathcups = matchups.remove('Group')   # Creating a list of the matchups of the fixtures  

for team in teams_df['Team']:
    grp_no = fixtures.loc[team,'Group']
    team_grp = ''.join(['Gr', grp_no])
    print(team_grp )

    for col in matchups:
        if pd.isna(fixtures.loc[team,col]):
            if col == 'Gr1_home':
                x = gr1_h
                y = 'h'
            elif col == 'Gr1_away':
                x = gr1_a
                y = 'a'
            elif col == 'Gr2_home':
                x = gr2_h
                y = 'h'
            elif col == 'Gr2_away':
                x = gr2_a
                y = 'a'
            elif col == 'Gr3_home':
                x = gr3_h
                y = 'h'
            elif col == 'Gr3_away':
                x = gr3_a
                y = 'a'
            elif col == 'Gr4_home':
                x = gr4_h
                y = 'h'
            else:
                x = gr4_a
                y = 'a'                

            opp_team = random.choice(x)
            fixtures.loc[team,col] = opp_team
            
   



print(fixtures)