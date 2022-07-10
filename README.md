# URL crawling process
Given urls, i utilize multiprocessing plus multi-threading to crawl from many websites 

# Run (dev mode)
- If virtual env already exists, activate: pipenv shell
    - If not, create virtual env: pipenv shell
    - Install all required packages:
        - install packages exactly as specified in Pipfile.lock: pipenv sync
        - install using the Pipfile, including the dev packages: pipenv install --dev

# Files
- Data and output path can be adjusted in `./src/config.py`
- The main crawler process is written in  `./src/crawler.py`


