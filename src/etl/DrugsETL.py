from utils.transform import *


class DrugsETL:

    # Main to launch the data ETL pipeline

    @staticmethod
    def run():
        journals_df, drugs_df = create_dataframes()
        drugs_mentioned_df = find_drugs_mentioned(journals_df, drugs_df)
        return write_nested_json(drugs_mentioned_df)


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    ETL = DrugsETL()
    ETL.run()
