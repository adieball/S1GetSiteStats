#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import requests
import json
import pandas as pd
import time

import urllib.request
import os.path

def main():
    """ Main entry point of the app """
    url = "https://PROVIDERURL.sentinelone.net/web/api/v2.1"
    # add your API Token here behind ApiToken:
    PARAMS = {"Authorization": "ApiToken ADDTOKENHERE"}
    # add your Account ID here:
    ACCOUNTID = "ADDACCOUNTIDHERE"
    urlGetSites = "/sites?limit=999&sortBy=name&states=active&accountId={}".format(ACCOUNTID)


    

    r = requests.get(url + urlGetSites, headers = PARAMS)
    data = r.json()

    #print(data)

    my_json = data['data']['sites']
    result = pd.DataFrame(my_json)
    print(result)

    with open('data.txt', 'w', encoding='utf-8') as f:
        json.dump(data, f, sort_keys=True, ensure_ascii=False, indent=4)

    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = timestr + '_json_data.xlsx'
    #uncomment and adjust in case you want to write the resulting XLS file somewhere else than the script home folder
    """
    savepath = '/home/s1mssp/s1-usagedata'
    completename = os.path.join(savepath, filename)
    """
    #delete this line in case you used above directory instructions!
    completename = filename

    print(completename)

    df = pd.DataFrame(result)
    df.head()
    df[['accountId', 'accountName','name', 'siteType', 'externalId', 'activeLicenses', 'totalLicenses', 'sku', 'state']].to_excel(completename)


# uncomment the following for monitoring script runs via PushMon
"""
    urlString = 'http://pshmn.com/xxxxxxxx'
    try:
        handle = urllib.request.urlopen(urlString)
        handle.read()
        handle.close()
    except IOError:
        print ("log error")
"""


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
