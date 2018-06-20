from pymongo import MongoClient

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from urllib.request import HTTPError
import time

client = MongoClient("mongodb://192.168.1.56:27017")
db_ttolae = client.TTOLAE
collection = db_ttolae.raw_daum_movie_info_add



n = 87474
errorPage = set()
fail_movieId=[]
while n < 120805 :  #이게 마지막임! 실제로는 120687!
    try:
        try:
            time.sleep(0.1)
            page = urlopen('https://movie.daum.net/moviedb/main?movieId={0}'.format(n))
            soup = BeautifulSoup(page, 'html.parser')

            movie_things = soup.find(class_='movie_detail')

        #영화가 없는 페이지 에러
        except HTTPError as e:
            print(e)
            #에러난 페이지 추가하기
            errorPage.add(n)
            n = n+1
            continue

        movie_id = n
        movie_title = (re.sub("\(\d{4}\)","", movie_things.find(class_='tit_movie').get_text())).strip()
        # 장르
        try:
            genre = movie_things.find('dl', class_='list_movie list_main').find_all()[1].get_text()
        except Exception as e:
            print(e)
            print("장르 없음")
            genre = ''


        # 개봉일
        try:
            opening = movie_things.find('dl', class_='list_movie list_main').find_all('dd', class_='txt_main')
            open_date = (re.findall('[^\D].+', opening[1].get_text())[0]).strip()
            # print(re.findall('[^\D].+',opening[1].get_text())[0])

            # for find_open in opening :
            #     opening_date_list = re.findall('\d.+',find_open.get_text())
            #     print(len(opening_date_list))
            #     print("opening_date_list", opening_date_list)
            #     # if len(opening_date_list) > 0:
            #     #     opendate = opening_date_list[1]
            #     # print(opendate)
            #     # open_date = opening_date_list
            #     # if opening_date_list != '(재개봉)':

            # open_date = (re.sub('개봉','',movie_things.find('dl',class_='list_movie list_main').find_all('dd',class_='txt_main')[1].get_text())).strip()
        except:
            open_date = ''
            errorPage.add(n)
            print('개봉일X')

        # 관람등급

        try:
            watching_info = movie_things.find("dl", class_="list_movie list_main").find_all('dd')
            watching_rate = ''
            for find_watching_rate in watching_info:
                watching_rate_list = re.findall('.*관람.*',
                                                find_watching_rate.get_text())  # find_watching_rate.get_text()
                if len(watching_rate_list) != 0:
                    watching_rate = watching_rate_list
                    # print("aaa", watching_rate)

            if len(watching_rate) > 0:
                W_rate = watching_rate[0]
                watching_rate = re.sub('\d+분,', '', W_rate).strip().strip()
                # print("watching_rate : ", watching_rate)
        except:
            print("Watching_rate에서 NonType 발생 fail_movieId 리스트에 추가")
            fail_movieId.extend([movie_id])


        try:
            nation = ''
            # 국가
            movie_things_dd_list = movie_things.find('dl', class_='list_movie list_main').find_all('dd')
            # print(movie_things_dd_list)

            for movie_things_dd in movie_things_dd_list :
                if ('''																		''' in movie_things_dd.get_text()) and ("감독" not in movie_things_dd.get_text()) and("주연" not in movie_things_dd.get_text()) :
                    movie_nation = movie_things_dd.get_text().strip()
                    nation = re.sub('\s', '', movie_nation).strip()
                    break

        except Exception as e:
            print(e)
            nation =''
            print('국가없음')







        print('================',n,'번째=======================')
        print('제목: ', movie_title)
        print('개봉일: ',open_date)
        print('장르: ',genre)
        print('관람등급: ',watching_rate)
        print('국가: ',nation)


        daum_movie = {'_id' : str(movie_id),
                        'movie_id' : [{'site':'daum','id':movie_id}],
                        'genre' : genre,
                        'open_date': open_date,
                        'watching rate' : watching_rate,
                        'nation' : nation
                          }

        collection.save(daum_movie)

        print(daum_movie)
        n = n+1

        print('오류 페이지 개수 : ', len(errorPage))
        # if len(errorPage) == 10000:
        #     break

    except Exception as exc:
        print(exc)
        print('전체 에러 발생 페이지 ', n)