from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from selenium import webdriver
from urllib.request import HTTPError
import time

driver = webdriver.Chrome('C:/Users/bit/PycharmProjects/ujung/driver/chromedriver.exe')

n = 1
errorPage = set()
fail_movieId=[]
while n < 120718 :  #이게 마지막임! 실제로는 120687!
    try:
        try:
            time.sleep(0.1)
            page = urlopen('http://movie.daum.net/moviedb/main?movieId={0}'.format(n))
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

        try:
            movie_running = movie_things.find("dl", class_="list_movie list_main").find_all("dd")
            running_time = 0
            for running in movie_running:
                movie_running_list = running.get_text()
                find_running_time = re.findall('\d+분', movie_running_list)
                if len(find_running_time) > 0:
                    running_time = int(find_running_time[0].rstrip('분'))
                    print('=========================')
                    print(running_time)
                    print('=========================')

        except:
            print("running_time에서 NonType 발생 fail_movieId 리스트에 추가")
            fail_movieId.extend([movie_id])
            n = n+1
            continue

        direc = ''
        try:
            direc = movie_things.find('dd', class_="type_ellipsis").find('a', class_='link_person #info #name').get_text()
        except :
            pass

        print('================',n,'번째==========')
        print(movie_title)

        # 네티즌 평점 및 사용자 리뷰
        pg = 1

        while True:
            driver.get('http://movie.daum.net/moviedb/grade?movieId={0}&type=netizen&page={1}'.format(n, pg))
            time.sleep(0.1)
            review_page = driver.page_source
            soup2 = BeautifulSoup(review_page, 'html.parser')

            m_things = soup2.find(class_= 'movie_detail')

            m_rating = [ movie_rate.get_text() for movie_rate in m_things.find_all('span', class_='num_grade')[:3] ]
            movie_ratings = ''.join(m_rating)
            people = int(re.sub('\D','',m_things.find('span', class_='txt_menu').get_text()))

            if m_things.find('p', class_='txt_nonerating'):     #리뷰 없을 때
                print('ㄴ리뷰')
                review = {'movie_id': movie_id,
                          'site': 'daum',
                          'user_id': '',  # 작성자아이디
                          'review_contents': '',  # 해당 리뷰
                          'reg_date': ''}  # 리뷰작성일자
                # print(review)
                break
            else:  #리뷰 있을 때
                #print('리뷰잇당')
                length = len(list(m_things.find("ul", class_="list_review list_netizen").children))
                end = int((length - 1) / 2)

                review_name=[ name.get_text() for name in m_things.find_all('em', class_='link_profile') ]
                review_content=[content.get_text().replace('\n','').replace('\t','').strip() for content in m_things.find_all('p', class_='desc_review')]
                sign_user = [ user.attrs['href'].split('uid=')[1][:7] for user in m_things.find_all('a', class_='link_review') ]
                review_regDate= [review.get_text().replace('\n','').replace('\t','')[:-7] for review in m_things.find_all('span', class_='info_append')]
                user_grade =  [int(grade.get_text()) for grade in m_things.find_all('em', class_='emph_grade')]

                for i in range(0, end):
                    review = {"movie_id": movie_id, "site": "daum", "user_id": sign_user[i]+review_name[i], "review_contents": review_content[i], "reg_date": review_regDate[i], "user_grade": user_grade[i]}
                    # print(review)

            pg += 1



        daum_movie = {'movie_id' : [{'site':'daum','id':movie_id}],
                        'movie_title' : movie_title,
                        'director': direc,
                        'running_time' : running_time,
                        'review_cnt' : [{'site' : 'daum','cnt': people}],
                        'score':[{'site':'daum','grade': movie_ratings}]
                          }
        print(daum_movie)
        n = n+1

        print('오류 페이지 개수 : ', len(errorPage))
        if len(errorPage) == 10000:
            break

    except Exception as exc:
        print(exc)
        print('전체 에러 발생 페이지 ', n)









