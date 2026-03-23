import controller

app = controller.init()

@app.route("/")
def index():
    return controller.index()

@app.route("/update/<couleur>/<is_red>")
def update(couleur,is_red):
    return controller.update(couleur,is_red)

if __name__ == "__main__":
    app.run(debug=True)