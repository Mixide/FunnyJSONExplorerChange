import unittest
import sys
from io import StringIO
sys.path.append("./")
from Strategy.TreeStrategy import TreeStrategy
from Strategy.RectStrategy import RectStrategy
from FJE import FJE 
class TestTreeFJEOutput(unittest.TestCase):
    def test_print_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        fje = FJE(TreeStrategy("Test/icon_test.json"))
        fje.show("Test/test.json")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), 
        "├─♧oranges\n"+
        "|  └─♧mandarin\n"+
        "|     ├─♣clementine\n"+
        "|     └─♣tangerine:cheap & juicy!\n"+
        "└─♧apples\n"+
        "   ├─♣gala\n"+
        "   └─♣pink lady\n")

class TestRectFJEOutput(unittest.TestCase):
    def test_print_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        fje = FJE(RectStrategy("Test/icon_test.json"))
        fje.show("Test/test.json")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), 
        "┌─♧oranges───────────────────────────────────────┐\n"+
        "|──├─♧mandarin───────────────────────────────────|\n"+
        "|──|──├─♣clementine──────────────────────────────|\n"+
        "|──|──├─♣tangerine:cheap & juicy!────────────────|\n"+
        "├─♧apples────────────────────────────────────────|\n"+
        "|──├─♣gala───────────────────────────────────────|\n"+
        "└──└─♣pink lady──────────────────────────────────┘\n")

if __name__ == '__main__':
    unittest.main()