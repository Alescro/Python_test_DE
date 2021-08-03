from utils.adhoc import *


class Adhoc:

    @staticmethod
    def run():
        df = read_nested_json(Configs.RESULTS_PATH_JSON)
        return find_journal_with_max_distinct_drugs(df)


if __name__ == "__main__":
    adhoc_treatment = Adhoc()
    result = adhoc_treatment.run()
    print(result)

