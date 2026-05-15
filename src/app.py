import os
import random
from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

MORPHS_DIR = os.path.join(app.static_folder, "morphs")
VALID_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")

PANEL_SIZES = [
    "small", "small", "small", "small",
    "medium", "wide", "tall"
]

def load_morphs_once():
    morphs = []

    if not os.path.exists(MORPHS_DIR):
        print("Morphs folder not found:", MORPHS_DIR)
        return morphs

    for morph_folder in os.listdir(MORPHS_DIR):
        folder_path = os.path.join(MORPHS_DIR, morph_folder)

        if not os.path.isdir(folder_path):
            continue

        frames = [
            frame for frame in os.listdir(folder_path)
            if frame.lower().endswith(VALID_EXTENSIONS)
        ]

        frames.sort()

        if len(frames) < 2:
            continue

        frame_urls = [
            f"/static/morphs/{morph_folder}/{frame}"
            for frame in frames
        ]

        morphs.append({
            "id": morph_folder,
            "frames": frame_urls
        })

    print("Morph folders loaded:", len(morphs))
    return morphs

MORPHS = load_morphs_once()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/panels")
def get_panels():
    if not MORPHS:
        return jsonify({"panels": []})

    panels = []

    for _ in range(40):
        morph = random.choice(MORPHS)
        image_url = random.choice(morph["frames"])

        panels.append({
            "image_url": image_url,
            "frames": morph["frames"],
            "size": random.choice(PANEL_SIZES),
            "morph_id": morph["id"]
        })

    return jsonify({"panels": panels})

if __name__ == "__main__":
    app.run(debug=True)
