from terminal_service import Terminal_service
from player import Player
from parachute import Parachute


class Director:
    """The responsibility of the director is to control how the game is played.

    Stereotype:
        Controller
    Attributes:
        console ( Console ): An instance of the class of objects known as Console.
        keep_playing ( boolean ): Whether or not the game can continue.
        word_guessed ( boolean ): Whether or not the word has been guessed.
        parachute ( array ): The status of the parachute.
        current_guess ( string ): The current amount of letters guessed.
        letter ( char ): The letter from the user. 
        jumper ( Jumper ): An instance of the class of objects known as Jumper.
        guesser ( Guesser ): An instance of the class of objects known as Guesser.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._console = Terminal_service()
        self._jumper = Parachute()
        self._guesser = Player()
        self._keep_playing = True
        self._word_guessed = False
        self._parachute = self._jumper.return_parachute()
        self._current_guess = self._guesser.return_guess()
        self._letter = ""

    def start_game(self):
        """Starts the game loop to control how the game is played.

        Args:
            self ( Director ): an instance of Director.
        """
        self._guesser.generate_word()
        self._guesser.generate_lines()
        self._do_outputs()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this instance it means
        getting a letter from the user.
        Args:
            self ( Director ): An instance of Director.
        """
        self._letter = self._console.get_letter()

    def _do_updates(self):
        """Updates the important game information for each round of play. In this case
        that means checking the parachute and cutting off part if user guess is wrong.
        As well as keeping track of correct guesses and updating the current word.
        Args:
            self ( Director ): An instance of Director.
        """
        good_parachute = self._jumper.check_parachute()
        if good_parachute == True and self._word_guessed == False:
            letter = self._letter
            valid_guess = self._guesser.check_guess(letter)
            self._current_guess = self._guesser.return_guess()
            self._jumper.cut_parachute(valid_guess)
            self._parachute = self._jumper.return_parachute()
            self._word_guessed = self._guesser.check_word()
        elif good_parachute == False:
            self._keep_playing = False
        if self._word_guessed == True:
            self._keep_playing = False

    def _do_outputs(self):
        """Outputs the important game information for each round of play. Such as the current word
        and the status of the jumper.
        Args:
            self ( Director ): An instance of Director.
        """
        self._console.display_guess(self._current_guess)
        self._console.display_parachute(self._jumper.parachute)
