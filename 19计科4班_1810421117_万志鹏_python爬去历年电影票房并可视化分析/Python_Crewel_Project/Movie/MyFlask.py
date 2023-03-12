from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)

@app.route("/show1")
def show1():
    data = pd.read_csv("./finalMovieData.csv")
    data = data.rename(columns={"3":"value", "1":"name"})
    data = data.to_dict(orient="records")
    return render_template("showone.html", data = data)

@app.route("/show2")
def show2():
    data = pd.read_csv("./finalMovieData.csv")
    data1 = data['1'].tolist()
    data2 = data['3'].tolist()
    # print(data1)
    # print(data2)
    return render_template("showtwo.html", data1 = data1, data2 = data2)

@app.route("/show3")
def show3():
    data = pd.read_csv("./finalMovieData.csv")
    data = data.rename(columns={"3":"value", "1":"name"})
    data = data.to_dict(orient="records")
    # print(data)
    return render_template("showthree.html", data = data)

@app.route("/show4")
def show4():
    data = pd.read_csv("./finalMovieData.csv")
    data1 = data['1'].tolist()
    data2 = data['3'].tolist()
    # print(data1)
    # print(data2)
    return render_template("showfour.html", data1 = data1, data2 = data2)

if __name__ == "__main__":
    app.run()