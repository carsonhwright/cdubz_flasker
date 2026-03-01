import os

from flask import Flask, render_template, send_from_directory


app = Flask(__name__, template_folder="templates")

# FILES_DIR = "/root/cdubz_flasker/cdflasker/files"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "files")

@app.route("/")
def index():
    try:
        files = os.listdir(FILES_DIR)
    except FileNotFoundError:
        files = []
    files.sort()
    return render_template("index.html", files=files)

# /root/cdubz_flasker/cdflasker/templates/shadow_wizard_money.jpg
# /root/cdubz_flasker/templates
@app.route("/<path:filename>")
def serve_file(filename):
    return send_from_directory(
        FILES_DIR,
        filename,
        as_attachment=False #True if you want it to download
    )


# @app.route("/files/")
# def list_files():
#     files = os.listdir(FILES_DIR)
#     file_links = [f'<li><a href="/files/{f}" target="_blank">{f}</a></li>' for f in files]
#     return f"<h1>Files</h1><ul>{''.join(file_links)}</ul>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)