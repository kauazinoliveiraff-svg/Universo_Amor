html_code = """
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<title>Disparos de Amor - Te Amo Nastya</title>
<style>
  body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    overflow: hidden;
    background: radial-gradient(ellipse at bottom, #0f0c29 0%, #302b63 50%, #24243e 100%);
    font-family: Arial, sans-serif;
  }

  /* Corações voando/disparando pelo fundo */
  .heart {
    position: absolute;
    width: 20px;
    height: 18px;
    background: #ff69b4;
    transform: rotate(-45deg);
    box-shadow: 0 0 25px #ff1493;
    animation: shoot 12s infinite linear, beat 1.8s infinite;
  }
  .heart::before, .heart::after {
    content: "";
    position: absolute;
    width: 20px;
    height: 20px;
    background: #ff69b4;
    border-radius: 50%;
  }
  .heart::before { top: -10px; left: 0; }
  .heart::after { left: 10px; top: 0; }

  @keyframes shoot {
    0% { transform: translateY(120vh) rotate(-45deg) scale(0.5); opacity: 0; }
    5% { opacity: 1; }
    95% { opacity: 1; }
    100% { transform: translateY(-30vh) rotate(-45deg) scale(1.2); opacity: 0; }
  }
  @keyframes beat {
    0%, 100% { transform: scale(1) rotate(-45deg); }
    50% { transform: scale(1.4) rotate(-45deg); }
  }

  /* Estrelas twinkling */
  #stars {
    position: absolute;
    inset: 0;
    pointer-events: none;
  }
  .star {
    position: absolute;
    background: #fff;
    border-radius: 50%;
    opacity: 0.9;
    animation: twinkle 4s infinite alternate;
  }
  @keyframes twinkle {
    0% { opacity: 0.3; }
    100% { opacity: 1; }
  }

  /* Coração grande central formado por pequenos corações */
  .big-heart-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 380px;
    height: 340px;
    z-index: 5;
  }

  .small-heart {
    position: absolute;
    width: 14px;
    height: 14px;
    background: #ff69b4;
    transform: rotate(-45deg);
    box-shadow: 0 0 15px #ff1493;
    animation: pulse-in-heart 3s infinite ease-in-out;
  }
  .small-heart::before, .small-heart::after {
    content: "";
    position: absolute;
    width: 14px;
    height: 14px;
    background: #ff69b4;
    border-radius: 50%;
  }
  .small-heart::before { top: -7px; left: 0; }
  .small-heart::after { left: 7px; top: 0; }

  @keyframes pulse-in-heart {
    0%, 100% { transform: rotate(-45deg) scale(0.9); opacity: 0.7; }
    50% { transform: rotate(-45deg) scale(1.15); opacity: 1; }
  }

  /* Texto central */
  .message {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 4.5em;
    color: #ff69b4;
    text-shadow: 0 0 40px #ff1493, 0 0 80px #ff69b4;
    animation: glow-text 4s infinite alternate;
    z-index: 10;
    pointer-events: none;
    white-space: nowrap;
  }
  @keyframes glow-text {
    from { text-shadow: 0 0 20px #ff1493; }
    to { text-shadow: 0 0 60px #ff1493, 0 0 100px #ff69b4; }
  }
</style>
</head>
<body>
  <div id="stars"></div>
  <div class="big-heart-container" id="bigHeart"></div>
  <div class="message">Te Amo, Nastya! 💖</div>

  <script>
    // Estrelas
    const stars = document.getElementById('stars');
    for (let i = 0; i < 220; i++) {
      const s = document.createElement('div');
      s.className = 'star';
      s.style.width = s.style.height = Math.random() * 3 + 1 + 'px';
      s.style.top = Math.random() * 100 + '%';
      s.style.left = Math.random() * 100 + '%';
      s.style.animationDelay = Math.random() * 4 + 's';
      stars.appendChild(s);
    }

    // Corações disparando fundo
    function shootHeart() {
      const h = document.createElement('div');
      h.className = 'heart';
      h.style.left = Math.random() * 100 + 'vw';
      h.style.animationDuration = (Math.random() * 8 + 8) + 's';
      document.body.appendChild(h);
      setTimeout(() => h.remove(), 20000);
    }
    setInterval(shootHeart, 200);  // Mais disparos para ficar dinâmico

    // Coração grande no centro com pequenos corações formando o shape
    const container = document.getElementById('bigHeart');
    const numHearts = 120;  // Densidade - aumenta para mais cheio
    const scale = 1.2;

    for (let i = 0; i < numHearts; i++) {
      const angle = (i / numHearts) * Math.PI * 2;
      const pulse = 16 * (Math.sin(angle * 5) * 0.1 + 1);  // Forma de coração clássico
      const r = pulse * (0.7 + 0.3 * Math.sin(angle * 3)); 

      const x = Math.cos(angle) * r * 140 * scale;
      const y = Math.sin(angle) * r * 130 * scale - 60 * scale;  // Move pra cima

      const small = document.createElement('div');
      small.className = 'small-heart';
      small.style.left = (x + 190 - 7) + 'px';  // Centro ajustado
      small.style.top = (y + 170 - 7) + 'px';
      small.style.animationDelay = (i * 0.03) + 's';  // Pulso sequencial
      container.appendChild(small);
    }
  </script>
</body>
</html>
"""
