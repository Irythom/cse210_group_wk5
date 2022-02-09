class Terminal_service:
    """This class is in charge of the console. Basically sending and recieving information
    to and from the console. More specifically it gets and sends text and numbers.
    
    Stereotype: 
        Interfacer
        
    Attributes:
        letter: The place where the input for the letter is stored.
        current_guess: Where the user's current guesses is displayed.
        parachute: Where the parachute is printed out line by line.
    """

    def __init__( self ):
        """Constructs a new Terminal service.
        Args:
            self ( Terminal_service ): An instance of Terminal_service. 
        """
        self.letter = ""
        
    def get_letter( self ):
        """Gets letter from the player.
        Args:
            self ( Terminal service ): An instance of Terminal_service. 
        Returns:
            Char: The letter from the user.
        """
        self.letter = input( "Guess a letter [a-z]: " )
        return self.letter

    def display_guess( self, current_guess ):
        """Displays the current correct guesses from the user
        Args:
            self ( Terminal service ): An instance of Terminal_service. 
            current_guess (string): The current guess's made by user.
        """
        for i in range(0, len( current_guess ), 1 ):
            print( f"{current_guess[i]} ", end = "" )


    def display_parachute( self, parachute ):
        """Displays the current correct guesses from the user
        Args:
            self ( Terminal service ): An instance of Terminal_service.  
            parachute ( array ): The current parachute as it now stands.
        """
        print()
        print()
        for i in range ( 0, len(parachute ), 1 ):
            print( parachute[i] )
              
        print()
        print( "^^^^^^^" )

        if parachute[0] == "  X":
            print("Game over")

        else:
            print("Play")
        
    
            

    