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

# ---------- Color palette ----------
def vivid_green_palette():
    """Green-purple vivid palette (matching your image style)"""
    return [
        (0.35, 0.85, 0.35, 0.45),  # bright green
        (0.6, 0.2, 0.6, 0.45),    # purple
        (0.45, 0.8, 0.5, 0.45),   # light green
        (0.75, 0.5, 0.8, 0.45),   # lilac
        (0.3, 0.6, 0.3, 0.45),    # deep green
    ]

# ---------- Poster generation ----------
def generate_poster(seed=None, layers=80, min_r=1.3, max_r=2.6, min_w=0.1, max_w=0.3):
    if seed:
        np.random.seed(seed)
        random.seed(seed)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.axis("off")
    ax.set_facecolor("white")

    palette = vivid_green_palette()

    for _ in range(layers):
        color = random.choice(palette)
        edge = (0, 0, 0, 0.25)  # soft gray outline
        r = random.uniform(min_r, max_r)
        x_center = random.uniform(-3.5, 3.5)
        y_center = random.uniform(-3.5, 3.5)
        wobble = random.uniform(min_w, max_w)
        x, y = spiky_blob(x_center, y_center, base_r=r, wobble=wobble)
        ax.fill(x, y, color=color, ec=edge, lw=0.4)

    # Title
    ax.text(-6.5, 6.5, "Generative Poster / Week 3 Arts & Advanced Big Data",
            fontsize=20, weight="bold", ha="left", va="top")

    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)
    return fig


# ---------- Sidebar Controls ----------
with st.sidebar:
    st.header("🎛️ Controls")
    layers = st.slider("Number of Layers", 40, 150, 80)
    min_r = st.slider("Minimum Radius", 0.5, 2.0, 1.3)
    max_r = st.slider("Maximum Radius", 1.5, 3.5, 2.6)
    min_w = st.slider("Minimum Wobble", 0.05, 0.3, 0.1)
    max_w = st.slider("Maximum Wobble", 0.15, 0.5, 0.3)
    seed = st.number_input("Random Seed (optional)", min_value=0, step=1)
    generate = st.button("🎨 Generate Poster")

# ---------- Main layout ----------
st.title("🎨 Generative Poster")
st.write("Week 3 • Arts & Advanced Big Data")

if generate:
    fig = generate_poster(seed if seed != 0 else None, layers, min_r, max_r, min_w, max_w)
    st.pyplot(fig, use_container_width=True)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300, bbox_inches="tight")
    st.download_button("💾 Download Poster (PNG)",
                       data=buf.getvalue(),
                       file_name="Week3_GenerativePoster.png",
                       mime="image/png")
else:
    st.info("Click **Generate Poster** to create your artwork.")

