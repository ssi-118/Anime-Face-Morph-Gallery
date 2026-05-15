import os
import random
from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

MORPHS_DIR = os.path.join(app.static_folder, "morphs")

def get_morphs():
    morphs = []

    for morph_folder in os.listdir(MORPHS_DIR):
        folder_path = os.path.join(MORPHS_DIR, morph_folder)

        if not os.path.isdir(folder_path):
            continue

        frames = [
            f for f in os.listdir(folder_path)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
        ]

        frames.sort()

        if frames:
            frame_urls = [
                url_for("static", filename=f"morphs/{morph_folder}/{frame}")
                for frame in frames
            ]

            morphs.append({
                "id": morph_folder,
                "frames": frame_urls
            })

    return morphs

PANEL_SIZES = ["small", "small", "small", "small", "medium", "wide", "tall"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/panels")
def get_panels():
    morphs = get_morphs()
    panels = []

    for _ in range(60):
        morph = random.choice(morphs)
        frame_index = random.randint(0, len(morph["frames"]) - 1)

        panels.append({
            "image_url": morph["frames"][frame_index],
            "frames": morph["frames"],
            "size": random.choice(PANEL_SIZES),
            "morph_id": morph["id"]
        })

    return jsonify({"panels": panels})

if __name__ == "__main__":
    app.run(debug=True)
