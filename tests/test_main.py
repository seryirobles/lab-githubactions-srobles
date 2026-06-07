import io
import runpy
import unittest
from contextlib import redirect_stdout

import main


class TestMain(unittest.TestCase):
    def test_main_prints_greeting(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            main.main()
        self.assertEqual(
            buffer.getvalue(), "Hello from lab-githubactions-srobles!\n"
        )

    def test_main_returns_none(self):
        with redirect_stdout(io.StringIO()):
            self.assertIsNone(main.main())

    def test_module_run_as_script(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            runpy.run_module("main", run_name="__main__")
        self.assertEqual(
            buffer.getvalue(), "Hello from lab-githubactions-srobles!\n"
        )


if __name__ == "__main__":
    unittest.main()
