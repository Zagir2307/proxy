import os, urllib.request
from flask import Flask, request, Response

app = Flask(__name__)
HDR = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}

@app.route("/")
def relay():
    target = request.args.get("url", "")
    if not target.startswith("https://"):
        return Response("Bad URL", status=400)
    try:
        req = urllib.request.Request(target, headers=HDR)
        with urllib.request.urlopen(req, timeout=8) as resp:
            return Response(resp.read(), status=resp.status, content_type="application/json")
    except Exception as e:
        return Response(str(e), status=502)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
