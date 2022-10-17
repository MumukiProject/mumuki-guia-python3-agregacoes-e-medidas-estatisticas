import pandas as pd

class Test(unittest.TestCase):

  def test_promedio_de_los_primeros_10_10_5_9_100_250_con_n_2(self):
    self.assertEquals(promedio_de_los_primeros(pd.Series([10, 10, 5, 9, 100, 250]), 2), 10)

  def test_promedio_de_los_primeros_10_10_5_9_100_250_con_n_4(self):
    self.assertEquals(promedio_de_los_primeros(pd.Series([10, 10, 5, 9, 100, 250]), 4), 8.5)

  def test_promedio_de_los_primeros_10_10_5_9_100_250_con_n_1(self):
    self.assertEquals(promedio_de_los_primeros(pd.Series([10, 10, 5, 9, 100, 250]), 1), 10)

  def test_promedio_de_los_primeros_1000_42_16_89_75_45_con_n_4(self):
    self.assertEquals(promedio_de_los_primeros(pd.Series([1000, 42, 16, 89, 75, 45]), 4), 286.75)
