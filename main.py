from flask import Flask, request, render_template, jsonify
import requests, random

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    joke_response = requests.get("https://api.chucknorris.io/jokes/random")
    joke_data = joke_response.json()

    category_response = requests.get("https://api.chucknorris.io/jokes/categories")
    categories = category_response.json()

    joke = joke_data["value"]
    image_url = joke_data["icon_url"]

    if request.method == "POST":
        if "kat" in request.form:  # pārbauda vai nospiestā poga ir par joka kategoriju
            category = request.form["kat"]
            joke_response = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
            joke_data = joke_response.json()
            joke = joke_data["value"]
            image_url = joke_data["icon_url"]
        
        elif "query" in request.form:  # pārbauda vai jāmeklē joks
            query = request.form["query"]
            search_response = requests.get(f"https://api.chucknorris.io/jokes/search?query={query}")
            search_results = search_response.json()

            if search_results["total"] > 0:
                random_joke = random.choice(search_results["result"])  # no atrastajiem jokiem izvēlas random joku
                joke = random_joke["value"]
                image_url = random_joke["icon_url"]
            else:
                joke = "No jokes found for that phrase."
                image_url = "https://api.chucknorris.io/img/chucknorris_logo_coloured_small@2x.png"

    return render_template("index.html", joks=joke, bilde=image_url, kategorijas=categories)



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

