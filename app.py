from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def home():   
    return render_template("home.html")


url = "https://ai-text-to-image-generator-flux-free-api.p.rapidapi.com/aaaaaaaaaaaaaaaaaiimagegenerator/quick.php"


headers = {
	"x-rapidapi-key": "ac84bc2e07mshba92f88283bf29ep1abeb4jsn6cee77a40c22",
	"x-rapidapi-host": "ai-text-to-image-generator-flux-free-api.p.rapidapi.com",
	"Content-Type": "application/json"
}

@app.route("/image",methods=["POST","GET"])
def image():
    image = None

    if request.method == "POST":
        prompt = request.form.get("prompt")

        payload = {
            "prompt": prompt,
            "style_id": 4,
            "size": "1-1"
        }

        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        print(data)

        if "final_result" in data and len(data["final_result"]) > 0:
            image_url = data["final_result"][0]["origin"]
    return render_template("img.html", image_url = image_url)




app.run(debug=True , port = 5001)