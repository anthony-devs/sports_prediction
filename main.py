import requests

def get_data():
    data = []
    for page in range(50, 101):
        print(page)
        req = requests.get(f"https://livescore-api.com/api-client/scores/history.json?secret=0y47cplQEANga3Td1co6LheVEZrTyv2y&page={page}&competition_id=2&package_id=4&key=3Xjb4yS8amKwfz39")
        dat = req.json()
        data.append(dat)
    return data


def probability():
    # Given teams
    team_a = input("Team A [HOME]: ")
    team_b = input("Team B [AWAY]: ")

    # Initialize variables to store goals
    matches_played_between = 0
    team_a_goals_scored = 0
    team_b_goals_scored = 0
    team_a_matches_won = 0
    team_b_matches_won = 0

    # Sample data of matches
    data = get_data()
    

    # Loop through matches to calculate goals
    for season in data:
        matches = season["data"]["match"]
        for match in matches:
            home_team = match["home_name"]
            away_team = match["away_name"]
            ft_score = match["ft_score"]
            status = match["status"]
            
            # Check if the match involves both specified teams and is finished
            if team_a in [home_team, away_team] and team_b in [home_team, away_team] and status == "FINISHED":
                matches_played_between += 1
                home_goals, away_goals = map(int, ft_score.split(" - "))
                if home_team == team_a:
                    team_a_goals_scored += home_goals
                    team_b_goals_scored += away_goals
                    if home_goals > away_goals:
                        team_a_matches_won += 1
                    elif home_goals < away_goals:
                        team_b_matches_won += 1
                else:
                    team_b_goals_scored += home_goals
                    team_a_goals_scored += away_goals
                    if away_goals > home_goals:
                        team_a_matches_won += 1
                    elif away_goals < home_goals:
                        team_b_matches_won += 1
    

    
        # Print results
    #print(f"Matches played between {team_a} and {team_b}: {matches_played_between}")
    #print(f"{team_a} goals scored: {team_a_goals_scored}")
    #print(f"{team_b} goals scored: {team_b_goals_scored}")
    #print(f"{team_a} matches won: {team_a_matches_won}")
    #print(f"{team_b} matches won: {team_b_matches_won}")
    prob = (((team_a_matches_won / matches_played_between) * 2) / matches_played_between)
    winA = team_a_matches_won / matches_played_between
    winB = team_b_matches_won / matches_played_between
    
    print(f'{team_a} won: {team_a_matches_won}')
    print(f"{team_a} 1 of {matches_played_between} [win rate]: { winA * 100}%")
    print(f'{team_a} 0 of 1 [MISS RATE]: {(1- winA) * 100}% ')
    if team_a_matches_won == 0:
        print(f'{team_a} 1 of 1 [Probability]: 0.0%')
    else:
        print(f'{team_a} 1 of 1 [Probability]: {(((matches_played_between - team_a_matches_won) / matches_played_between)) * 100}%')

    print(f'{team_b} won: {team_b_matches_won}')
    print(f"{team_b} 1 of {matches_played_between} [win rate]: { winB * 100}%")
    print(f'{team_b} 0 of 1 [MISS RATE]: {(1- winB) * 100}% ')
    if team_b_matches_won == 0:
        print(f'{team_b} 1 of 1 [Probability]: 0.0%')
    else:
        print(f'{team_b} 1 of 1 [Probability]: {(((matches_played_between - team_b_matches_won) / matches_played_between)) * 100}%')
    
    
    print(f" [{team_a}] - Has a {(((matches_played_between - team_a_matches_won) / matches_played_between)) * 100}% Chance to win \n [{team_b}] - Has a {(((matches_played_between - team_b_matches_won) / matches_played_between)) * 100}% Chance to win")
    if team_a_matches_won or team_b_matches_won == 0:
        print("UNCERTAIN!!!")
    else:
        if {(((matches_played_between - team_a_matches_won) / matches_played_between)) * 100} > {(((matches_played_between - team_b_matches_won) / matches_played_between)) * 100}:
            print(f"{team_a} is likely to win {team_b} in a next match")
        elif {(((matches_played_between - team_a_matches_won) / matches_played_between)) * 100} < {(((matches_played_between - team_b_matches_won) / matches_played_between)) * 100}:
            print(f"{team_b} is likely to win {team_a} in a next match")
        elif {(((matches_played_between - team_a_matches_won) / matches_played_between)) * 100} == {(((matches_played_between - team_b_matches_won) / matches_played_between)) * 100}:
            print("It's probably a draw")


probability()
#get_data()