class Parachute:
    """This class is in charge of the jumper. It controls the parachute and destroying it
    as the user gets the guesses wrong.
    Stereotype:
        Information holder
    Attributes:
        parachute ( array ): Stores symbols for parachute.
    """
    def __init__( self ):
        """Class constructor. Declares and initializes instance attributes.
        Args:
            self ( Jumper ): An instance of Jumper.
        """
        self.parachute =  [ " ___", "/___\\", "\   /", " \ /", "  0", " /|\\", " / \\" ]
    
    def check_parachute( self ):
        """Checks if the parachute is still viable, and changes the array if not.
        Args:
            self ( Jumper ): An instance of Jumper.
        Returns:
            boolean: True or false depending on if parachute works.
        """
        if self.parachute[0] != "  0":
            return True
        elif self.parachute[0] == "  0":
            self.parachute.pop( 0 )
            self.parachute.insert( 0, "  X" )
            return False

    def cut_parachute( self, valid_guess ):
        """Destroys the parachute if the guess is wrong.
        Args:
            self ( Jumper ): An instance of Jumper.
            valid_guess ( boolean ): The validity of the guess. 
        """
        if valid_guess == True:
            pass
        elif valid_guess == False:
            self.parachute.pop( 0 )

    def return_parachute( self ):
        """Returns the parachute as it now stands.
        Args:
            self (Jumper): An instance of Jumper.
        Returns:
            parachute (array): The parachute as it is currently.
        """
        return self.parachute