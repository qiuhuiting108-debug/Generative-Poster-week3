import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random, io

# ---------- Page setup ----------
st.set_page_config(page_title="Generative Poster / Week 3 Arts & Advanced Big Data", layout="wide")

# ---------- Spiky blob ----------
def spiky_blob(xc, yc, base_r=1.0, spikes=260, jitter=0.5):
    ang = np.linspace(0, 2*np.pi, spikes)
    r = base_r * (1 + jitter * np.random.randn(spikes))
    x = xc + r * np.cos(ang)
    y = yc + r * np.sin(ang)
    return x, y

# ---------- Color palette ----------
def complex_palette():
    return [
        (0.3, 0.8, 0.3, 0.6),   # green
        (0.6, 0.2, 0.7, 0.5),   # purple
        (0.4, 0.9, 0.4, 0.7),   # light green
        (0.7, 0.3, 0.8, 0.5),   # violet
        (0.2, 0.7, 0.5, 0.6),   # teal
        (0.8, 0.9, 0.8, 0.4)    # pale green
    ]

# ---------- Generate poster ----------
def generate_poster(seed=None):
    if seed:
        np.random.seed(seed)
        random.seed(seed)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.axis("off")
    ax.set_facecolor("white")
    palette = complex_palette()

    # dense spiky composition
    for i in range(100):
        color = random.choice(palette)
        r = random.uniform(3.0, 4.0)
        jitter = random.uniform(0.3, 0.6)
        x, y = spiky_blob(random.gauss(0, 0.5), random.gauss(0, 0.5),
                          base_r=r, spikes=260, jitter=jitter)
        ax.fill(x, y, color=color, ec="none")

    # Title text
    ax.text(-6, 6.3, "Generative Poster", fontsize=26, weight="bold", ha="left", va="top")
    ax.text(-6, 5.6, "Week 3 • Arts & Advanced Big Data", fontsize=16,
            style="italic", ha="left", va="top")

    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)
    return fig

# ---------- Sidebar Controls ----------
with st.sidebar:
    st.header("🎨 Controls")
    style = st.selectbox("Select Poster Style", ["Complex Composition"], index=0)
    seed = st.number_input("Random Seed (optional)", min_value=0, step=1)
    generate = st.button("🎨 Generate Poster")

# ---------- Main layout ----------
st.title("🎨 Generative Poster Generator")
st.write("Create generative art posters with unique visual styles and download them as PNG.")

# ---------- Only show when button clicked ----------
if generate:
    fig = generate_poster(seed if seed != 0 else None)
    st.pyplot(fig, use_container_width=True)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300, bbox_inches="tight")
    st.download_button("💾 Download Poster (PNG)",
                       data=buf.getvalue(),
                       file_name="Week3_GenerativePoster.png",
                       mime="image/png")
else:
    st.info("⬅️ Adjust the settings and click **Generate Poster** to create your artwork.")
