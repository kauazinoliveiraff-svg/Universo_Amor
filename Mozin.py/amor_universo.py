import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Te Amo Nastya 💖", layout="wide", initial_sidebar_state="collapsed")

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<title>Te Amo, Nastya! 💖</title>
<style>
  body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    overflow: hidden;
    background: radial-gradient(ellipse at bottom, #0f001a 0%, #000 100%);
    font-family: Arial, sans-serif;
  }

  /* Estrelas no fundo */
  #stars {
    position: absolute;
    inset: 0;
    pointer-events: none;
  }
  .star {
    position: absolute;
    background: #fff;
    border-radius: 50%;
    opacity: 0.7;
    animation: twinkle 6s infinite alternate;
  }
  @keyframes twinkle {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 1; }
  }

  /* Borda rosa em cima com coraçõezinhos espalhados */
  .top-border {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 120px;
    background: linear-gradient(to bottom, #ff69b4, transparent);
    overflow: hidden;
    z-index: 5;
  }
  .top-heart {
    position: absolute;
    width: 14px;
    height: 14px;
    background: #ff69b4;
    transform: rotate(-45deg);
    box-shadow: 0 0 15px #ff1493;
    opacity: 0.9;
  }
  .top-heart::before, .top-heart::after {
    content: "";
    position: absolute;
    width: 14px;
    height: 14px;
    background: #ff69b4;
    border-radius: 50%;
  }
  .top-heart::before { top: -7px; left: 0; }
  .top-heart::after { left: 7px; top: 0; }

  /* Coração grande central feito de pequenos corações */
  .big-heart {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 380px;
    height: 340px;
    z-index: 10;
  }
  .small-heart {
    position: absolute;
    width: 10px;
    height: 10px;
    background: #ff69b4;
    transform: rotate(-45deg);
    box-shadow: 0 0 12px #ff1493;
    animation: pulse 3.5s infinite ease-in-out;
  }
  .small-heart::before, .small-heart::after {
    content: "";
    position: absolute;
    width: 10px;
    height: 10px;
    background: #ff69b4;
    border-radius: 50%;
  }
  .small-heart::before { top: -5px; left: 0; }
  .small-heart::after { left: 5px; top: 0; }
  @keyframes pulse {
    0%, 100% { transform: rotate(-45deg) scale(0.8); opacity: 0.7; }
    50% { transform: rotate(-45deg) scale(1.25); opacity: 1; }
  }

  /* Texto centralizado abaixo do coração */
  .message {
    position: absolute;
    top: 65%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 4.2em;
    color: #ff69b4;
    text-shadow: 0 0 40px #ff1493, 0 0 80px #ff69b4;
    animation: glow 4s infinite alternate;
    z-index: 15;
    white-space: nowrap;
    pointer-events: none;
  }
  @keyframes glow {
    from { text-shadow: 0 0 25px #ff1493; }
    to { text-shadow: 0 0 70px #ff1493, 0 0 110px #ff69b4; }
  }
</style>
</head>
<body>
  <div id="stars"></div>
  <div class="top-border" id="topBorder"></div>
  <div class="big-heart" id="bigHeart"></div>
  <div class="message">Te Amo, Nastya! 💖</div>

  <script>
    // Estrelas no fundo
    const starsContainer = document.getElementById('stars');
    for (let i = 0; i < 200; i++) {
      const star = document.createElement('div');
      star.className = 'star';
      star.style.width = star.style.height = (Math.random() * 3 + 1) + 'px';
      star.style.top = Math.random() * 100 + '%';
      star.style.left = Math.random() * 100 + '%';
      star.style.animationDelay = Math.random() * 6 + 's';
      starsContainer.appendChild(star);
    }

    // Coraçõezinhos espalhados na borda rosa de cima
    const topContainer = document.getElementById('topBorder');
    for (let i = 0; i < 80; i++) {
      const heart = document.createElement('div');
      heart.className = 'top-heart';
      heart.style.left = Math.random() * 100 + '%';
      heart.style.top = Math.random() * 80 + 'px';
      heart.style.animationDelay = Math.random() * 3 + 's';
      topContainer.appendChild(heart);
    }

    // Coração grande central formado por pequenos corações
    const heartContainer = document.getElementById('bigHeart');
    const numHearts = 110; // cheio mas leve
    for (let i = 0; i < numHearts; i++) {
      const angle = (i / numHearts) * Math.PI * 2;
      const r = 0.8 + 0.3 * Math.sin(angle * 5) + 0.1 * Math.sin(angle * 10);
      const x = Math.cos(angle) * r * 150;
      const y = Math.sin(angle) * r * 130 - 65;
      const small = document.createElement('div');
      small.className = 'small-heart';
      small.style.left = (x + 190 - 5) + 'px';
      small.style.top = (y + 170 - 5) + 'px';
      small.style.animationDelay = (i * 0.025) + 's';
      heartContainer.appendChild(small);
    }
  </script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)



