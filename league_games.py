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

            # Convert team points to an integer and handle any errors
            try:
                points = int(temp[2])
                team_points.append(points)  # Add the teams points into the team points list
            except ValueError:
                print(f"Warning: Invalid team points '{temp[2]}' for team '{temp[0]}'. Defaulting to 0.")
                team_points.append(0)  # Add a default value if conversion fails 

    # Create a dictionary of team info lists
    team_info = {'Team': team,
                 'Team_location': team_location, 
                 'Team_points': team_points}
    
    df = pd.DataFrame(team_info)    # Convert the team info into a DataFrame
    print(df.dtypes)
    return(df)


# This function splits the teams in the league into 4 groups 
def league_groups(df):
    print(df.dtypes)
    # df is the teams_list 
    df['Team_points'] = pd.to_numeric(df['Team_points'])
    # sort teams by team points 
    df = df.sort_values('Team_points') 

    # split the sorted list into four groups 
    gr1 = df.iloc[0:8,:]    # group 1
    gr2 = df.iloc[9:17,:]    # group 2
    gr3 = df.iloc[18:26,:]    # group 3
    gr4 = df.iloc[27:35,:]    # group 4

    print('Group 1' + gr1 + '\n')
    print('Group 2' + gr2 + '\n')
    print('Group 3' + gr3 + '\n')
    print('Group 4' + gr4 + '\n')
 
    return(df,gr1, gr2, gr3, gr4)


# This function selects a random team from the specified group
def team_selection(grp):
    # random team no selection
    len(grp)
    x = random.randint(len-1)
    team = grp.iloc[x,:]
    del grp[team]

    return(team, grp)


# This function identifies teams in the same location and excludes them for the team
def same_loc(team_location, gr1, gr2, gr3, gr4): 
    grps = (gr1, gr2, gr3, gr4)
    mygr1 ={}
    # identify team location
    # identify teams in that location 
    for grp in grps:
        for team in grp:
            if grp.loc[team,'Team_location'] == team_location:
                print(f'{grp.loc[team,'Team']} has been excluded')
                del grp[grp.loc[team,:]]

    return(gr1,gr2,gr3,gr4)


# This function randomly selects the selcted teams opponents 
def team_draw(gr1,gr2,gr3,gr4, team):
    opponents = []
    my_grps = (gr1,gr2,gr3,gr4)
    # random team no selection
    for grp in my_grps:
        len(grp)
        x = random.randint(len-1)
        team1 = grp[x]
        del grp[team]
        opponents.append(team1)
        y = random.randint(len-2)
        team2 = grp[y]
        del grp[team]
        opponents.append(team2)
    
    return (opponents)


# League teams group stage draw for opposition
#league_team()    #Input team in the league
(teams_df) = read_teams()    # Put the team information into a DataFrame 
(teams_df,pot1, pot2, pot3, pot4) = league_groups(teams_df)    # Split teams into 4 groups by team points
'''pots = [pot1, pot2, pot3, pot4]
for pot in pots:
    current_pot = pot
    for team_in_pot  in pot:
        (selected_team,my_potx) = team_selection(current_pot)
        (mypot1,mypot2,mypot3,mypot4) = same_loc(selected_team[1], pot1, pot2, pot3, pot4)
        (team_opps) = team_draw(mypot1,mypot2,mypot3,mypot4, selected_team)'''

