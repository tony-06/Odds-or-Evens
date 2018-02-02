from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import random


class App:
    """This class is going to hold all of the display buttons and variables
    as well as all of the methods to update them onscreen"""

    def __init__(self):
        self.root = Tk()
        self.root.title('Odds or Evens?')
        self.root.lower()
        self.main_frame = ttk.Frame(self.root, padding=(10, 5))
        self.main_frame.grid(column=0, row=0, columnspan=2, rowspan=4, sticky=(N, S, E, W))
        self.main_frame.columnconfigure(0)
        self.main_frame.rowconfigure(0)
        self.game_frame = ttk.Frame(self.main_frame, padding=8)
        self.game_frame.grid(column=0, row=1, columnspan=2, rowspan=3)
        self.name = simpledialog.askstring(title='New player', prompt='What is your name?',
                                           parent=self.game_frame, initialvalue='player')
        self.name = self.name.capitalize()
        self.entry_label = ttk.Label(self.game_frame, text='Guess a number:', font=('helvetica', 14))
        self.entry_label.grid(column=0, row=1, padx=10)
        self.bet_button = ttk.Button(self.game_frame, text="Bet", default='active', width=22)
        self.bet_button.grid(column=1, row=2, columnspan=2)
        self.odd_or_even = BooleanVar()
        self.radio_frame = ttk.Labelframe(self.game_frame)
        self.radio_frame.grid(column=1, row=1, rowspan=1, sticky=(N, S))
        self.user_guess_odd = ttk.Radiobutton(self.radio_frame, text='Odd',
                                              variable=self.odd_or_even, value=False)
        self.user_guess_odd.grid(column=0, row=0, pady=8, padx=5)
        self.user_guess_even = ttk.Radiobutton(self.radio_frame, text='Even',
                                               variable=self.odd_or_even, value=True)
        self.user_guess_even.grid(column=0, row=1, pady=8, padx=5)
        self.user_integer = getint()
        self.user_entry = ttk.Entry(self.game_frame, textvariable=self.user_integer, width=18, takefocus=True)
        self.user_entry.grid(column=0, row=2, sticky=(N, S, E, W), pady=8, padx=12)
        self.user_entry.focus()
        self.update_hidden_var('     ???', '')
        self.update_win_loss()
        self.update_win_loss_count()

    def update_hidden_var(self, hidden_var, game_sum):
        a = '\nHidden Number : \n{:5}\n\nTotal sum : \n{:5}'.format(hidden_var, game_sum)
        variable_display = ttk.Label(self.game_frame,
                                     text=a)
        variable_display.grid(column=2, row=1, padx=10)

    def update_win_loss(self, result=None):
        if result == True:
            win_loss_label = ttk.Label(self.main_frame, text='{} Won!!'.format(self.name))
            win_loss_label.grid(column=0, row=4, columnspan=1)
        elif result == False:
            win_loss_label = ttk.Label(self.main_frame, text='{} Lost!!'.format(self.name))
            win_loss_label.grid(column=0, row=4, columnspan=1)

    def update_win_loss_count(self, result=(0, 0)):
        score_box = ttk.Label(self.main_frame,
                              text='Wins : {:5>} \n\nLosses : {:5>}\n'.format(result[0], result[1]))
        score_box.grid(column=1, row=4)


class Game(App):
    """Game functions"""

    def __init__(self):
        App.__init__(self)
        self.wins = 0
        self.losses = 0
        self.bet_button = ttk.Button(self.game_frame,
                                     text="Bet",
                                     command=self.submit_bet,
                                     default='active', width=22)
        self.bet_button.grid(column=1, row=2, columnspan=2)
        self.root.mainloop()

    def is_even(self, x):
        if x % 2 == 0:
            return True
        else:
            return False

    def get_hidden_var(self):
        return random.randint(0, 100)

    def _keep_score(self):
        return self.wins, self.losses

    def submit_bet(self):
        hidden_var = self.get_hidden_var()
        oe = self.odd_or_even.get()
        ue = self.user_entry.get()
        try:
            int(ue)
        except ValueError:
            return
        if int(ue) < 101:
            game_sum = hidden_var + int(ue)
            if (oe and self.is_even(game_sum)) \
                    or (not oe and not self.is_even(game_sum)):
                self.wins += 1
                self.update_win_loss(True)
            else:
                self.losses += 1
                self.update_win_loss(False)
            self.update_hidden_var(hidden_var, game_sum)
        w, l = self._keep_score()
        self.update_win_loss_count((w, l))


start = Game()
