import json, numpy as np
tr=json.load(open('train.json')); te=json.load(open('test.json'))
classes=sorted(set(tr['labels']))
y=[classes.index(l) for l in te['labels']]
Pk=np.load('Pk.npy'); Pe=np.load('Pe.npy')
def pack(P):
    o=np.argsort(-P,1)
    return [[int(o[i,0]),round(float(P[i,o[i,0]]),4),int(o[i,1])] for i in range(len(P))]
k=pack(Pk); e=pack(Pe)
rows=[[te['texts'][i],y[i],k[i][0],k[i][1],k[i][2],e[i][0],e[i][1],e[i][2]] for i in range(len(y))]
out={"source":"Banking77 (PolyAI, CC BY 4.0), test split","intents":classes,"trainSize":len(tr['texts']),
 "models":{"keyword":"Keyword baseline: naive Bayes on word counts","embedding":"AI classifier: sentence embeddings + logistic regression"},
 "cols":["text","truth","kw_pred","kw_conf","kw_second","em_pred","em_conf","em_second"],"rows":rows}
s=json.dumps(out,separators=(',',':'),ensure_ascii=False)
open('../data/results.json','w').write(s); print(len(s)//1024,'KB')
