import datetime
date_test = '2011.12.11'
date_test2 = '2002.11.22'
date_test3 = '2011.05'

min = ''
 # 10월 18일

print(date_test)
if date_test3.count(".") == 1 :
    test3 = datetime.datetime.strptime(date_test3, '%Y.%m')
else :
    test3 = datetime.datetime.strptime(date_test3, '%Y.%m.%d')

test =  datetime.datetime.strptime(date_test, '%Y.%m.%d')
test2 = datetime.datetime.strptime(date_test2, '%Y.%m.%d')
# test3 = datetime.datetime.strptime(date_test3, '%Y.%m.%d')





print(test3)
print(test > test2)