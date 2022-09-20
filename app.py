from flask import Flask, render_template, request
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

data = pd.read_json("Data/entries.json")
df = data['entries'].apply(pd.Series)#.set_index("API")

app = Flask(__name__)

@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('home.html',
                           tables=[df.to_html(classes='table table-bordered" id="myTable',
                                              render_links=True)],
                           titles=df.columns.values,
                           data=list(df.Category.unique())
                           )

if __name__ == "__main__":
    app.run(debug=True, port=3000)















