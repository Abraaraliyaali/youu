from flask import Flask, render_template
import markdown2
import os

app = Flask(__name__)

@app.route("/wiki/<title>")
def show_entry(title):
    filepath = f"entries/{title}.md"
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            md = file.read()
        html = markdown2.markdown(md)
        return render_template("page.html", content=html, title=title)
    else:
        return "Page not found", 404

if __name__ == "__main__":
    app.run(debug=True)
