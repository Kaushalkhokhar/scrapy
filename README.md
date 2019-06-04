# scrapy

## Settings required for adding different features

### To create database of extracted data

1. In items.py create field to store a extracted data
2. In pipelines.py 
  import <databse> like sqlite3, MySQL etc
  In instanciate the class with create_connetction and create_table methods to create a database table
  in process_item method call store_bd method, which has insert module to insert data to table.
3. In settings.py remove '#' from ITEM_PIPELINES

### for rotating user agent
Link: https://pypi.org/project/scrapy-user-agents/

### rotating IP
Link:https://github.com/hyan15/scrapy-proxy-pool

### general setting in settings.py
1. ROBOTSTXT_OBEY = True 
  True means folllows the robots.txt rules for given url
  False means does not folllows the robots.txt rules for given url

  
