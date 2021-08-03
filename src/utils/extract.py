from configs.Config import *

Configs = Config()


# Function to read input files and normalize dates format

def read_files(files,
               date_cols: list = None,
               ):
    """
    Function to read dataframes over any list of appendable files from any formats
    Args:
        files: list of file paths
        date_cols: columns to parse into datetime
    """

    def check_date_cols(DF, dates):
        dtypes = dict(DF.dtypes)  # we get a dict with the dtypes of each column
        dates = [col for col in dates if col in DF.columns]
        for col in dates:
            DF[col] = pd.to_datetime(DF[col],
                                     errors='coerce')
        return DF

    def read_file(f,
                  dates,
                  extension: str = None

                  ):

        if 'csv' in file_extension:
            dataframe = pd.read_csv(f, sep=',')
            columns = dataframe.columns
        elif 'json' in file_extension:
            dataframe = pd.read_json(f, convert_dates=True)
            columns = dataframe.columns

        dataframe = check_date_cols(dataframe, dates)

        return dataframe, columns

    total_files = len(files)
    # list of dataframes to transform later on
    dfs = []
    for i, file in enumerate(list(files)):
        file_extension = file.suffix

        try:
            df, _ = read_file(file, date_cols, file_extension)

            print(
                "│ ├─ {0}/{1}, @{2}: {3}".format(i + 1, total_files, datetime.now().strftime('%H:%M'), str(file.name)))
            # We filter only the wanted columns and add an indicator of the file where these rows come from

            dfs.append(df)

        except Exception as e:
            raise ImportError(f"! ├─ !! Could not fetch {file.name}; {e.args}")

    return dfs

    print(f"│ └─ @{datetime.now().strftime('%H:%M')}: FINISHED Appending")


def clean_clinical(df):
    # Checking NaN values in the df
    df[df.isna().any(axis=1)]

    # Filling the first row with complementary information from its duplicate row
    df = df.fillna(df.loc[6, :]).dropna()

    # Renaming the column name as 'title', cleaning rows from "xc3" parasite strings
    df = df.replace(r'\\xc3\\xb1', '', regex=True)
    df = df.replace(r'\\xc3\\x28', '', regex=True).rename(columns={"scientific_title": "title"})

    return df


def create_dataframes():
    clinical_df, drugs_df, pubmed_csv, pubmed_json = read_files([Configs.CLINICAL_TRIALS_PATH, Configs.DRUGS_PATH,
                                                                 Configs.PUBMED_CSV_PATH, Configs.PUBMED_JSON_PATH],
                                                                date_cols=['date'])

    # Concatenating pubmed two dataframes into one
    pubmed_df = pd.concat([pubmed_csv, pubmed_json], ignore_index=True)
    # Adding one missing id on row 13
    pubmed_df["id"] = np.where((pubmed_df.id == "") & (pubmed_df.journal.str.contains("maternal-fetal", case=False)),
                               "13", pubmed_df.id)

    # Cleaning the clinical trials dataframe
    clinical_df = clean_clinical(clinical_df)

    # Merging journal dataframes together
    journals_df = pd.concat([clinical_df, pubmed_df], ignore_index=True)
    return journals_df, drugs_df