
html_code = """
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<title>Disparos de Amor - Te Amo Nastya</title>
<style>
  body, html { margin:0; padding:0; height:100%; overflow:hidden; background: radial-gradient(ellipse at bottom, #0f0c29 0%, #302b63 50%, #24243e 100%); }
  .heart { position:absolute; width:20px; height:18px; background:#ff69b4; transform:rotate(-45deg); box-shadow:0 0 25px #ff1493; animation:disparo 9s infinite linear, batida 1.6s infinite; }
  .heart::before, .heart::after { content:""; position:absolute; width:20px; height:20px; background:#ff69b4; border-radius:50%; }
  .heart::before { top:-10px; left:0; } .heart::after { left:10px; top:0; }
  @keyframes disparo { 0% { transform:translate(var(--sx), 130vh) rotate(-45deg) scale(0.4); opacity:0; } 10% { opacity:1; } 90% { opacity:0.9; } 100% { transform:translate(var(--ex), -50vh) rotate(-45deg) scale(1.4); opacity:0; } }
  @keyframes batida { 0%,100% { transform:scale(1) rotate(-45deg); } 50% { transform:scale(1.45) rotate(-45deg); } }
  #stars { position:absolute; inset:0; pointer-events:none; }
  .star { position:absolute; background:#fff; border-radius:50%; opacity:0.85; animation:twinkle 5s infinite alternate; }
  @keyframes twinkle { 0% { opacity:0.35; } 100% { opacity:1; } }
  .big-heart { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:380px; height:340px; z-index:5; }
  .small-heart { position:absolute; width:10px; height:10px; background:#ff69b4; transform:rotate(-45deg); box-shadow:0 0 12px #ff1493; animation:pulse-heart 3.2s infinite ease-in-out; }
  .small-heart::before, .small-heart::after { content:""; position:absolute; width:10px; height:10px; background:#ff69b4; border-radius:50%; }
  .small-heart::before { top:-5px; left:0; } .small-heart::after { left:5px; top:0; }
  @keyframes pulse-heart { 0%,100% { transform:rotate(-45deg) scale(0.75); opacity:0.7; } 50% { transform:rotate(-45deg) scale(1.25); opacity:1; } }
  .message { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); font-size:4.8em; color:#ff69b4; text-shadow:0 0 45px #ff1493, 0 0 90px #ff69b4; animation:glow 4.5s infinite alternate; z-index:10; pointer-events:none; white-space:nowrap; }
  @keyframes glow { from { text-shadow:0 0 25px #ff1493; } to { text-shadow:0 0 70px #ff1493, 0 0 110px #ff69b4; } }
</style>
</head>
<body>
  <div id="stars"></div>
  <div class="big-heart" id="bigHeart"></div>
  <div class="message">Te Amo, Nastya! 💖</div>

  <script>
    // Estrelas twinkling
    for (let i = 0; i < 220; i++) {
      const s = document.createElement('div');
      s.className = 'star';
      s.style.width = s.style.height = Math.random() * 3 + 1 + 'px';
      s.style.top = Math.random() * 100 + '%';
      s.style.left = Math.random() * 100 + '%';
      s.style.animationDelay = Math.random() * 5 + 's';
      document.getElementById('stars').appendChild(s);
    }

    // Corações disparados dos cantos e fundo
    function dispararCoracao() {
      const h = document.createElement('div');
      h.className = 'heart';
      const side = Math.random();
      let sx = '0%', ex = '0%';
      if (side < 0.33) { sx = '-10%'; ex = '130vw'; } // Esquerda
      else if (side < 0.66) { sx = '110%'; ex = '-130vw'; } // Direita
      else { sx = Math.random() * 100 + '%'; ex = (Math.random() * 80 - 40) + 'vw'; } // Fundo
      h.style.left = sx;
      h.style.setProperty('--sx', sx);
      h.style.setProperty('--ex', ex);
      h.style.animationDuration = (Math.random() * 5 + 7) + 's';
      document.body.appendChild(h);
      setTimeout(() => h.remove(), 12000);
    }
    setInterval(dispararCoracao, 200); // Ritmo bom, sem sobrecarregar

    // Coração central grande formado por pequenos corações (sem estrela, só coração cheio)
    const container = document.getElementById('bigHeart');
    const numHearts = 120; // Cheio mas leve para funcionar
    for (let i = 0; i < numHearts; i++) {
      const ang = (i / numHearts) * Math.PI * 2;
      const r = 0.85 + 0.25 * Math.sin(ang * 5) + 0.12 * Math.sin(ang * 10); // Shape coração clássico
      const x = Math.cos(ang) * r * 150;
      const y = Math.sin(ang) * r * 130 - 65;
      const sh = document.createElement('div');
      sh.className = 'small-heart';
      sh.style.left = (x + 190 - 5) + 'px';
      sh.style.top = (y + 170 - 5) + 'px';
      sh.style.animationDelay = (i * 0.025) + 's';
      container.appendChild(sh);
    }
  </script>
</body>
</html>
"""
