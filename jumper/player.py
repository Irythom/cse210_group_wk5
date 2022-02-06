import random

class Player:
    """The class for the guesser. This class is in charge of generating the word
    as well as checking the guesses the user makes. 
    Stereotype:
        Information Holder
    Attributes:
        word ( string ): Holds the randomly generated five letter word.
        guess_letter ( char ): stores the current guessed letters.
    """
    def __init__( self ):
        """Class constructor. Declares and initializes instance attributes.
        Args:
            self ("Guesser ): An instance of Guesser.
        """
        self.word = ""
        self.guess_letter = [ "_", "_", "_", "_", "_"]
    
    def generate_word( self ):
        """Generates word that will be guessed.
        Args:
            self ( Guesser ): An instance of Guesser.
        """
        word_list = [ "smile", "angry", "ramen", "towel", "tiger", "whale", "fruit", "grape", "syrup" ]
        random_number = random.randint( 1, len( word_list ) - 1)
        self.word = word_list[ random_number ]

    def check_guess( self, letter ):
        """Checks the user's current guess. 
        Args:
            self ( Guesser ): An instance of Guesser.
            letter ( char ): The letter from the user.
        Returns:
            boolean: True or false whether or not the guess is correct. 
        """
        if letter in self.word:
            location = self.word.index( letter )
            self.guess_letter[ location ] = letter
            return True
        else:
            return False
    
    def check_word( self ):
        """Checks if the user has gotten the whole word.
        Args:
            self (Guesser): An instance of Guesser.
        Returns:
            boolean: True or false depending on whether the user has gotten the word.
        """
        check_word = ""
        for i in self.guess_letter:
            check_word += i
        if self.word == check_word:
            return True
        else:
            return False
    
    def return_guess( self ):
        """This just returns the current guess as it stands.
        Args:
            self ( Guesser ): An instance of Guesser.
        Returns:
            string: The current guess as it now stands.
        """
        return self.guess_letter