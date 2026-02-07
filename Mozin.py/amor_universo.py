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
    background: radial-gradient(ellipse at bottom, #0a0015 0%, #000 100%);
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
    opacity: 0.6;
    animation: twinkle 10s infinite alternate;
  }
  @keyframes twinkle {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 0.9; }
  }

  /* Borda rosa em cima com coraçõezinhos */
  .top-border {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 140px;
    background: linear-gradient(to bottom, #ff69b4, transparent);
    overflow: hidden;
    z-index: 5;
  }

  /* Corações piscando/espalhados pela tela toda */
  .sparkle-heart {
    position: absolute;
    width: 14px;
    height: 14px;
    background: #ff69b4;
    transform: rotate(-45deg);
    box-shadow: 0 0 15px #ff1493;
    opacity: 0;
    animation: sparkle 8s infinite ease-in-out;
  }
  .sparkle-heart::before,
  .sparkle-heart::after {
    content: "";
    position: absolute;
    width: 14px;
    height: 14px;
    background: #ff69b4;
    border-radius: 50%;
  }
  .sparkle-heart::before { top: -7px; left: 0; }
  .sparkle-heart::after { left: 7px; top: 0; }

  @keyframes sparkle {
    0%, 100% { opacity: 0; transform: scale(0.5) rotate(-45deg); }
    20%, 80% { opacity: 1; transform: scale(1.1) rotate(-45deg); }
    50% { opacity: 0.9; transform: scale(1.3) rotate(-45deg); }
  }

  /* Coração grande central feito de pequenos corações (fixo e pulsante) */
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
    animation: pulse-heart 4s infinite ease-in-out;
  }
  .small-heart::before,
  .small-heart::after {
    content: "";
    position: absolute;
    width: 10px;
    height: 10px;
    background: #ff69b4;
    border-radius: 50%;
  }
  .small-heart::before { top: -5px; left: 0; }
  .small-heart::after { left: 5px; top: 0; }
  @keyframes pulse-heart {
    0%, 100% { transform: rotate(-45deg) scale(0.8); opacity: 0.7; }
    50% { transform: rotate(-45deg) scale(1.3); opacity: 1; }
  }

  /* Texto centralizado abaixo do coração */
  .message {
    position: absolute;
    top: 65%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 4.5em;
    color: #ff69b4;
    text-shadow: 0 0 45px #ff1493, 0 0 90px #ff69b4;
    animation: glow 4.5s infinite alternate;
    z-index: 15;
    white-space: nowrap;
    pointer-events: none;
  }
  @keyframes glow {
    from { text-shadow: 0 0 30px #ff1493; }
    to   { text-shadow: 0 0 80px #ff1493, 0 0 130px #ff69b4; }
  }
</style>
</head>
<body>
  <div id="stars"></div>
  <div class="top-border" id="topBorder"></div>
  <div class="big-heart" id="bigHeart"></div>
  <div class="message">Te Amo, Nastya! 💖</div>

  <script>
    // Estrelas
    const stars = document.getElementById('stars');
    for (let i = 0; i < 220; i++) {
      const s = document.createElement('div');
      s.className = 'star';
      s.style.width = s.style.height = (Math.random() * 3 + 1) + 'px';
      s.style.top = Math.random() * 100 + '%';
      s.style.left = Math.random() * 100 + '%';
      s.style.animationDelay = Math.random() * 10 + 's';
      stars.appendChild(s);
    }

    // Coraçõezinhos na borda rosa de cima
    const top = document.getElementById('topBorder');
    for (let i = 0; i < 130; i++) {
      const h = document.createElement('div');
      h.className = 'sparkle-heart';
      h.style.left = Math.random() * 100 + '%';
      h.style.top = Math.random() * 100 + 'px';
      h.style.animationDelay = Math.random() * 6 + 's';
      top.appendChild(h);
    }

    // Corações piscando espalhados pela tela toda
    function createSparkle() {
      const h = document.createElement('div');
      h.className = 'sparkle-heart';
      h.style.left = Math.random() * 100 + 'vw';
      h.style.top = Math.random() * 100 + 'vh';
      h.style.animationDuration = (Math.random() * 5 + 8) + 's';
      h.style.animationDelay = Math.random() * 8 + 's';
      document.body.appendChild(h);
      setTimeout(() => h.remove(), 20000);
    }
    setInterval(createSparkle, 600); // Piscam suavemente pela tela

    // Coração grande central (feito de pequenos corações)
    const heartContainer = document.getElementById('bigHeart');
    const num = 110;
    for (let i = 0; i < num; i++) {
      const angle = (i / num) * Math.PI * 2;
      const r = 0.85 + 0.25 * Math.sin(angle * 5) + 0.1 * Math.sin(angle * 10);
      const x = Math.cos(angle) * r * 140;
      const y = Math.sin(angle) * r * 130 - 65;
      const sh = document.createElement('div');
      sh.className = 'small-heart';
      sh.style.left = (x + 190 - 5) + 'px';
      sh.style.top = (y + 170 - 5) + 'px';
      sh.style.animationDelay = (i * 0.03) + 's';
      heartContainer.appendChild(sh);
    }
  </script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)
