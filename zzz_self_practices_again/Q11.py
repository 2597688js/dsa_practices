"""
Ask number of games played in a tournament. Ask the user number of
games won and number of games loss. Calculate number of tie and total
Points. (1 win= 4 points, 1 tie =2 points
"""

def calculate_score(total_games:int, won_games:int, lost_games:int) -> (int, int):
    tie_games = total_games - (won_games + lost_games)
    total_points = (won_games * 4) + (tie_games * 2)

    return tie_games, total_points


if __name__ == "__main__":
    total_games = 10
    won_games = 5
    lost_games = 4
    tie_games, total_games= calculate_score(total_games, won_games, lost_games)
    print(f" Tie : {tie_games} , Total score : {total_games}")