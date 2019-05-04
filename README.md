# AutoMiner
AutoMiner harnesses the power of data mining to discover patterns in transaction data. You can use this app to apply these methods to your own data by uploading a data file and tweaking the support and confidence settings.

AutoMiner is hosted on Heroku: https://autominer.herokuapp.com/

## Requirements
This application is written for Python 3.6+ and uses the following libraries:
* gunicorn
* flask
* flask-wtf
* wtforms
* apyori

## Form Fields
### File
You can upload your own data file of transactions to be mined by AutoMiner. The file must have one transaction per line, with items separated by semicolons. The file must also conform to UTF-8 encoding (meaning some special characters may not be permitted).

### Minimum Support
This field refers to the minimum relative support, which refers to how often items in a pattern co-occur in transactions. This can be any value from 0 to 1. Increasing this value filters out more patterns, resulting in only the most popular ones being mined.

### Minimum Confidence
Confidence is a value that describes how often association rules are found to be true. In other words, if item A occurs in a transaction, how likely is it that item B will also occur? This can be any value from 0 to 1. Increasing this value results in fewer patterns being mined, since it will only retain the most confident rules.

## Troubleshooting
Due to limited resources, the app may sometimes timeout during mining, displaying an "Application Error" page. If this occurs, please try increasing your support and confidence values. If the problem persists, you may also need to try a smaller data file.

## Results
Once you submit the form, the app will begin mining patterns from your data. Once it is finished, it will automatically download the results file. The first line of this file contains the name of the data file that you submitted, the values you specified for support and confidence, and the execution time in seconds.

After this line, the results file contains all of the prominent patterns that were mined based on your settings. Each line contains a pattern (which consists of one or more items separated by semicolons) and the number of times it appears in the data file (also known as absolute support). Below is a sample of what these lines may look like:

`[150, 'Bread; Milk; Eggs']`
