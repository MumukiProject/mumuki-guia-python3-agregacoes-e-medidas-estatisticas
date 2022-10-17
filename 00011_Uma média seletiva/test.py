import pandas as pd

class Test(unittest.TestCase):

  def test_media_dos_primeiros_10_10_5_9_100_250_com_n_2(self):
    self.assertEquals(media_dos_primeiros(pd.Series([10, 10, 5, 9, 100, 250]), 2), 10)

  def test_media_dos_primeiros_10_10_5_9_100_250_com_n_4(self):
    self.assertEquals(media_dos_primeiros(pd.Series([10, 10, 5, 9, 100, 250]), 4), 8.5)

  def test_media_dos_primeiros_10_10_5_9_100_250_com_n_1(self):
    self.assertEquals(media_dos_primeiros(pd.Series([10, 10, 5, 9, 100, 250]), 1), 10)

  def test_media_dos_primeiros_1000_42_16_89_75_45_com_n_4(self):
    self.assertEquals(media_dos_primeiros(pd.Series([1000, 42, 16, 89, 75, 45]), 4), 286.75)
