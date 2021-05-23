import json

def get_all_players_score():
    score_board = open('score_board.json', 'r')
    return json.load(score_board)


def get_player_score(player_name):
    players_scores = get_all_players_score();
    if player_name in players_scores:
        return players_scores[player_name]
    return 0


def update_player_score(player_name, score):
    players_scores = get_all_players_score();
    players_scores[player_name] = score
    score_board = open('score_board.json', 'w')
    json.dump(players_scores, score_board, indent=4)


def print_all_players_scores():
    print("All Players Score::")
    players_scores = get_all_players_score();
    print(json.dumps(players_scores, indent=4))



def get_top_10_players():
    top_10_players = open('top_10_players.json', 'r')
    return json.load(top_10_players)


def update_top_10_player_list(player_name, player_score):
    top_10_players = get_top_10_players()
    if len(top_10_players) < 10 or player_name in top_10_players:
        top_10_players[player_name] = player_score
        update_top_10_player_scores(top_10_players)
        return 0

 
    min_score_player_name = get_player_with_minimun_score(top_10_players)
    if top_10_players[min_score_player_name] < player_score:
        del top_10_players[min_score_player_name]
        top_10_players[player_name] = player_score
        update_top_10_player_scores(top_10_players)


def update_top_10_player_scores(updated_top_10_player_list):
    top_10_players = open('top_10_players.json', 'w')
    json.dump(updated_top_10_player_list, top_10_players, indent=4)


def get_player_with_minimun_score(top_10_players):    
    min_score=min([value for key,value in top_10_players.items()])
    for key,value in top_10_players.items():
        if value==min_score:
            return key        


def print_top_10_players():
    print ("Top 10 Players::")
    top_10_players = get_top_10_players()
    print(json.dumps(top_10_players, indent=4))

if __name__ == "__main__":
    #update_top_10_player_list(Naresh,10)
    print(get_player_with_minimun_score(get_top_10_players()))
