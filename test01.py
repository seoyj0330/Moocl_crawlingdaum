 #의미 있는 단어들 리스트를 합쳐서 한 단어로 만들기
#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import re
import unicodedata
import hgtk


make = [[('좋', 'VA'), ('은', 'ETM'), ('영화', 'NNG')], [('마지막', 'NNG'), ('대결', 'NNG')], [('만화', 'NNG'), ('원작', 'NNG')], [('뻔하', 'VA'), ('ㄴ', 'ETM'), ('스토리', 'NNG')]]

# for makings in make:
#     print(makings)
#     jjjj = [words[0] for words in makings]
#     print(jjjj)
#     yupp =[','.join(jjjj).replace(',','')]
#     print(yupp)




# # 초,중,종성 분해
# #  in_char = in_char - 0xAC00;
# #  //in_cho = in_char / (21 * 28);
# #  in_cho = in_char / (0x0015 * 0x001C);
# #  //in_jung = (in_char / 28) % 21;
# #  in_jung = (in_char / 0x001C) % 0x0015;
# #  //in_jong = in_char % 28;
# #  in_jong = in_char % 0x001C
#
# ch = ord(ch) - 0xAC00
#
# jong = ch % 28
#
# jung = ((ch - jong) / 28) % 21
#
# cho = (((ch - jong) / 28) - jung) / 21


#한글 유니코드 시작값 = 44032 // 끝값 = 55199
# 한글 코드 식(값 = (초성 * 21 + 중성) * 28 + 종성 + 0xAC00
# 한글 코드 값 = x
# 초성 인덱스 = (x - 44032) / (21 * 28)
# 중성 인덱스 = (x - 44032 - (초성 인덱스 * 21 * 28)) / 28
# 종성 인덱스 = (x - 44032 - (초성 인덱스 * 21 * 28) - (중성 인덱스 * 28))

base = 44032    #유니코드 0xAC00
first = 588 #초성 21*28
middle = 28 #중성

# 초성 0~18
first_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 중성 0~20
middle_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 종성 리스트. 0 ~ 27 + 1(1개 없음)
last_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

result = []
for makings in make:
    making_word = [words[0] for words in makings]
    print(making_word)
    m_word = [','.join(making_word).replace(',','')]
    print('이렇게? :',m_word)
    for wordz in m_word:
        for wordplz in wordz:
            print('제발좀: ', wordplz)
    # yaho = str(yupp)
    # print(ord(yaho))
            if re.match('.*[ㄱ-힣]+.*', wordplz) is not None: #in yaho: # ㄱ-힣 까지 공백문자를 포함해서 매치가 되는지 검사
                char_code = ord(wordplz) - base    #( x - 44032)

                # 초성인덱스
                cho_idx = int( char_code / first )
                result.append(first_list[cho_idx])
                print('초성:{}'.format(first_list[cho_idx]))

                # 중성인덱스
                middle_idx = int(( char_code - ( cho_idx * first )) / middle )

                result.append(middle_list[middle_idx])
                print('중성:{}'.format(middle_list[middle_idx]))

                # 종성인덱스
                # if wordplz
                last_idx = int( char_code - (cho_idx * first ) - ( middle_idx * middle))
                result.append(last_list[last_idx])
                print('종성:{}'.format(last_list[last_idx]))

            else:
                result.append(wordplz)
            print("".join(result))
