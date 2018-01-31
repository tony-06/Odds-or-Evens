from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from random import randint


class Applet:
    def __init__(self):
        self.root = Tk()
        self.root.title('Odds or Evens?')

        self.main_frame = Frame(self.root)
        self.main_frame.grid(sticky=(N, S, E, W))

        self.game_frame = Frame(self.main_frame)
        self.game_frame.grid(row=1, columnspan=4, rowspan=5)

        self.guess_label = Label(self.game_frame, text='Guess a number 0-100:')
        self.guess_label.grid(row=1, padx=8)

        self.user_integer = getint()
        self.user_entry = Entry(self.game_frame, textvariable=self.user_integer)
        self.user_entry.grid(row=2, padx=8)

        self.user_bet = BooleanVar()
        self.bet_even = Radiobutton(self.game_frame, text='Even', variable=self.user_bet, value=True)
        self.bet_even.grid(column=1, row=1, sticky='w')
        self.bet_odd = Radiobutton(self.game_frame, text='Odd', variable=self.user_bet, value=False)
        self.bet_odd.grid(column=1, row=2, sticky='w')

        self.bet_button = Button(self.game_frame, text='Bet', command=self.submit_bet, width=16)
        self.bet_button.grid(row=3)

        self.hidden_var_label = Label(self.game_frame, text='Hidden number :')
        self.hidden_var_label.grid(column=3, row=1, sticky='e')
        self.hidden_var = Label(self.game_frame, text='???')
        self.hidden_var.grid(column=4, row=1, padx=16)

        self.total_sum_label = Label(self.game_frame, text='Total sum :')
        self.total_sum_label.grid(column=3, row=2, sticky='e')
        self.total_sum = Label(self.game_frame, text='???')
        self.total_sum.grid(column=4, row=2)

        self.wins_label = Label(self.game_frame, text='Wins :\nLosses :')
        self.wins_label.grid(column=1, row=5, rowspan=2, pady=8)
        self.wins = 0
        self.losses = 0

        self.win_update = Label(self.game_frame)
        self.win_loss_tag = ttk.Label(self.game_frame)

        self.name = simpledialog.askstring(title='New Player', prompt='What is your name?',
                                           parent=self.root, initialvalue='Player')
        self.main_frame.mainloop()

    def is_even(self, x):
        if x % 2 == 0:
            return True
        else:
            return False

    def get_hidden_var(self):
        return randint(0, 100)

    def keep_score(self):
        return self.wins, self.losses

    def submit_bet(self):
        hidden_variable = self.get_hidden_var()
        bet = self.user_bet.get()
        try:
            player_var = int(self.user_entry.get())
        except ValueError:
            return
        if player_var < 101:
            game_sum = hidden_variable + player_var
            if (bet and self.is_even(game_sum)) or (not bet and not self.is_even(game_sum)):
                self.wins += 1
                self.win_loss_tag = ttk.Label(self.game_frame, text='{} Wins!!!'.format(self.name))
                self.win_loss_tag.grid(row=6)
            else:
                self.losses += 1
                self.win_loss_tag = ttk.Label(self.game_frame, text='{} Loses!!!'.format(self.name))
                self.win_loss_tag.grid(row=6)
            self.hidden_var = Label(self.game_frame, text=hidden_variable)
            self.hidden_var.grid(column=4, row=1, padx=16)
            self.total_sum = Label(self.game_frame, text=game_sum)
            self.total_sum.grid(column=4, row=2)
            self.win_update = Label(self.game_frame, text='{}\n{}'.format(self.keep_score()[0],
                                                                          self.keep_score()[1]))
            self.win_update.grid(column=2, row=5, rowspan=2)


s = Applet()
