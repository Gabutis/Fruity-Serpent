import pickle


class Leaderboard:
    def __init__(self):
        self.scores = []

    def add_score(self, player_name, score):
        if player_name.strip() != "" and score > 0:
            for entry in self.scores:
                if entry["player_name"] == player_name:
                    if score > entry["score"]:
                        entry["score"] = score
                    return

            entry = {"player_name": player_name, "score": score}
            self.scores.append(entry)
            self.scores = sorted(self.scores, key=lambda x: x["score"], reverse=True)[
                :15
            ]


def save_leaderboard(leaderboard):
    with open(".leaderboard_data.pickle", "wb") as file:
        pickle.dump(leaderboard, file)


def load_leaderboard():
    try:
        with open(".leaderboard_data.pickle", "rb") as file:
            leaderboard = pickle.load(file)
    except FileNotFoundError:
        leaderboard = Leaderboard()
    return leaderboard
