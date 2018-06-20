#-*- coding:utf-8 -*-
from konlpy.tag import Komoran
from pymongo import MongoClient

ko = Komoran()

client = MongoClient("mongodb://192.168.1.56:27017/")
db_ttolae = client.TTOLAE
collection_review = db_ttolae.review

find_movie = collection_review.find({"movie_id" : 42886})
count = find_movie.count()
test_review_list = []

for i in range(0,count) :
    current_document = find_movie.next()
    test_review_list.append(current_document)

sum = [ r['review_contents'] for r in test_review_list  ]
sample_list = sum[400:450]

# global global_index
# global_index = 0
# idx = 0
final_list=[]
final_word_list=[]

def chk(wordlist, idx, conList):
    if idx + 1 == len(wordlist) :
        print("끝지점 도달")
        print(idx+1)
        global global_index
        global_index  = idx
        return      #재귀에서 return은 함수를 끝내겠다는 뜻

    else :
        if wordlist[idx][1] == 'NNG' :
            if wordlist[idx + 1][1] == 'NNG' :
                conList.append(wordlist[idx + 1])
                print('NNGNNG : ',conList)
                final_list.append(conList)
                chk(wordlist, idx + 1, conList)

        elif wordlist[idx][1] == 'VA':
            if wordlist[idx + 1][1] == 'NNG' :
                conList.append(wordlist[idx+1])
                final_list.append(conList)
                print('VANNG : ', conList)
                chk(wordlist, idx + 1, conList)

                if wordlist[idx + 2][1] == 'NNG' or wordlist[idx + 2][1] == 'MAG':
                    conList.append(wordlist[idx + 2])
                    print('야이러너넌너넌: ',conList)
                    final_list.append(conList)
                    chk(wordlist, idx + 1, conList)

            elif wordlist[idx + 1][1] == 'ETM':
                conList.append(wordlist[idx + 1])
                # conList.append(wordlist[idx + 1] + wordlist[idx + 2])
                if wordlist[idx + 2][1] == 'NNG':
                    conList.append(wordlist[idx + 2])
                    print('VAETMNNG : ', conList)
                    final_list.append(conList)
                    chk(wordlist, idx + 1, conList)

        elif wordlist[idx][1] == 'MAG':
            if wordlist[idx + 1][1] == 'VA':
                conList.append(wordlist[idx+1])
                print('MAGVA : ', conList)
                final_list.append(conList)
                chk(wordlist, idx + 1, conList)


def pickup(wordlist):
    for idx, word in enumerate(wordlist):
        if idx + 1 == len(wordlist):
            break
        if word[1] == 'NNG' or word[1] =='VA' or word[1] == 'NNP' or word[1] =='NNB' or word[1] == 'NA' or word[1] =='NF' or word[1] == 'NV':
            # final_word_list.append([word])
            final_list.append([word])
            print("이것은말이지~~", word)


n=0
for sample in sample_list:
    wordlist = ko.pos(sample)
    pickup(wordlist)
    # into_words.append(final_word_list)
    i = 0
    n = n+1
    while i < len(wordlist) :
        chk(wordlist, i, [wordlist[i]])
        # into_words.append(final_list)
        i = i+1
        # print(i)
    print(n,"번째","list :", wordlist)
    print('FINAL_LIST',final_list)
    # print('WORD_LIST', final_word_list)
    final_list = []
    # final_word_list = []
    # print('WE MAKE WORDS!!!!!!! ', into_words)
    print("----------------------------------------------")

