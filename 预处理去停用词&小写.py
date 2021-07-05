def read_constraint():
    from nltk.corpus import stopwords
    en_stops = set(stopwords.words('english'))
    print('en_stops',en_stops)
    with open('./data/test_pla/constraint.txt', encoding='utf8') as file_obj:
        constraint_words = file_obj.read().replace('\n','').lower().split(" ")
        constraint_words_list=[]
        for word in constraint_words:
            if word not in en_stops:
                constraint_words_list.append(word)
                print(word)
        return constraint_words_list
