from utils.transform import *


def read_nested_json(json_file):
    with open(json_file) as json_data:
        data = json.load(json_data)
    df = pd.json_normalize(data,
                           record_path='publications',
                           meta=['drug', 'atccode'],
                           errors='ignore'
                           ) \
        .sort_values('journal')
    return df


# Ad-hoc Data Treatment : from the JSON output, finds the journal/or list of journals who mentions
# the most distinct drug names

def find_journal_with_max_distinct_drugs(df):
    journals_aggregated = df.groupby('journal').agg({'drug': pd.Series.nunique}) \
        .sort_values('drug',
                     ascending=False) \
        .reset_index()

    # In case top journals mentions the same number of distinct drugs
    maximum = None
    count = None
    for i, row in journals_aggregated['drug'].iteritems():
        if i == 0:
            maximum = row
            count = 1
        else:
            if row == maximum:
                count += 1
            else:
                break

    return journals_aggregated.nlargest(count, 'drug')
