from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

movies = [ {"id": 1, "title": "Grave of the Fireflies", "year": 1998, "genre": "Drama", "duration": "1h 29m", "type": "Local", "summary": "A young boy and his little sister struggle to survive in Japan during World War II.", "comments": []},
           {"id": 2, "title": "Tangled", "year": 2010, "genre": "Rom-Com", "duration": "1h 40m", "type": "Local", "summary": "The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief has stumbled upon her, she is about to discover the world for the first time, and who she really is.", "comments": []},
           {"id": 3, "title": "Soul", "year": 2020, "genre": "Comedy", "duration": "1h 40m", "type": "DASH", "summary": "Joe is a middle-school band teacher whose life hasn't quite gone the way he expected. His true passion is jazz. But when he travels to another realm to help someone find their passion, he soon discovers what it means to have soul.", "comments": []},
           {"id": 4, "title": "WALL·E", "year": 2008, "genre": "Adventure", "duration": "1h 38m", "type": "DASH", "summary": "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.", "comments": []},
           {"id": 5, "title": "Up", "year": 2009, "genre": "Drama", "duration": "1h 36m", "type": "CDN + DASH", "summary": "78-year-old Carl Fredricksen travels to Paradise Falls in his house equipped with balloons, inadvertently taking a young stowaway.", "comments": []},
           {"id": 6, "title": "Big Hero 6", "year": 2014, "genre": "Adventure", "duration": "1h 42m", "type": "CDN + HLS", "summary": "A special bond develops between plus-sized inflatable robot Baymax and prodigy Hiro Hamada, who together team up with a group of friends to form a band of high-tech heroes.", "comments": []}, ]

def load_comments(movie_id): #not operable
    comments_file = f'comments_{movie_id}.txt'
    if os.path.exists(comments_file):
        with open(comments_file, 'r') as file:
            return json.load(file)
    return []

def save_comments(movie_id, comments): #not operable
    comments_file = f'comments_{movie_id}.txt'
    with open(comments_file, 'w') as file:
        json.dump(comments, file)

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

@app.route('/movie/<int:id>', methods=['GET', 'POST'])
def movie(id):
    movie = next((m for m in movies if m['id'] == id), None)
    if not movie:
        return "Movie not found", 404

    if request.method == 'POST': #not operable
        comment = request.form['comment']
        comments = load_comments(id)
        comments.insert(0, {"comment": comment, "sentiment": "positive"})
        save_comments(id, comments)
        return redirect(url_for('movie', id=id))

    movie['comments'] = load_comments(id)
    return render_template(f'movie{id}.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
