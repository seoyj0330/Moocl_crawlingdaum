# VA + ET 합치기


def chk(wordlist, idx, conList,final_list):
    if idx + 1 == len(wordlist) :
        print("끝지점 도달")
        print(idx+1)
        global global_index
        global_index  = idx
        return      #재귀에서 return은 함수를 끝내겠다는 뜻

    else :
        if wordlist[idx][1] == 'NNG' or wordlist[idx][1] == 'NNP' :
            if idx+1 < len(wordlist) and (wordlist[idx + 1][1] == 'NNG' or wordlist[idx+1][1] == 'NNP'):
                conList.append(wordlist[idx + 1])
                print('NNGNNG : ',conList)

                print("append 전 ",final_list)
                final_list.append(conList.copy())

                print("append 후 ",final_list)

                chk(wordlist, idx + 1, conList,final_list)

        elif wordlist[idx][1] == 'VA':
            if idx+1 < len(wordlist) and (wordlist[idx + 1][1] == 'NNG' or wordlist[idx+1][1] == 'NNP'):
                conList.append(wordlist[idx+1])
                print('VANNG : ', conList)

                print("append 전 ",final_list)
                final_list.append(conList.copy())
                print("append 후 ",final_list)

                chk(wordlist, idx + 1, conList,final_list)

                if idx+2 < len(wordlist) and (wordlist[idx + 2][1] == 'NNG' or wordlist[idx+2][1] == 'NNP') or wordlist[idx + 2][1] == 'MAG':
                    conList.append(wordlist[idx + 2])
                    print('야이러너넌너넌: ',conList)

                    print("append 전 ", final_list)
                    final_list.append(conList.copy())
                    print("append 후 ", final_list)


                    chk(wordlist, idx + 1, conList,final_list)

            elif wordlist[idx + 1][1] == 'ETM':
                conList.append(wordlist[idx + 1])
                # conList.append(wordlist[idx + 1] + wordlist[idx + 2])
                if idx+2 < len(wordlist) and (wordlist[idx + 2][1] == 'NNG'or wordlist[idx+2][1] == 'NNP'):
                    conList.append(wordlist[idx + 2])
                    print('VAETMNNG : ', conList)

                    print("append 전 ", final_list)
                    final_list.append(conList.copy())
                    print("append 후 ", final_list)

                    chk(wordlist, idx + 1, conList,final_list)

        elif wordlist[idx][1] == 'MAG':
            if idx+1 < len(wordlist) and wordlist[idx + 1][1] == 'VA':
                conList.append(wordlist[idx+1])
                print('MAGVA : ', conList)

                print("append 전 ",final_list)
                final_list.append(conList.copy())
                print("append 후 ",final_list)

                chk(wordlist, idx + 1, conList,final_list)





# def chk(wordlist):
#     for idx, word in enumerate(wordlist):
#         if idx + 1 == len(wordlist):
#             break
#         # nngindex = -1
#         if word[1] == 'NNG' :
#             # nngindex = idx
#             nextnngidx = -1
#             # print(word[0])
#             if wordlist[idx + 1][1] == 'NNG':
#                 nextnngidx = idx + 1
#                 print(word[0] + wordlist[idx+1][0])
#             elif wordlist[idx +1][1] == 'MAG':
#                 print(word[0]+wordlist[idx+1][0])
#         elif word[1] == 'VA' :
#             # print(word[0])
#             if wordlist[idx+1][1] == 'NNG':
#                 print(word[0] + wordlist[idx + 1][0])
#         elif word[1] == 'MAG':
#             print(word[0])
#             if wordlist[idx+1][1] == 'VA':
#                 print(word[0] + wordlist[idx+1][0])

