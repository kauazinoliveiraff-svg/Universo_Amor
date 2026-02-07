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
    background: #0a0015;
    font-family: Arial, sans-serif;
  }

  /* Estrelas de fundo */
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
    animation: twinkle 8s infinite alternate;
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

  /* Corações espalhados pela tela (aparecem e desaparecem) */
  .floating-heart {
    position: absolute;
    width: 16px;
    height: 16px;
    background: #ff69b4;
    transform: rotate(-45deg);
    box-shadow: 0 0 18px #ff1493;
    opacity: 0;
    animation: floatAndFade 12s infinite ease-in-out;
  }
  .floating-heart::before,
  .floating-heart::after {
    content: "";
    position: absolute;
    width: 16px;
    height: 16px;
    background: #ff69b4;
    border-radius: 50%;
  }
  .floating-heart::before { top: -8px; left: 0; }
  .floating-heart::after { left: 8px; top: 0; }

  @keyframes floatAndFade {
    0%   { opacity: 0; transform: translateY(100vh) rotate(-45deg) scale(0.6); }
    10%  { opacity: 0.9; }
    90%  { opacity: 0.9; }
    100% { opacity: 0; transform: translateY(-20vh) rotate(-45deg) scale(1.2); }
  }

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

  /* Texto centralizado */
  .message {
    position: absolute;
    top: 65%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 4.5em;
    color: #ff69b4;
    text-shadow: 0 0 45px #ff1493, 0 0 90px #ff69b4;
    animation: glow 4s infinite alternate;
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
    for (let i = 0; i < 180; i++) {
      const s = document.createElement('div');
      s.className = 'star';
      s.style.width = s.style.height = (Math.random() * 3 + 1) + 'px';
      s.style.top = Math.random() * 100 + '%';
      s.style.left = Math.random() * 100 + '%';
      s.style.animationDelay = Math.random() * 8 + 's';
      stars.appendChild(s);
    }

    // Coraçõezinhos na borda rosa de cima
    const top = document.getElementById('topBorder');
    for (let i = 0; i < 120; i++) {
      const h = document.createElement('div');
      h.className = 'top-heart';
      h.style.left = Math.random() * 100 + '%';
      h.style.top = Math.random() * 80 + 'px';
      top.appendChild(h);
    }

    // Corações espalhados pela tela (aparecem e somem)
    function createFloatingHeart() {
      const h = document.createElement('div');
      h.className = 'floating-heart';
      h.style.left = Math.random() * 100 + 'vw';
      h.style.top = Math.random() * 100 + 'vh';
      h.style.animationDelay = Math.random() * 8 + 's';
      document.body.appendChild(h);
      setTimeout(() => h.remove(), 15000);
    }
    setInterval(createFloatingHeart, 400); // Aparecem e somem suavemente

    // Coração grande central (sem estrela)
    const heartContainer = document.getElementById('bigHeart');
    const num = 100;
    for (let i = 0; i < num; i++) {
      const angle = (i / num) * Math.PI * 2;
      const r = 0.8 + 0.28 * Math.sin(angle * 5) + 0.12 * Math.sin(angle * 10);
      const x = Math.cos(angle) * r * 140;
      const y = Math.sin(angle) * r * 120 - 60;
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

st.markdown("Pronto! Copia este código inteiro, substitui o teu ficheiro no GitHub, faz commit e reboot no Streamlit. Deve ficar exatamente como na imagem: corações espalhados pela tela que aparecem e somem, borda rosa em cima, coração grande central atrás do texto, sem estrela. Se ainda não ficar certo, diz o que falta que ajustamos mais! 💖")
