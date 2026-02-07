import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Disparos de Amor para Nastya", layout="wide", initial_sidebar_state="collapsed")

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.title("💫 Disparos de Amor no Universo 💖")
st.markdown("Te Amo, Nastya! ✨ Abre no telemóvel e vê os corações disparando!")

html_code = """
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<title>Disparos de Amor - Te Amo Nastya</title>
<style>
  body, html { margin:0; padding:0; height:100%; overflow:hidden; background: radial-gradient(ellipse at bottom, #0f0c29 0%, #302b63 50%, #24243e 100%); }
  .heart { position:absolute; width:22px; height:20px; background:#ff69b4; transform:rotate(-45deg); box-shadow:0 0 30px #ff1493; animation:disparo 10s infinite linear, batida 1.5s infinite; }
  .heart::before, .heart::after { content:""; position:absolute; width:22px; height:22px; background:#ff69b4; border-radius:50%; }
  .heart::before { top:-11px; left:0; } .heart::after { left:11px; top:0; }
  @keyframes disparo { 0% { transform:translateY(120vh) rotate(-45deg) scale(0.3); opacity:0; } 8% { opacity:1; } 92% { opacity:1; } 100% { transform:translateY(-40vh) rotate(-45deg) scale(1.3); opacity:0; } }
  @keyframes batida { 0%,100% { transform:scale(1) rotate(-45deg); } 50% { transform:scale(1.5) rotate(-45deg); } }
  #stars { position:absolute; inset:0; pointer-events:none; }
  .star { position:absolute; background:#fff; border-radius:50%; opacity:0.8; animation:twinkle 5s infinite alternate; }
  @keyframes twinkle { 0% { opacity:0.4; } 100% { opacity:1; } }
  .big-heart { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:400px; height:360px; z-index:5; }
  .small-heart { position:absolute; width:12px; height:12px; background:#ff69b4; transform:rotate(-45deg); box-shadow:0 0 12px #ff1493; animation:pulse-heart 4s infinite ease-in-out; }
  .small-heart::before, .small-heart::after { content:""; position:absolute; width:12px; height:12px; background:#ff69b4; border-radius:50%; }
  .small-heart::before { top:-6px; left:0; } .small-heart::after { left:6px; top:0; }
  @keyframes pulse-heart { 0%,100% { transform:rotate(-45deg) scale(0.8); opacity:0.8; } 50% { transform:rotate(-45deg) scale(1.2); opacity:1; } }
  .message { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); font-size:5em; color:#ff69b4; text-shadow:0 0 50px #ff1493, 0 0 100px #ff69b4; animation:glow 5s infinite alternate; z-index:10; pointer-events:none; white-space:nowrap; }
  @keyframes glow { from { text-shadow:0 0 30px #ff1493; } to { text-shadow:0 0 80px #ff1493, 0 0 120px #ff69b4; } }
</style>
</head>
<body>
  <div id="stars"></div>
  <div class="big-heart" id="bigHeart"></div>
  <div class="message">Te Amo, Nastya! 💖</div>

  <script>
    // Estrelas
    for (let i = 0; i < 250; i++) {
      const s = document.createElement('div');
      s.className = 'star';
      s.style.width = s.style.height = Math.random() * 4 + 1 + 'px';
      s.style.top = Math.random() * 100 + '%';
      s.style.left = Math.random() * 100 + '%';
      s.style.animationDelay = Math.random() * 5 + 's';
      document.getElementById('stars').appendChild(s);
    }

    // Corações disparando
    function disparo() {
      const h = document.createElement('div');
      h.className = 'heart';
      h.style.left = Math.random() * 100 + 'vw';
      h.style.animationDuration = (Math.random() * 7 + 8) + 's';
      document.body.appendChild(h);
      setTimeout(() => h.remove(), 15000);
    }
    setInterval(disparo, 150);

    // Coração grande formado por pequenos (shape clássico de coração)
    const container = document.getElementById('bigHeart');
    const num = 140;
    for (let i = 0; i < num; i++) {
      const ang = (i / num) * Math.PI * 2;
      const r = 0.8 + 0.3 * Math.sin(ang * 5) + 0.1 * Math.sin(ang * 10);
      const x = Math.cos(ang) * r * 160;
      const y = Math.sin(ang) * r * 140 - 70;
      const sh = document.createElement('div');
      sh.className = 'small-heart';
      sh.style.left = (x + 200 - 6) + 'px';
      sh.style.top = (y + 180 - 6) + 'px';
      sh.style.animationDelay = (i * 0.02) + 's';
      container.appendChild(sh);
    }
  </script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)

st.markdown("Se ainda preto, verifica os logs no Streamlit Cloud e manda aqui. Ou reboot de novo!")
