from flask import Flask, jsonify, request
from storage import all_articles,liked_articles, not_liked_articles
from demographicFiltering import output

app=Flask(__name__)
@app.route("/")
def get_article():
    return jsonify({
        "data":all_articles[1:],
        "status":"success"
    })
@app.route("/liked-articles",methods=["POST"])
def liked_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201
@app.route("/not-liked-articles",methods=["POST"])
def not_liked_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201
@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        data = {
            "text": article[2],
            "url": article[0],
            "title": article[1],
            
            "lang": article[3],
            "total_events": article[4]
        }
        article_data.append(data)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200
if __name__=="__main__":
    app.run()
