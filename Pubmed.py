fetch = PubMedFetcher()
 * You can also use fetch = PubMedFetcher(cachedir='/path/to/cachedir') to specify the cache. 
article = fetch.article_by_pmid('123456')
print(article.title)
print(article.journal, article.year, article.volume, article.issue)
print(article.authors)

 * Also refer to https://pypi.python.org/pypi/metapub for further directions


