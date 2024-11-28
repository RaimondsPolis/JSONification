from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    atbilde = requests.get("https://api.chucknorris.io/jokes/random")
    joks = atbilde.json()
    atbilde = requests.get("https://api.chucknorris.io/jokes/categories")
    kategorijas = atbilde.json()

    if request.method == "POST":
        kategorija = request.form["kat"]
        atbilde = requests.get(f"https://api.chucknorris.io/jokes/random?category={kategorija}")
        joks = atbilde.json()

    return render_template("index.html", joks = joks["value"], bilde = joks["icon_url"],kategorijas = kategorijas)

@app.route("/uni")
def uni():
    atbilde = requests.get("http://universities.hipolabs.com/search?country=latvia")
    visas = atbilde.json()
    nosaukumi = []
    print(visas[0]["web_pages"][0]) #izprintē tikai 
    for elements in visas:
        pieliekamais = {
            "nosaukums": elements["name"],
            "majaslapa": elements["web_pages"]
        
        }
        nosaukumi.append(pieliekamais)
    
    return render_template("uni.html", uni = nosaukumi)



@app.route("/chats")
def chats():
    return render_template("chats.html")


@app.route("/suutiit", methods = ["POST"])
def suutiit():
    sanemtais = request.json
    if sanemtais["saturs"] == "\clear":
        with open("chataZinas.txt", "w") as f:
            f.write("")
        return "Izdzests"

    with open("chataZinas.txt", "a") as f:
        f.write(sanemtais["vards"])
        f.write("----")
        f.write(sanemtais["saturs"])
        f.write("\n")
    return jsonify("OK")

@app.route("/jschats/lasiit")
def lasit():
    saturs = []
    with open("chataZinas.txt", "r") as f:
        saturs = f.readlines()
    return saturs


if __name__ == '__main__':
    app.run(port=5000)

