import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name('hello.py')


class GreetingCliTests(unittest.TestCase):
    def run_program(self, *args: str) -> str:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout

    def test_no_names_runs_default_demo(self) -> None:
        self.assertEqual(
            self.run_program(),
            'Hello Samantha\nGoodbye Alan\nHello Class!\n',
        )

    def test_one_name_gets_personalized_greeting(self) -> None:
        self.assertEqual(self.run_program('Alice'), 'Hello Alice!\n')

    def test_multiple_names_each_get_a_greeting(self) -> None:
        self.assertEqual(
            self.run_program('Alice', 'Bob'),
            'Hello Alice!\nHello Bob!\n',
        )


if __name__ == '__main__':
    unittest.main()
