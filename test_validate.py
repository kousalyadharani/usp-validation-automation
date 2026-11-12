import unittest
from validate import run
class ValidationTests(unittest.TestCase):
 def test_reports_each_check(self):
  r=run([{"name":"x","path":"a","op":"equals","expected":1}],{"a":1});self.assertEqual((r["passed"],r["failed"]),(1,0))
 def test_missing_path_fails_visible(self):
  r=run([{"name":"x","path":"missing","expected":1}],{});self.assertEqual(r["failed"],1);self.assertIn("missing",r["results"][0]["reason"])
if __name__=="__main__":unittest.main()
