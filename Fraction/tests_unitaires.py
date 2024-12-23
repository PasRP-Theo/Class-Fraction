import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):

    def test_initialisation(self):
        self.assertEqual(str(Fraction(2, 4)), "1/2")
        self.assertEqual(str(Fraction(-2, -4)), "1/2")
        self.assertEqual(str(Fraction(-2, 4)), "-1/2")
        self.assertEqual(str(Fraction(6, 2)), "3")
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_affichage_mixte(self):
        self.assertEqual(str(Fraction(2, 4)), "1/2")
        self.assertEqual(Fraction(7, 3).as_mixed_number(), "2 1/3")
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2")
        self.assertEqual(Fraction(1, 2).as_mixed_number(), "1/2")

    def test_addition(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 4), Fraction(3, 4))
        self.assertEqual(Fraction(1, 2) + Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(1, 2) + Fraction(-1, 4), Fraction(1, 4))
        self.assertEqual(Fraction(-1, 2) + Fraction(1, 2), Fraction(0, 1))

    def test_soustraction(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 4), Fraction(1, 4))
        self.assertEqual(Fraction(1, 2) - Fraction(1, 2), Fraction(0, 1))
        self.assertEqual(Fraction(1, 2) - Fraction(-1, 4), Fraction(3, 4))
        self.assertEqual(Fraction(-1, 2) - Fraction(1, 2), Fraction(-1, 1))

    def test_multiplication(self):
        self.assertEqual(Fraction(1, 2) * Fraction(1, 4), Fraction(1, 8))
        self.assertEqual(Fraction(2, 3) * Fraction(3, 4), Fraction(1, 2))
        self.assertEqual(Fraction(4, 2) * Fraction(5, 1), Fraction(10, 1))
        self.assertEqual(Fraction(-4, 2) * Fraction(5, 1), Fraction(-10, 1))

    def test_division(self):
        self.assertEqual(Fraction(1, 2) / Fraction(1, 4), Fraction(2, 1))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 1)
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 1) / Fraction(0, 1)
        self.assertEqual(Fraction(4, 2) / Fraction(5, 1), Fraction(2, 5))
        self.assertEqual(Fraction(-4, 2) / Fraction(5, 1), Fraction(-2, 5))

    def test_puissance(self):
        self.assertEqual(Fraction(1, 2) ** Fraction(2, 1), Fraction(1, 4))
        with self.assertRaises(ValueError):
            Fraction(-1, 2) ** Fraction(1, 2)
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 1) ** Fraction(-1, 1)
        self.assertEqual(Fraction(2, 3) ** Fraction(2, 1), Fraction(4, 9))
        self.assertEqual(Fraction(1, 2) ** Fraction(3, 2), Fraction(1, 8))

    def test_egalite(self):
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertFalse(Fraction(2, 3) == Fraction(3, 4))
        self.assertFalse(Fraction(1, 2) == Fraction(1, 3))

    def test_nulle(self):
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(1, 3).is_zero())

    def test_entier(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(3, 4).is_integer())

    def test_fractions_propre(self):
        self.assertTrue(Fraction(2, 3).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

    def test_unitaire(self):
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertTrue(Fraction(-1, 7).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())
        self.assertFalse(Fraction(0, 1).is_unit())

    def test_adjacent(self):
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))
        self.assertFalse(Fraction(2, 2).is_adjacent_to(Fraction(1, 3)))
        with self.assertRaises(TypeError):
            Fraction(1, 2).is_adjacent_to(1)

    def test_puissance_racine_negative(self):
        with self.assertRaises(ValueError):
            Fraction(-2, 3) ** Fraction(1, 2)

    def test_puissance_resultat_fractionnaire(self):
        with self.assertRaises(ValueError):
            Fraction(2, 3) ** Fraction(1, 2)

    def test_puissance_exposant_entier(self):
        self.assertEqual(Fraction(2, 3) ** Fraction(2, 1), Fraction(4, 9))

    def test_conversion_en_float(self):
        self.assertAlmostEqual(float(Fraction(1, 2)), 0.5)
        self.assertAlmostEqual(float(Fraction(-3, 4)), -0.75)
        self.assertEqual(float(Fraction(0, 1)), 0.0)

    def test_addition_pas_valide(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) + "n'est pas une fraction"

    def test_soustraction_non_valide(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) - 42

    def test_multiplication_non_valide(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) * None

    def test_division_non_valide(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) / [1, 2]

    def test_puissance_non_valide(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) ** "n'est pas une fraction"

if __name__ == "__main__":
    unittest.main()
