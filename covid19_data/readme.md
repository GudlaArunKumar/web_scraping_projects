## Covid-19 Information Scraping:

Here we will scrap the data from the website https://www.covid19india.org/

**web scraping** -  Web scraping is an automatic method to obtain large amounts of data from websites. 
Most of this data is unstructured data in an HTML format which is then converted into structured data in a 
spreadsheet or a database so that it can be used in various applications

Refer here https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/

Also the data will be dynamic, so we can't write down manually and update daily, so in this case web scraping comes into the picture.

Whenever there ia request from client (web browser), request goes to server and it replies back with HTML, CSS, JS files so that client makes sense of all 3 files and display the web page accordingly.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Types of scraping:**

1. Static -  This is applicable only to static web pages where content is same each time we refresh the page
we can use Python Beautiful Soup library for static web scraping

2. Dynamic - This is applicable to dynamic web pages, for example covid 19 website, where data/content gets 
refreshed every and then in the web page.
we can use Selenium for dynamic Web scraping, because it has rendering part

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
**scraping using python:**

1. Install Selenium through "pip install selenium"
2. Install web drivers (can be for chrome, mozilla etc..) using selenium geckodriver web page.
3. By inspecting HTML code of the particular website, we can scrap the data which we are interested through crawling with help of class name or ID or CSS elements etc. depending on the web pages.
4. Structure the scraped data for further analysis







