import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Universo do Amor 💖 Nastya", layout="wide")

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.title("💫 Universo do Amor para Nastya 💖")
st.markdown("Te Amo, Nastya! ✨ Abre no teu telemóvel e vê os corações voando!")

nome = "Nastya"

html_code = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<title>Te Amo, {nome}!</title>
<style>
  body, html {{ margin:0; padding:0; height:100%; overflow:hidden; background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%); }}
  .heart {{ position:absolute; width:20px; height:20px; background:#ff69b4; transform:rotate(-45deg); box-shadow:0 0 20px #ff69b4; animation:float 8s infinite linear, pulse 2s infinite; }}
  .heart::before, .heart::after {{ content:""; position:absolute; width:20px; height:20px; background:#ff69b4; border-radius:50%; }}
  .heart::before {{ top:-10px; left:0; }} .heart::after {{ left:10px; top:0; }}
  @keyframes float {{ 0% {{ transform:translateY(100vh) rotate(-45deg); opacity:0; }} 10% {{ opacity:1; }} 90% {{ opacity:1; }} 100% {{ transform:translateY(-20vh) rotate(-45deg); opacity:0; }} }}
  @keyframes pulse {{ 0%,100% {{ transform:scale(1) rotate(-45deg); }} 50% {{ transform:scale(1.3) rotate(-45deg); }} }}
  #stars {{ position:absolute; top:0; left:0; right:0; bottom:0; pointer-events:none; }}
  .star {{ position:absolute; background:white; border-radius:50%; opacity:0.8; animation:twinkle 5s infinite; }}
  @keyframes twinkle {{ 0%,100% {{ opacity:0.4; }} 50% {{ opacity:1; }} }}
  .message {{ position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); font-size:3.5em; color:#ff69b4; text-shadow:0 0 25px #ff1493; animation:glow 3s infinite alternate; z-index:10; white-space:nowrap; }}
  @keyframes glow {{ from {{ text-shadow:0 0 10px #ff1493; }} to {{ text-shadow:0 0 40px #ff1493, 0 0 60px #ff69b4; }} }}
</style>
</head>
<body>
  <div class="message">Te Amo, {nome}! 💖✨</div>
  <div id="stars"></div>
  <script>
    const stars = document.getElementById('stars');
    for (let i = 0; i < 150; i++) {{
      const star = document.createElement('div');
      star.className = 'star';
      star.style.width = star.style.height = (Math.random() * 3 + 1) + 'px';
      star.style.top = Math.random() * 100 + '%';
      star.style.left = Math.random() * 100 + '%';
      star.style.animationDelay = Math.random() * 5 + 's';
      stars.appendChild(star);
    }}
    function createHeart() {{
      const heart = document.createElement('div');
      heart.className = 'heart';
      heart.style.left = Math.random() * 100 + 'vw';
      heart.style.animationDuration = (Math.random() * 5 + 6) + 's';
      document.body.appendChild(heart);
      setTimeout(() => heart.remove(), 12000);
    }}
    setInterval(createHeart, 400);
  </script>
</body>
</html>
"""

components.html(html_code, height=800, scrolling=False)

st.markdown("Manda este link para a Nastya! Funciona direto no browser do telemóvel dela ❤️")

