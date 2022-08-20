from src.crawler import Crawler
from src.config import data_path, output_columns
import pandas as pd


def main():
    df = pd.read_csv(data_path + '/url_list.csv')

    input_list = df.values.tolist()
    crawler = Crawler()
    result  = crawler.multi_processing(input_list)

    output = [i for r in result.get() for i in r]

    output = pd.DataFrame(output, columns= output_columns)
    output.to_csv(data_path + '/output.csv')

    
if __name__ == "__main__":
    main()


# langdetect = "*"
# requests = "*"
# bs4 = "*"
# nltk = "*"
# sklearn = "*"
# lxml = "*"
# pandas = "*"
