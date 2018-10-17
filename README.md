# XJTU Ancient Book Search

A tool for searching ancient books in XJTU, powered by ElasticLunr.js.
Have a try! [https://hehuan2112.github.io/xjtu-ancient-books/](https://hehuan2112.github.io/xjtu-ancient-books/).

The original version is based on the ElasticSearch, which means that a backend server is needed to run the server program. Since the amount of books is not so large, I re-wrote the query function and use a in-browser search engine to provide instant search. However, as present, the ElasticLunr.js doesn't support indexing Chinese words. I temporarily used a Japanese tokenizer to process text. 