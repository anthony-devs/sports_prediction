import requests
import asyncio
import aiohttp
    

def get_data():
    data = []
    for page in range(50, 101):
        print(page)
        url = f"https://livescore-api.com/api-client/scores/history.json?secret=0y47cplQEANga3Td1co6LheVEZrTyv2y&page={page}&competition_id=2&package_id=4&key=3Xjb4yS8amKwfz39"
        response = requests.get(url)
    data.append(response.json())
    return data

games_data = get_data()
async def probability():
    # Given teams
    team_a = input("Team A [HOME]: ")
    team_b = input("Team B [AWAY]: ")

    if(team_a == "q" or team_b == "q"):
        exit(0)
    else:
        # Initialize variables to store goals
        matches_played_between = 0
        team_a_goals_scored = 0
        team_b_goals_scored = 0
        team_a_matches_won = 0
        team_b_matches_won = 0
        a_PROBABILITY = 0
        b_PROBABILITY = 0
        # Sample data of matches
        
        

        # Loop through matches to calculate goals
        for season in games_data:
            matches = season["data"]["match"]
            for match in matches:
                home_team = match["home_name"]
                away_team = match["away_name"]
                ft_score = match["ft_score"]
                status = match["status"]
                
                # Check if the match involves both specified teams and is finished
                if  str(home_team).__contains__(team_a) or str(away_team).__contains__(team_a) and str(home_team).__contains__(team_b) or str(away_team).__contains__(team_b) and status == "FINISHED":
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

        if matches_played_between == 0:
            print("THERE HAS NEVER BEEN A MATCH PLAYED BETWEEN THEM \nTHIS MATCH IS HISTORY IN THE MAKING!!!")
        a_PROBABILITY = ((team_a_matches_won)/(matches_played_between - team_a_matches_won)) * matches_played_between
        b_PROBABILITY = ((team_b_matches_won)/(matches_played_between - team_b_matches_won)) * matches_played_between
        winA = team_a_matches_won / matches_played_between
        winB = team_b_matches_won / matches_played_between
        
        print(f'{team_a} won: {team_a_matches_won}')
        print(f"{team_a} 1 of {matches_played_between} [win rate]: {(winA * 100):.2f}%")
        print(f'{team_a} 0 of 1 [MISS RATE]: {((1- winA) * 100):.2f}% ')
        print(f'{team_a} 1 of 1 [Probability]: {a_PROBABILITY:.2f}')
        print(f'{team_a} is most likely to score over {(team_a_goals_scored/matches_played_between):.2f} goals')

        print("\n \n \n")

        print(f'{team_b} won: {team_b_matches_won}')
        print(f"{team_b} 1 of {matches_played_between} [win rate]: { (winB * 100):.2f}%")
        print(f'{team_b} 0 of 1 [MISS RATE]: {((1 - winB) * 100):.2f}% ')
        print(f'{team_b} 1 of 1 [Probability]: {b_PROBABILITY:.2f}')
        print(f'{team_b} is most likely to score over {(team_b_goals_scored/matches_played_between):.2f} goals')
        if a_PROBABILITY == 0:
            print(f"{team_b} has a 100% chance of winning in a next match")
        elif b_PROBABILITY == 0:
            print(f"{team_a} has a 100% chance of winning in a next match")
        else:
            if a_PROBABILITY < b_PROBABILITY:
                print(f"{team_b} has a {((a_PROBABILITY / b_PROBABILITY) * 100):.2f}% chance of winning in a next match")
                print(f"The odds are: {team_b} - {(b_PROBABILITY / a_PROBABILITY):.2f}")
            elif a_PROBABILITY > b_PROBABILITY:
                print(f"{team_a} has a {(b_PROBABILITY / a_PROBABILITY) * 100}% chance of winning in a next match")
                print(f"The odds are: {team_a} - {(a_PROBABILITY / b_PROBABILITY):.2f}")

            else:
                print("the chances are 50/50, there may be a draw")
        prompt = input("Do You Want Another? : ")
        if prompt == "yes":
            probability()
        else:
            exit()
        


asyncio.run(probability())
#get_data()