from math import gcd

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
        if den == 0:
            raise ValueError("Den peut pas etre zero.")

        common_divisor = gcd(num, den)                 # Simplify fraction with GCD
        self.__numerator = num // common_divisor
        self.__denominator = den // common_divisor

        if self.denominator < 0:                     # Force den to be positive
            self.__numerator = -self.numerator
            self.__denominator = -self.denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : la fraction est initialisée
        POST : retourne la fraction
        """
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : la fraction est initialisée
        POST : retourne une string de la partie int + reste/ den
        """
        integer_part = self.numerator // self.denominator
        remainder = abs(self.numerator % self.denominator)

        if remainder == 0:
            return str(integer_part)
        elif integer_part == 0:
            return f"{remainder}/{self.denominator}"
        else:
            return f"{integer_part} {remainder}/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other est une instance de la classe
         POST : retourne la somme de deux fractions
         RAISES :
         """
        if not isinstance(other, Fraction):
            raise TypeError("peut ajouter que deux intances de la fraction.")

        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_den = self.denominator * other.denominator  # fraction sum formula
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other est une instance de la classe
        POST : retourne la difference de deux fractions
        RAISES :
        """
        if not isinstance(other, Fraction):
            raise TypeError("peut ajouter que deux intances de la fraction")

        new_num = self.numerator * other.denominator - self.denominator * other.numerator
        new_den = self.denominator * other.denominator    # fraction sub. formula
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other est une instance de la classe
        POST : retourne le produit de deux franctions
        RAISES :
        """
        if not isinstance(other, Fraction):
            raise TypeError("peut ajouter que deux intances de la fraction")

        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator    # fraction mul. formula
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other est une instance de la classe
        POST : retourne le queotient de deux franctions
        RAISES :
        """
        if not isinstance(other, Fraction):
            raise TypeError("peut diviser que deux intances de la fraction.")

        if other.numerator == 0:
            raise ZeroDivisionError("Num ne peut pas etre 0.")

        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator  # fraction division formula
        return Fraction(new_num, new_den)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other est une instance de la classe
        POST : retourne la puissance de deux franctions
        RAISES :
        """
        if not isinstance(other, Fraction):
            raise TypeError("la fraction doit avoir deux instance.")

        if other.denominator == 1:  # Exponent is an integer
            num_power = pow(self.numerator, other.numerator)
            den_power = pow(self.denominator, other.numerator)
            return Fraction(num_power, den_power)

        if self.numerator < 0:  # Negative base with fractional exponent
            raise ValueError("impossible de calculer la puissant d'un négatif.")

        # Handle fractional exponents
        num_power = pow(self.numerator, other.numerator)
        den_power = pow(self.denominator, other.numerator)

        num_result = num_power ** (1 / other.denominator)
        den_result = den_power ** (1 / other.denominator)

        # Ensure results are integers for valid fractions by rounding and comparing
        if round(num_result) != num_result or round(den_result) != den_result:
            raise ValueError("le resultat de la fraction n'est pas représentable sous forme int.")

        return Fraction(int(round(num_result)), int(round(den_result)))

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other est une instance de la classe
        POST : retourne la valeur vraie si les deux fractions sont =
        RAISES : si other n'est pas une instance de la fration on a TypeError

        """
        if not isinstance(other, Fraction):
            raise TypeError("la fraction doit avoir deux instance.")

        return self.numerator * other.denominator == self.denominator * other.numerator

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : fraction initialisée
        POST : retourne la valeur decimal d'une fration
        """
        return self.numerator / self.denominator

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : 
        POST : RETOURNE la valeur vraie si le num = 0 sinon faux
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : 
        POST : retourne vraie sur le num est un multiple du den
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : 
        POST : retourne vraie si la valeur absolue de la fracton est inferieur a 1
        """

        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : 
        POST : retourne vrai si le numerateur vaut 1
        """
        return abs(self.numerator) == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : other est initialsiée
        POST : retourne vraie si la difference entre les deux fractions est une fraction unitaire
        RAISES : Si other n'est pas une fration valueError
        """
        if not isinstance(other, Fraction):
            raise TypeError("la fraction doit avoir deux instance.")

        return (self - other).is_unit()

if __name__ == '__main__':
    print(Fraction(2, 4))            # Affiche : 1/2
    print(Fraction(-2, -4))          # Affiche : 1/2
    print(Fraction(-2, 4))           # Affiche : -1/2
    print(Fraction(6, 2))            # Affiche : 3
    print(Fraction(2, 4))            # Affiche : 1/2
    print(Fraction(7, 3).as_mixed_number())  # Affiche : 2 1/3
    print(Fraction(4, 2).as_mixed_number())  # Affiche : 2

    print(Fraction(1, 2) + Fraction(1, 4))  # Affiche : 3/4
    print(Fraction(1, 2) - Fraction(1, 4))  # Affiche : 1/4
    print(Fraction(1, 2) * Fraction(1, 4))  # Affiche : 1/8
    print(Fraction(1, 2) / Fraction(1, 4))  # Affiche : 2
    print(Fraction(2, 3) ** Fraction(2, 1))  # Affiche : 4/9
    print(Fraction(1, 2) == Fraction(1, 2))  # Affiche : True

    print(float(Fraction(1, 2)))   # Affiche : 0.5

    print(Fraction(0, 3).is_zero())  # Affiche : True
    print(Fraction(8, 4).is_integer())  # Affiche : True
    print(Fraction(4, 6).is_proper())   # Affiche : True
    print(Fraction(3, 9).is_unit())     # Affiche : True
    print('\n')

    print(Fraction(2, 4).is_zero())     # Affiche : False
    print(Fraction(3, 9).is_integer())  # Affiche : False
    print(Fraction(9, 3).is_proper())   # Affiche : False
    print(Fraction(5, 3).is_unit())     # Affiche : False
    print(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))  # Affiche : True
    print(Fraction(2, 2).is_adjacent_to(Fraction(1, 3)))  # Affiche : False

    try:
        print(Fraction(1, 2) + 1)
    except TypeError as e:
        print("Erreur :", e)
    try:
        print(Fraction(1, 2) / Fraction(0, 1))
    except ZeroDivisionError as e:
        print("Erreur :", e)
