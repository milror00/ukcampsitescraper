# ukcampsitescraper

This is a demo project that uses python - and scrapy to locate uk campsites.

This is a demo to demonstrate the skills I have for scraping. This code is not to be used for any reason commercial or personally other than to demonstrate the approach to scraping.

Requirements to run :

* Python 3.7 above
* scrapy 2.1.0



## Steps for installation:

1. Clone git repo
1. pip install -r requirements.txt
1. settings file is by default set to write out results into a json file data_export.json.
1. run python main.py --start 11784 --end 11795. This is the page range - to search for stores
1. In the root of the file you should find data_export.json

## Troubleshooting 

Logs are streamed to stdout - exceptions and errors will be captured there please red through the log  

Log Level are set in the settings.py:

```
#LOG_FILE = 'scrapy.log'
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'
LOG_ENCODING = 'utf-8'
LOG_STDOUT =True

```


# Results

'''
[
  {
    "siteName": "Upper Hurst Farm",
    "postcode": "SK17 0HH",
    "telephone": "01298 687273"
  },
  {
    "siteName": "Keviki",
    "postcode": "DN15 9PA",
    "telephone": "01724 73405"
  },
  {
    "siteName": "Greenpark",
    "postcode": "AB31 4DB",
    "telephone": "01330 825544"
  },
  {
    "siteName": "Oaklands Leisure",
    "postcode": "SY6 7DL",
    "telephone": "01694 72377"
  }
]
'''
