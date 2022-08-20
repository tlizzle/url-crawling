# URL crawling process
Given urls, the porocess utilizes multiprocessing plus multi-threading to crawl from many websites 

# Run (dev mode)
- If virtual env already exists, activate: pipenv shell
    - If not, create virtual env: pipenv shell
    - Install all required packages:
        - install packages exactly as specified in Pipfile.lock: pipenv sync
        - install using the Pipfile, including the dev packages: pipenv install --dev

To Run the process
- `python -m src.main`
- After run the commnad above, the process will read the urls list from `url_list.csv` and generate output to `output.csv` which contains several information such as url,url_hash,title,title_hash,lang_code.

# Files 
- Data and output path can be adjusted in `./src/config.py`
- The main crawler process is written in  `./src/crawler.py`


