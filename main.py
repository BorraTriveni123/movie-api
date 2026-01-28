from flask import Flask, request, jsonify

app = Flask(__name__)

movies = []
movie_id = 1

@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify(movies)

@app.route("/movies", methods=["POST"])
def add_movie():
    global movie_id
    data = request.json
    movie = {
        "id": movie_id,
        "name": data["name"],
        "rating": data["rating"]
    }
    movies.append(movie)
    movie_id += 1
    return jsonify(movie), 201

@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie(id):
    for movie in movies:
        if movie["id"] == id:
            data = request.json
            movie["name"] = data.get("name", movie["name"])
            movie["rating"] = data.get("rating", movie["rating"])
            return jsonify(movie)
    return {"error": "Movie not found"}, 404

@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    global movies
    movies = [m for m in movies if m["id"] != id]
    return {"message": "Movie deleted"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
