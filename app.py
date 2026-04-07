from flask import Flask, render_template, request, jsonify
from search.search_engine import SearchEngine

app = Flask(__name__)

engine = SearchEngine()


@app.route("/")
def home():
    return render_template("index.html")


# ✅ ADD THIS ROUTE
@app.route("/results")
def results_page():
    return render_template("results.html")


@app.route("/search", methods=["POST"])
def search():
    try:
        data = request.get_json()
        query = data.get("query")
        mode = data.get("mode", "semantic")  # NEW

        print("Query received:", query)

        if not query:
            return jsonify({"papers": []})

        papers = engine.search(query, mode=mode)

        print("First paper: ", papers[0])

        # Fix ObjectId
        for paper in papers:
            if "_id" in paper:
                paper["_id"] = str(paper["_id"])

        return jsonify({"papers": papers})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"papers": []})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)