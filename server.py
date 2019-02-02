from flask import Flask, request, redirect, send_from_directory

app = Flask(__name__)


@app.route("/report", methods=["POST"])
def report():
    print(request.get_json())
    return ""


@app.route("/firmware", methods=["get"])
def determine_firmware():
    return redirect("firmware/fwuppoc.fw")


@app.route("/firmware/<path:filename>", methods=["get"])
def serve_fw(filename):
    return send_from_directory("firmwares/", filename, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
