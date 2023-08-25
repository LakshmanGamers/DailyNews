from flask import Flask, render_template, request
import requests
from datetime import date

app = Flask(__name__)

# Initialize date with today's date
current_date = str("2023-08-02")

@app.route('/', methods=['GET', 'POST'])
def get_news():
    global current_date
    titles = []
    description = []
    page_url = []
    image_url = []
    
    if request.method == "POST":
        new_date = request.form.get("new_date")
        if new_date:
            current_date = new_date

    data = requests.get(
        f"https://newsapi.org/v2/everything?q=Apple&from={current_date}&sortBy=popularity&apiKey=cdf47c8dfa1c44f6a091ce327825a53a"
    )
    res = data.json()["articles"]

    for i in res:
        titles.append(i["title"])
        description.append(i["description"])
        page_url.append(i["url"])
        image_url.append(i["urlToImage"])

    return render_template('index.html', info=[titles, description, page_url, image_url, current_date])

if __name__ == '__main__':
    app.run(debug=True)



