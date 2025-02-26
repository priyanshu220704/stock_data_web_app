from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load CSV file
df = pd.read_csv("dump.csv")

# Clean index names
df["index_name"] = df["index_name"].str.strip()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/indices")
def get_indices():
    """Return a list of unique index names from the CSV."""
    indices = df["index_name"].dropna().unique().tolist()
    return jsonify(indices)

@app.route("/data/<index_name>")
def get_index_data(index_name):
    """Return data for a specific index."""
    index_name = index_name.strip()  # Ensure clean comparison
    filtered_data = df[df["index_name"] == index_name]

    if filtered_data.empty:
        return jsonify({"error": "No data found"}), 404

    # Reverse the data so that dates appear in chronological order
    reversed_data = filtered_data.fillna(0).iloc[::-1]

    return jsonify(reversed_data.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
