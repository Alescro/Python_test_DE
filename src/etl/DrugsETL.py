from utils.transform import *
import logging

logging.basicConfig(filename='logger.txt',
                    level=logging.NOTSET,
                    filemode='w'
                    )
logger = logging.getLogger(__name__)


class DrugsETL:

    # Main to launch the data ETL pipeline

    @staticmethod
    def run():
        journals_df, drugs_df = create_dataframes()
        logger.debug('Files have been loaded into 2 dataframes : journals_df and drugs_df')
        drugs_mentioned_df = find_drugs_mentioned(journals_df, drugs_df)
        logger.debug('A new dataframe has been created. \nDrugs_mentioned_df shows the different drugs and their '
                     'related mentions in trials and publications from journals')
        return write_nested_json(drugs_mentioned_df)


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    ETL = DrugsETL()
    ETL.run()
    logger.info('Data ETL completed. \nPlease check the output here : {}'.format(
        Configs.NESTED_JSON_PATH))
