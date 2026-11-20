import json, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
tr=json.load(open('train.json')); te=json.load(open('test.json'))
classes=sorted(set(tr['labels']))
ytr=np.array([classes.index(l) for l in tr['labels']]); yte=np.array([classes.index(l) for l in te['labels']])
res={}
# keyword baseline: bag of words naive bayes
cv=CountVectorizer(lowercase=True, ngram_range=(1,1), min_df=1)
Xtr=cv.fit_transform(tr['texts']); Xte=cv.transform(te['texts'])
nb=MultinomialNB(alpha=0.3).fit(Xtr,ytr); P=nb.predict_proba(Xte)
res['keyword']=P
# embedding classifier: logistic regression on sentence embeddings
Etr=np.array(tr['emb']); Ete=np.array(te['emb'])
lr=LogisticRegression(C=10,max_iter=3000).fit(Etr,ytr); res['embedding']=lr.predict_proba(Ete)
for k,P in res.items():
    pred=P.argmax(1); conf=P.max(1); acc=(pred==yte).mean()
    print(k, 'acc', round(acc,4), 'mean conf', round(conf.mean(),3))
    for t in [0.5,0.7,0.8,0.9,0.95]:
        m=conf>=t; print('  t',t,'auto',round(m.mean(),3),'err among auto',round(1-(pred[m]==yte[m]).mean(),4))
np.save('Pk.npy',res['keyword']); np.save('Pe.npy',res['embedding'])
