import unittest

from atividades import comer, dormir


class AtividadesTestes(unittest.TestCase):
    def test_comer_saudavel(self):
        self.assertEqual(
            comer("quiabo", True), "Estou comendo quiabo, porque quero manter a forma"
        )

    def test_comer_junk(self):
        self.assertEqual(
            comer(comida="pizza", eh_saudavel=False),
            "Estou comendo pizza, porque a gente só vive uma vez",
        )

    def test_dormir_pouco(self):
        self.assertEqual(dormir(4), "Continuo cansado após dormir por 4 horas.")

    def test_dormir_muito(self):
        self.assertEqual(dormir(10), "Dormi muito, to atrasado pro trabalho.")


if __name__ == "__main__":
    unittest.main()
