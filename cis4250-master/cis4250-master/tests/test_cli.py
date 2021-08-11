import unittest
import json
import sys
sys.path.append("..")

from cis4250.cli import CLI

class TestCLI(unittest.TestCase):

    def test_good_load_settings(self):
        """Test that the CLI correctly loads a valid settings file"""

        #Write valid settings values to a 'settings.json' file
        settings_dict = {"result_detail_level":"full","num_results": 20, "num_results_file": 100}

        with open("test_settings.json", "w") as fp:
            settings_json = json.dumps(settings_dict, indent=4)
            fp.write(settings_json)

        test_cli = CLI()

        test_cli.load_settings_from_file(True)

        self.assertEqual("full", test_cli.settings["result_detail_level"])
        self.assertEqual(20, test_cli.settings["num_results"])
        self.assertEqual(100, test_cli.settings["num_results_file"])

    def test_bad_load_settings(self):
        """Test that that CLI correctly ignores invalid settings data in a file"""

        #Write invalid setting values to a 'settings.json file
        settings_dict = {"result_detail_level":"extreme","num_results": 2000, "num_results_file": 20000}

        with open("test_settings.json", "w") as fp:
            settings_json = json.dumps(settings_dict, indent=4)
            fp.write(settings_json)

        test_cli = CLI()

        test_cli.load_settings_from_file(True)

        self.assertEqual("basic", test_cli.settings["result_detail_level"])
        self.assertEqual(20, test_cli.settings["num_results"])
        self.assertEqual(50, test_cli.settings["num_results_file"])

    def test_good_write_settings(self):
        """Test that that CLI correctly writes CLI settings to a file"""

        test_cli = CLI()
        test_cli.settings["num_results"] = 100
        test_cli.settings["result_detail_level"] = "detailed"
        test_cli.save_settings_to_file(True)

        with open("test_settings.json", "r") as fp:
            settings_dict = json.load(fp)

            self.assertEqual("detailed", settings_dict["result_detail_level"])
            self.assertEqual(100, settings_dict["num_results"])
            self.assertEqual(50, settings_dict["num_results_file"])


if __name__ == '__main__':
    unittest.main()