from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

FILES_DIR = "/root/cdubz_flasker/cdflasker/files"

@app.route("/")
def index():
    return render_template("index.html")

# /root/cdubz_flasker/cdflasker/templates/shadow_wizard_money.jpg
# /root/cdubz_flasker/templates
@app.route("/<path:filename>")
def download_file(filename):
    return send_from_directory(
        FILES_DIR,
        filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)