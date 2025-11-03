import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random, io

# ---------- Page setup ----------
st.set_page_config(page_title="Week 3 • Arts & Advanced Big Data", layout="wide")

# ---------- Blob function ----------
def spiky_blob(xc, yc, base_r=1.0, wobble=0.25, spikes=150):
    ang = np.linspace(0, 2*np.pi, spikes)
    r = base_r * (1 + wobble * np.random.randn(spikes))
    x = xc + r * np.cos(ang)
    y = yc + r * np.sin(ang)
    return x, y

# ---------- Pastel palette ----------
def pastel_palette():
    return [
        (0.85, 0.95, 0.85, 0.6),  # mint green
        (0.8, 0.9, 0.95, 0.6),    # light blue
        (0.95, 0.9, 0.95, 0.6),   # pink
        (0.95, 0.95, 0.85, 0.6),  # pale yellow
        (0.85, 0.85, 0.95, 0.6),  # lavender
        (0.9, 0.95, 0.9, 0.6),    # light jade
    ]

# ---------- Generate Poster ----------
def generate_poster(seed=None, layers=60, min_r=1.2, max_r=3.0, min_w=0.1, max_w=0.3):
    if seed:
        np.random.seed(seed)
        random.seed(seed)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.axis("off")
    ax.set_facecolor("white")

    palette = pastel_palette()

    for _ in range(layers):
        color = random.choice(palette)
        edge_color = (0, 0, 0, 0.25)  # ✏️ 半透明描边
        r = random.uniform(min_r, max_r)
        x_center = random.uniform(-3.5, 3.5)
        y_center = random.uniform(-3.5, 3.5)
        wobble = random.uniform(min_w, max_w)
        x, y = spiky_blob(x_center, y_center, base_r=r, wobble=wobble)
        ax.fill(x, y, color=color, ec=edge_color, lw=0.6)  # ⬅️ 关键描边设置

    # Title text on poster
    ax.text(-6.5, 6.5, "Generative Poster / Week 3 Arts & Advanced Big Data",
            fontsize=20, weight="bold", ha="left", va="top")

    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)
    return fig

# ---------- Sidebar Controls ----------
with st.sidebar:
    st.header("🎨 Controls")
    style = st.selectbox("Select Poster Style", ["Pastel"])
    seed = st.number_input("Random Seed (optional)", min_value=0, step=1)
    generate = st.button("🎨 Generate Poster")

# ---------- Main Layout ----------
st.title("🎨 Generative Poster / Week 3 Arts & Advanced Big Data")
st.write("Create generative art posters with unique visual styles and download them as PNG.")

# ---------- Generate Poster ----------
if generate:
    fig = generate_poster(seed if seed != 0 else None)
    st.pyplot(fig, use_container_width=True)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300, bbox_inches="tight")
    st.download_button("💾 Download Poster (PNG)",
                       data=buf.getvalue(),
                       file_name="Week3_GenerativePoster_Pastel_Outline.png",
                       mime="image/png")
else:
    st.info("Click **Generate Poster** to create your artwork.")
