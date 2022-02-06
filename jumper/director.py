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
    def __init__( self ):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Terminal_service()
        self.jumper = Parachute()
        self.guesser = Player()
        self.keep_playing = True
        self.word_guessed = False
        self.parachute = self.jumper.return_parachute()
        self.current_guess = self.guesser.return_guess()
        self.letter = ""
        
    def start_game( self ):
        """Starts the game loop to control how the game is played.
        
        Args:
            self ( Director ): an instance of Director.
        """
        self.guesser.generate_word()
        self.do_outputs()
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs( self ):
        """Gets the inputs at the beginning of each round of play. In this instance it means
        getting a letter from the user.
        Args:
            self ( Director ): An instance of Director.
        """
        self.letter = self.console.get_letter()

    def do_updates( self ):
        """Updates the important game information for each round of play. In this case
        that means checking the parachute and cutting off part if user guess is wrong.
        As well as keeping track of correct guesses and updating the current word.
        Args:
            self ( Director ): An instance of Director.
        """
        good_parachute = self.jumper.check_parachute()
        if good_parachute == True and self.word_guessed == False:
            letter = self.letter
            valid_guess = self.guesser.check_guess( letter )
            self.current_guess = self.guesser.return_guess()
            self.jumper.cut_parachute( valid_guess )
            self.parachute = self.jumper.return_parachute()
            self.word_guessed = self.guesser.check_word()
        elif good_parachute == False:
            self.keep_playing = False
        if self.word_guessed == True:
            self.keep_playing = False
        
    def do_outputs( self ):
        """Outputs the important game information for each round of play. Such as the current word
        and the status of the jumper.
        Args:
            self ( Director ): An instance of Director.
        """
        self.console.display_guess( self.current_guess )
        self.console.display_parachute( self.jumper.parachute )