import os

cwd = os.getcwd()
CORPUS = '../corpus'
sites = [
    "https://github.com/search?p={}&q=stars%3A%3E0&s=stars&type=Repositories",  \
    "https://github.com/search?o=desc&p={}&q=stars%3A%3E1&s=forks&type=Repositories"]
