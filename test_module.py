import unittest
from sea_level_predictor import draw_plot


class SeaLevelPredictorTest(unittest.TestCase):

    def test_draw_plot(self):
        fig = draw_plot()
        self.assertIsNotNone(fig)


if __name__ == "__main__":
    unittest.main()
