import controller
import keep_alive
import os

app = controller.init()
if os.environ.get('RENDER'):
    keep_alive.start()

@app.route("/")
def index():
    return controller.index()

@app.route("/update/<couleur>/<is_red>")
def update(couleur,is_red):
    return controller.update(couleur,is_red)

if __name__ == "__main__":
    app.run(debug=True)