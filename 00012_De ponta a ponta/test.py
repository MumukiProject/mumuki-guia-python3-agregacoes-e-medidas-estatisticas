import pandas as pd

class Test(unittest.TestCase):

  def test_diferencia_de_extremos_10_5_100(self):
    self.assertEquals(diferencia_de_extremos(pd.Series([10, 5, 100])), 95)

  def test_diferencia_de_extremos_10_10_5_9_100_250(self):
    self.assertEquals(diferencia_de_extremos(pd.Series([10, 10, 5, 9, 100, 250])), 245)

  def test_diferencia_de_extremos_1000_42_16_89_75_45(self):
    self.assertEquals(diferencia_de_extremos(pd.Series([1000, 42, 16, 89, 75, 45])), 984)
