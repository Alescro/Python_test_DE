import unittest

from utils.adhoc import *


class AdhocTest(unittest.TestCase):

    @staticmethod
    def fixture_read_nested_json():
        return read_nested_json("resources/raw/JSON_drugs_publications.json")

    @staticmethod
    def fixture_find_journal_with_max_distinct_drugs():
        df = AdhocTest.fixture_read_nested_json()
        return find_journal_with_max_distinct_drugs(df)

    def test_adhoc(self):
        result = AdhocTest.fixture_find_journal_with_max_distinct_drugs()
        expected = {'journal': ["Journal of emergency nursing", "Psychopharmacology", "The journal of maternal-fetal "
                                                                                      "& neonatal medicine"],
                    'drug': [2, 2, 2]}
        expected_result = pd.DataFrame(data=expected)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

