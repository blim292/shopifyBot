# shopifyBot
##### Shopify scraping/automation

###### Purpose:
PoC of web scraping/automation using a combination of the beautifulsoup library and selenium framework in Python.

###### Summary of Processes:
1. Bootup selenium webdriver when starting script (can choose to run the automation with a phantom browser as a background process)
2. Use a get request and process the html using beautifulsoup to look for changes in page (restock).
3. If restock is found, proceed with selenium automation.
