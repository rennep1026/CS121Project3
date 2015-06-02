import json
import nltk
import collections

def snippet(termids, termlist: list):
    returnstring = ''
    for id in termids:
        returnstring += '...'
        surr_list = []
        if id in termlist:
            index = termlist.index(id)
            for i in range(index-3,index+3):
                if (i >= 0 and i<len(termlist)):
                    surr_list.append(termlist[i])
            for l in surr_list:
                returnstring+= id2term[str(l)] +" "
    return returnstring +'...'

if __name__ == '__main__':

    with open("index.json","r") as f:
        tfidf = json.load(f)

    #goes unused
    #with open('id2docfreq.json', 'r') as f:
    #    id2docfreq = json.load(f)

    with open('term2id.json', 'r') as f:
        term2id = json.load(f)

    with open('id2term.json', 'r') as f:
        id2term = json.load(f)
        
    with open('docid2url.json', 'r') as f:
        doc2url = json.load(f)
        
    with open('doc2termlist.json', 'r') as f:
        doc2termlist = json.load(f)

    
    user_input = ''
    while True:
        user_input = input("SEARCH : ")
        if user_input == ':quit':
            quit()
        tokens = nltk.tokenize.word_tokenize(user_input.lower())

        #lookup term id
        tid = []
        for t in tokens:
            if t in term2id:
                tid.append(term2id[t])

         #add tfidf
        score = collections.defaultdict(int)
        for id in tid:
            doc2score = tfidf[str(id)]
            for doc in doc2score:
                score[str(doc)] += doc2score[doc]

        sortedscores = collections.OrderedDict(sorted(score.items(), key=lambda t: t[1]))

        if len(sortedscores) == 0:
            print("No results found")
        else:
            for i in range(6):
                if len(sortedscores) > 0:
                    urlvalpair = sortedscores.popitem(True)
                    docid =urlvalpair[0]
                    url = doc2url[docid]
                    print(str(i) + ":" + url)
                    termlist = doc2termlist[int(docid)]
                    print(snippet(tid,doc2termlist[int(docid)]))
        print('\n\n')