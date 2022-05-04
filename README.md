# twisel
library python for scraping twitter without API. 

## Details 
Twitter Api has limitation about time to get tweet, you can't get older tweets than a week. to get full archive tweet, you must submit approval and it could takes two days. but with selenium, you can build bot to scrap twitter automatically. but the problem is you must understand css and html to make scraping easier. this library is made for those who want to do tweeter scraping fast without API limitation. this library is my first open source project. i know this library have many bug and problem. so, this library also will be updated over time. sorry for my english, i hope i can improve my grammar like me updating this library. thank you :)

## Get Started
Before you use this library, you must download driver.exe according to your browser application and version. you can check this link: 
- Chrome  : https://chromedriver.chromium.org/downloads
- Safari  : http://www.java2s.com/Code/Jar/s/Downloadseleniumsafaridriver2291jar.htm
- Edge    : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- IE      : https://www.microsoft.com/en-us/download/details.aspx?id=44069
- FireFox : https://github.com/mozilla/geckodriver/releases


After  download driver, extract file and copy PATH where you save file .exe

example : 'C:\Users\Downloads\chromedriver_win32/chromedriver'

install library twisel using pip

```
pip install twisel
```
### searching tweets
```python
from twisel.getdata import SearchTwitter


scrap = SearchTwitter()
scrap.PATH =  r'C:\Users\Downloads\chromedriver_win32/chromedriver' #PATH where you save driver.exe
scrap.keyword = 'elon musk'
result = scrap.search()
```

- .PATH     : PATH where you save driver.exe *
- .keyword  : searching keyword (str) *
- .browser  : the browser you are currenty using (str) 
    - default : chrome
    - option  : edge, firefox, IE, safari
- .until    : search date limit 
    - default : ''
    - option  : 'YYYY-MM-DD'
- .since    : searh date limit
    - default : ''
    - option  : 'YYYY-MM-DD'
    
- .populer    : get populer tweeter (bool)
    - default : True
    - option  : False (get lastest tweet)
    
- .tweets : maximum data to be retrieved (int)
    - default : 100
    
    
(*) : required

### save to csv
```python
from twisel.save import Exporter

ekspor = Exporter()
ekspor.save_col = ['name','tweet']
ekspor.save_csv(result, 'output')

```

- .save_col  : 
    - default : ['tweet']
    - option : ['name','username','time']

save_csv(result, 'output')

result is variabel from scrap.search() and output is name scrap file in our directory.
