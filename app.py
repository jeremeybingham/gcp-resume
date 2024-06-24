from flask import Flask, render_template
import duckdb
import json

app = Flask(__name__)

# ensure duckdb table exists
con = duckdb.connect(database='incrementer.duckdb')
con.execute("CREATE TABLE IF NOT EXISTS incrementer (count INTEGER)")

# load initial value from hits.json or =0
try:
    with open('hits.json', 'r') as f:
        data = json.load(f)
        initial_count = data.get('count', 0)
except FileNotFoundError:
    initial_count = 0

# initialize count in DuckDB if doesn't exist
con.execute("INSERT INTO incrementer (count) SELECT ? WHERE NOT EXISTS (SELECT * FROM incrementer)", (initial_count,))


@app.route('/')
def hits():
    # increment DuckDB 
    con.execute("UPDATE incrementer SET count = count + 1")
    # fetch count
    current_count = con.execute("SELECT count FROM incrementer").fetchone()[0]
    # store in hits.json
    with open('hits.json', 'w') as f:
        json.dump({'count': current_count}, f)
    # output
    return render_template('index.html', current_count=current_count)


# serve the app 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)