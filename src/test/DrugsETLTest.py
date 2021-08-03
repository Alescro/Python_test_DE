import unittest

from utils.transform import *


class DrugsETLTest(unittest.TestCase):

    @staticmethod
    def fixture_read_files():
        return read_files()

    @staticmethod
    def fixture_create_dataframes():
        return create_dataframes()

    @staticmethod
    def fixture_find_drugs_mentioned(journals_df, drugs_df):
        return find_drugs_mentioned(journals_df, drugs_df)

    def test_total_number_titles(self):
        df1, df2 = DrugsETLTest.fixture_create_dataframes()
        drugs_mentioned = DrugsETLTest.fixture_find_drugs_mentioned(df1, df2)
        merged_title_count = drugs_mentioned['title'].count()
        expected_drug_mention_in_title_count = 8
        self.assertEqual(merged_title_count, expected_drug_mention_in_title_count)

    def test_valid_number_of_mention_for_diphenhydramine(self):
        df1, df2 = DrugsETLTest.fixture_create_dataframes()
        df = DrugsETLTest.fixture_find_drugs_mentioned(df1, df2)
        expected_drug_count = 6
        drug_name = 'DIPHENHYDRAMINE'
        df = df[df['drug'] == drug_name]
        df = df['drug'].count()
        self.assertEqual(df, expected_drug_count)


if __name__ == "__main__":
    unittest.main()
