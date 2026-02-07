html_code = """
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<title>Disparos de Amor - Te Amo Nastya</title>
<style>
  body, html { margin:0; padding:0; height:100%; overflow:hidden; background: radial-gradient(circle at bottom, #0a0015 0%, #000 100%); }
  .heart { position:absolute; width:20px; height:18px; background:#ff3366; transform:rotate(-45deg); box-shadow:0 0 25px #ff0066; animation:disparo 8s infinite linear, batida 1.4s infinite; }
  .heart::before, .heart::after { content:""; position:absolute; width:20px; height:20px; background:#ff3366; border-radius:50%; }
  .heart::before { top:-10px; left:0; } .heart::after { left:10px; top:0; }
  @keyframes disparo { 0% { transform:translate(var(--sx), 120vh) rotate(-45deg) scale(0.5); opacity:0; } 10% { opacity:1; } 90% { opacity:0.9; } 100% { transform:translate(var(--ex), -40vh) rotate(-45deg) scale(1.4); opacity:0; } }
  @keyframes batida { 0%,100% { transform:scale(1) rotate(-45deg); } 50% { transform:scale(1.5) rotate(-45deg); } }
  #stars { position:absolute; inset:0; pointer-events:none; }
  .star { position:absolute; background:#fff; border-radius:50%; opacity:0.8; animation:twinkle 4-7s infinite; }
  @keyframes twinkle { 0%,100% { opacity:0.3; } 50% { opacity:1; } }
  .big-heart { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:420px; height:380px; z-index:5; }
  .small-heart { position:absolute; width:11px; height:11px; background:#ff3366; transform:rotate(-45deg); box-shadow:0 0 15px #ff0066; animation:pulse-heart 3s infinite ease-in-out; }
  .small-heart::before, .small-heart::after { content:""; position:absolute; width:11px; height:11px; background:#ff3366; border-radius:50%; }
  .small-heart::before { top:-5.5px; left:0; } .small-heart::after { left:5.5px; top:0; }
  @keyframes pulse-heart { 0%,100% { transform:rotate(-45deg) scale(0.8); opacity:0.7; } 50% { transform:rotate(-45deg) scale(1.3); opacity:1; } }
  .message { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); font-size:5em; color:#ff69b4; text-shadow:0 0 50px #ff0066, 0 0 100px #ff3366; animation:glow 4s infinite alternate; z-index:10; pointer-events:none; white-space:nowrap; }
  @keyframes glow { from { text-shadow:0 0 30px #ff0066; } to { text-shadow:0 0 90px #ff0066, 0 0 140px #ff3366; } }
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
      s.style.width = s.style.height = Math.random() * 3 + 1 + 'px';
      s.style.top = Math.random() * 100 + '%';
      s.style.left = Math.random() * 100 + '%';
      s.style.animationDelay = Math.random() * 4 + 's';
      document.getElementById('stars').appendChild(s);
    }

    // Corações disparados dos cantos/baixo com direção variada
    function disparar() {
      const h = document.createElement('div');
      h.className = 'heart';
      const side = Math.random();
      let startX = '0%';
      let endX = '0%';
      if (side < 0.3) { startX = '-10%'; endX = '120vw'; } // Esquerda → direita
      else if (side < 0.6) { startX = '110%'; endX = '-120vw'; } // Direita → esquerda
      else { startX = Math.random() * 100 + '%'; endX = (Math.random() * 60 - 30) + 'vw'; } // Baixo → cima variado
      h.style.left = startX;
      h.style.setProperty('--sx', startX);
      h.style.setProperty('--ex', endX);
      h.style.animationDuration = (Math.random() * 4 + 6) + 's';
      document.body.appendChild(h);
      setTimeout(() => h.remove(), 10000);
    }
    setInterval(disparar, 120); // Ritmo intenso como no vídeo

    // Coração central grande cheio de pequenos corações (tudoooo pulsando)
    const container = document.getElementById('bigHeart');
    const num = 150; // Cheio mas otimizado para não travar
    for (let i = 0; i < num; i++) {
      const ang = (i / num) * Math.PI * 2;
      const heartR = 16 * (Math.sin(ang * 5) + 0.7 * Math.sin(ang * 10)); // Shape clássico de coração
      const r = heartR * (0.7 + 0.3 * Math.sin(ang * 4));
      const x = Math.cos(ang) * r * 170;
      const y = Math.sin(ang) * r * 150 - 75;
      const sh = document.createElement('div');
      sh.className = 'small-heart';
      sh.style.left = (x + 210 - 5.5) + 'px';
      sh.style.top = (y + 190 - 5.5) + 'px';
      sh.style.animationDelay = (i * 0.02) + 's';
      container.appendChild(sh);
    }
  </script>
</body>
</html>
"""
