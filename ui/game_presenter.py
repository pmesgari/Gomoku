from business_rules.board import Player


class GamePresenter:
    player_turn_names = {
        Player.White: "White's Turn",
        Player.Black: "Black's Turn",
        Player.Empty: "Tilt"
    }

    win_status_strings = {
        Player.White: "White Wins!",
        Player.Black: "Black Wins!",
        Player.Empty: "Tilt"
    }

    def get_player_status(self, player):
        return self.player_turn_names[player]

    def get_win_status(self, player):
        return self.win_status_strings[player]