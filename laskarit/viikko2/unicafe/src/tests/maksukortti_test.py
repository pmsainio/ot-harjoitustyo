import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)


    def test_alkusaldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_saldo_kasvaa(self):
            self.maksukortti.lataa_rahaa(41000)
            self.assertEqual(str(self.maksukortti), "saldo: 420.0")

    def test_saldo_pienenee(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_saldo_pysyy_positiivisena(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5000), False)