class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : 
        POST : la fraction est initialisée avec le num et den
        RAISES : si le den vaut 0 alors on a ValueError
        """

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : la fraction est initialisée
        POST : retourne la fraction
        """

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : la fraction est initialisée
        POST : retourne une string de la partie int + reste/ den
        """

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other est une instance de la classe
         POST : retourne la somme de deux fractions
         RAISES :
         """

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other est une instance de la classe
        POST : retourne la difference de deux fractions
        RAISES :
        """

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other est une instance de la classe
        POST : retourne le produit de deux franctions
        RAISES :
        """

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other est une instance de la classe
        POST : retourne la puissance de deux franctions
        RAISES :
        """

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other est une instance de la classe
        POST : retourne la valeur vraie si les deux fractions sont =
        RAISES : si other n'est pas une instance de la fration on a TypeError

        """

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : fraction initialisée
        POST : retourne la valeur decimal d'une fration
        """

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : 
        POST : RETOURNE la valeur vraie si le num = 0 sinon faux
        """

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : 
        POST : retourne vraie sur le num est un multiple du den
        """

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : 
        POST : retourne vraie si la valeur absolue de la fracton est inferieur a 1
        """

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : 
        POST : retourne vrai si le numerateur vaut 1
        """

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : other est initialsiée
        POST : retourne vraie si la difference entre les deux fractions est une fraction unitaire
        RAISES : Si other n'est pas une fration valueError
        """