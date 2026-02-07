html_code = """
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<title>Disparos de Amor - Te Amo Nastya</title>
<style>
  body, html { margin:0; padding:0; height:100%; overflow:hidden; background: radial-gradient(ellipse at bottom, #0f0c29 0%, #302b63 50%, #24243e 100%); }
  .heart { position:absolute; width:18px; height:16px; background:#ff69b4; transform:rotate(-45deg); box-shadow:0 0 20px #ff1493; animation:disparo 8s infinite linear, batida 1.8s infinite; }
  .heart::before, .heart::after { content:""; position:absolute; width:18px; height:18px; background:#ff69b4; border-radius:50%; }
  .heart::before { top:-9px; left:0; } .heart::after { left:9px; top:0; }
  @keyframes disparo { 0% { transform:translate(var(--sx), 120vh) rotate(-45deg) scale(0.5); opacity:0; } 10% { opacity:1; } 90% { opacity:0.9; } 100% { transform:translate(var(--ex), -30vh) rotate(-45deg) scale(1.3); opacity:0; } }
  @keyframes batida { 0%,100% { transform:scale(1) rotate(-45deg); } 50% { transform:scale(1.4) rotate(-45deg); } }
  #stars { position:absolute; inset:0; pointer-events:none; }
  .star { position:absolute; background:#fff; border-radius:50%; opacity:0.7; animation:twinkle 6s infinite alternate; }
  @keyframes twinkle { 0% { opacity:0.3; } 100% { opacity:1; } }
  .big-heart { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:320px; height:280px; z-index:5; }
  .small-heart { position:absolute; width:9px; height:9px; background:#ff69b4; transform:rotate(-45deg); box-shadow:0 0 10px #ff1493; animation:pulse-heart 3s infinite ease-in-out; }
  .small-heart::before, .small-heart::after { content:""; position:absolute; width:9px; height:9px; background:#ff69b4; border-radius:50%; }
  .small-heart::before { top:-4.5px; left:0; } .small-heart::after { left:4.5px; top:0; }
  @keyframes pulse-heart { 0%,100% { transform:rotate(-45deg) scale(0.8); opacity:0.7; } 50% { transform:rotate(-45deg) scale(1.2); opacity:1; } }
  .message { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); font-size:4em; color:#ff69b4; text-shadow:0 0 40px #ff1493, 0 0 80px #ff69b4; animation:glow 4s infinite alternate; z-index:10; pointer-events:none; white-space:nowrap; }
  @keyframes glow { from { text-shadow:0 0 20px #ff1493; } to { text-shadow:0 0 60px #ff1493, 0 0 100px #ff69b4; } }
</style>
</head>
<body>
  <div id="stars"></div>
  <div class="big-heart" id="bigHeart"></div>
  <div class="message">Te Amo, Nastya! 💖</div>

  <script>
    // Estrelas (leve)
    for (let i = 0; i < 180; i++) {
      const s = document.createElement('div');
      s.className = 'star';
      s.style.width = s.style.height = Math.random() * 2.5 + 1 + 'px';
      s.style.top = Math.random() * 100 + '%';
      s.style.left = Math.random() * 100 + '%';
      s.style.animationDelay = Math.random() * 6 + 's';
      document.getElementById('stars').appendChild(s);
    }

    // Disparos dos cantos e fundo
    function dispararCoracao() {
      const h = document.createElement('div');
      h.className = 'heart';
      const side = Math.random();
      let sx = '0%', ex = '0%';
      if (side < 0.3) { sx = '-10%'; ex = '120vw'; }
      else if (side < 0.6) { sx = '110%'; ex = '-120vw'; }
      else { sx = Math.random() * 100 + '%'; ex = (Math.random() * 60 - 30) + 'vw'; }
      h.style.left = sx;
      h.style.setProperty('--sx', sx);
      h.style.setProperty('--ex', ex);
      h.style.animationDuration = (Math.random() * 6 + 7) + 's';
      document.body.appendChild(h);
      setTimeout(() => h.remove(), 12000);
    }
    setInterval(dispararCoracao, 250); // Equilíbrio: intenso mas não sobrecarrega

    // Coração central grande formado por pequenos (cheio, sem estrela)
    const container = document.getElementById('bigHeart');
    const num = 90; // Otimizado para funcionar
    for (let i = 0; i < num; i++) {
      const ang = (i / num) * Math.PI * 2;
      const r = 0.8 + 0.3 * Math.sin(ang * 5) + 0.1 * Math.sin(ang * 10);
      const x = Math.cos(ang) * r * 140;
      const y = Math.sin(ang) * r * 120 - 60;
      const sh = document.createElement('div');
      sh.className = 'small-heart';
      sh.style.left = (x + 160 - 4.5) + 'px';
      sh.style.top = (y + 140 - 4.5) + 'px';
      sh.style.animationDelay = (i * 0.03) + 's';
      container.appendChild(sh);
    }
  </script>
</body>
</html>
"""
