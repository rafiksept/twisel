from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time


class CustomError(Exception):
    pass

class SearchTwitter:

    def __init__(self):
        self.PATH = r'c:'
        self.browser = 'chrome'
        self.keyword = ''
        self.until = ''
        self.since = ''
        self.populer = True
        self.tweets = 10000
        self.lang = "en"

    def setKeyword(self):
        spliting = self.keyword.split()
        joining = '%20'.join(spliting)
        searching = f'%22{joining}%22'

        return searching

    def setPopuler(self):
        if self.populer == False:
            populer = '&f=live'
        else:
            populer = ''

        return populer

    def setUntil(self):
        if self.until != '':
            until = f'%20until%3A{self.until}'
        else:
            until = ''

        return until

    def setSince(self):
        if self.since != '':
            since = f'%20since%3A{self.since}'
        else:
            since = ''

        return since

    def setSrc(self):
        if self.until != '' or self.since != '':
            src = 'typed_query'
        else:
            src = 'recent_search_click'

        return src

    def setTweets(self):
      return self.tweets

    def setLang(self):
        return f'%20lang%3A{self.lang}'



    def getDriver(self):

        if self.browser == 'chrome':
            return webdriver.Chrome(executable_path=self.PATH)
        elif self.browser == 'edge':
            return webdriver.Edge(executable_path= self.PATH)
        elif self.browser == 'firefox':
            return webdriver.Firefox(executable_path=self.PATH)
        elif self.browser == 'IE':
            return webdriver.Ie(executable_path=self.PATH)
        elif self.browser == 'safari':
            return webdriver.Safari(executable_path=self.PATH)

    def search(self):
        if self.keyword == '':
            raise CustomError('Keyword not Valid!')
        else:
            driver = self.getDriver()
            driver.get(f'https://twitter.com/search?q={self.setKeyword()}{self.setLang()}{self.setUntil()}{self.setSince()}&src={self.setSrc()}{self.setPopuler()}')
            kata = []
            layar = 0
            make_sure = 0


            while True:

                loading = WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'svg[style="stroke: rgb(29, 155, 240); opacity: 0.2;"]')))
                huruf = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.css-1dbjc4n article')))
                temukan = driver.find_elements(By.CSS_SELECTOR,'article .css-1dbjc4n .r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0')
                nama = driver.find_elements(By.CSS_SELECTOR,'article .css-901oao.r-1awozwy.r-6koalj.r-37j5jr.r-a023e6.r-b88u0q.r-rjixqe.r-bcqeeo.r-1udh08x.r-3s2u2q.r-qvutc0')
                username = driver.find_elements(By.CSS_SELECTOR,'article .css-901oao.css-1hf3ou5.r-14j79pv.r-18u37iz.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0 .css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
                waktu_tunggu = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, 'time')))
                times = driver.find_elements(By.TAG_NAME, 'time')



                if len(kata) > self.setTweets():
                    break


                for i, j,l, c  in zip(nama, temukan, username, times):
                    try:
                        jr = j.text.replace('\n', ' ')
                        ir = i.text
                        lr = l.text
                        cr = c.get_attribute('datetime')
                    except:
                        jr = "Failed"
                        ir = "Failed"
                        lr = "Failed"
                        cr = "Failed"


                    kata.append({'name': ir,'username':lr, 'tweet': jr,'time':cr})




                last_height = driver.execute_script("return document.body.scrollHeight")

                if int(layar) == int(last_height) + 720 :
                    if make_sure > 5:
                        driver.close()
                        break
                    make_sure += 1
                else:
                    make_sure = 0



                driver.execute_script(f"window.scrollTo(0, {layar});")
                time.sleep(0.5)
                layar = int(last_height) + 720

            val = []
            for i in kata:
                if i in val:
                    continue
                else:
                    val.append(i)


            return val[:self.tweets]



# if __name__ == "__main__":
#     scrap = SearchTwitter()
#     scrap.PATH = r'C:\Users\RAFIK\Downloads\chromedriver_win32 (4)/chromedriver'  # PATH where you save driver.exe
#     scrap.keyword = 'bali'
#     scrap.until = '2022-07-20'
#     scrap.since = '2022-07-19'
#     scrap.tweets = 10000
#     scrap.populer = False
#     result = scrap.search()
#
#     ekspor = Exporter()
#     ekspor.save_col = ['tweet']
#     ekspor.save_csv(result, 'datagemastik')