import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df=pd.read_csv("articles.csv")
count=CountVectorizer(stop_words="english")
count_matrix=count.fit_transform(df["title"])
cosin_sim2=cosine_similarity(count_matrix,count_matrix)
df=df.reset_index()
indices=pd.Series(df.index,index=df["contentId"])
def getRecommendation(title,cosin_sim):
  idx=indices[title]
  sim_scores=list(enumerate(cosin_sim[idx]))
  sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
  sim_scores=sim_scores[1:11]
  movie_indices=[i[0] for i in sim_scores]
  return df["original_title"].iloc[movie_indices]
