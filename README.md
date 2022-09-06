# S1GetSiteStats
Pulling information about sites of a given account (mainly for license count)with any given Sentineone hosted environment

You'll need the following information before you can run this script:

**AccountID**: This is the ID (only numbers) of your account within the Sentinelone hosted platform
You'll find this long numerical code under "Account Info" in your Portal

**API Token**: the Authorization token of a user account that has access to your account
Click on your user account name, then on "My User". Then click on "Options" and the on "Generate (or Regenerate) Token". Note that token (copy it), as you won't be able to retrieve it again once you close that window.
Unfortunately Auth Tokens expire automatically after 6 month (as of today (September 2022)) so you need to re-generate the token regularily and update your script. This can be done automatically by using the API as well.

**URL HOST**: The Host of your provider, i.e. everything before .sentinelone.net/web/api/v2.1

Once you edited the getSiteStats.py file with the values above you can run it with:

python3 getSiteStats.py

**Dependencies**
This script requires the following modules: requests, pandas and openpyxl

install with:

pip3 install requests pandas openpyxl before you run the script the first time.
