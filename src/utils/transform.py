from utils.extract import *


def get_list_drugs(drugs):
    list_drugs = [str.lower(drug) for drug in drugs['drug']]
    return list_drugs


def find_drugs_mentioned(journals, drugs):
    """
        find_drugs_mentioned looks for drug mentions according to the following rules:
        - drug is considered as mentioned in PubMed article or in clinical test if it's mentioned in publication title.
        - drug is considered as mentioned bu journal if it is mentioned in publication issued by this journal.

        In output we create a nested json file with different hierarchical levels, multi indexed columns like :
         {"drug":"BETAMETHASONE" :
            {
                {'journal': 'Journal of emergency nursing',
                'date': '2020-01-01T00:00:00.000Z',
                'title': 'Use of Diphenhydramine as an Adjunctive Sedative for Colonoscopy in Patients Chronically on Opioids',
                'id': 'NCT01967433'
            }
    """

    list_drugs = get_list_drugs(drugs)

    def mentioned(row):
        """
        Function to extract the drug's names that are mentioned in the journal's title as a list
        """
        drugs_mentioned = []
        for drug in list_drugs:
            title = row['title']
            if drug in str.lower(title):
                drugs_mentioned.append(str.upper(drug))
        return drugs_mentioned

    # Creating a new column "drug" in the journal dataframe containing the list of mentioned drugs
    journals['drug'] = journals.apply(mentioned, axis=1)

    # Exploding the dataframe on the mentioned drugs list, splitting rows by the "," separator
    # Dataframe.explode : Transform each element of a list-like to a row, replicating index values.
    journals = journals.explode('drug')

    # Merging the journals dataframe with the drugs dataframe on the "drug" key
    drugs_mentioned_df = drugs.merge(journals, how='inner', on='drug').reset_index(drop=True)

    return drugs_mentioned_df


def write_nested_json(df):
    df.groupby(['drug', 'atccode'], as_index=True).apply(lambda x: x[['journal', 'date', 'title', 'id']]
                                                         .to_dict('records')) \
        .reset_index() \
        .rename(columns={0: 'publications'}) \
        .to_json('JSON_drugs_publications.json', orient='records', date_format='iso', indent=4, index=True,
                 force_ascii=False)

    print('Data Extraction-Transformation-Loading completed. \nPlease check the output here : {}'.format(
        Configs.RESULTS_PATH_JSON))
