// ORBIT v2 — interazioni: reveal a cascata, cursor glow, magnetic buttons,
// contatori animati, nav attiva, parallasse hero leggera.

// Reveal a cascata (assegna --i in base alla posizione nel proprio genitore)
document.querySelectorAll('.reveal-group').forEach(group => {
  Array.from(group.children).forEach((el, i) => el.style.setProperty('--i', i));
});
const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.15 });
revealEls.forEach(el => io.observe(el));

// Cursor glow (desktop only)
const glow = document.getElementById('cursor-glow');
if (glow && matchMedia('(min-width:901px)').matches) {
  window.addEventListener('mousemove', (e) => {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
  }, { passive: true });
}

// Magnetic buttons
document.querySelectorAll('.magnetic').forEach(btn => {
  btn.addEventListener('mousemove', (e) => {
    const r = btn.getBoundingClientRect();
    const x = e.clientX - r.left - r.width / 2;
    const y = e.clientY - r.top - r.height / 2;
    btn.style.transform = `translate(${x * 0.18}px, ${y * 0.35}px)`;
  });
  btn.addEventListener('mouseleave', () => { btn.style.transform = ''; });
});

// Nav: stato scrolled + link attivo per sezione + barra di progresso scroll
const header = document.querySelector('header');
const sections = document.querySelectorAll('main section[id]');
const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');
const progressBar = document.getElementById('scroll-progress');
function onScroll() {
  header.classList.toggle('scrolled', window.scrollY > 40);
  let current = '';
  sections.forEach(s => {
    if (window.scrollY + 140 >= s.offsetTop) current = s.id;
  });
  navLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + current));
  if (progressBar) {
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (window.scrollY / docHeight) * 100 : 0;
    progressBar.style.width = pct + '%';
  }
}
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Tilt 3D al passaggio del mouse sulle card di vetro (solo desktop)
if (matchMedia('(min-width:901px)').matches && matchMedia('(hover: hover)').matches) {
  document.querySelectorAll('.glass').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width;
      const py = (e.clientY - r.top) / r.height;
      const rx = (py - 0.5) * -7;
      const ry = (px - 0.5) * 7;
      card.classList.add('tilting');
      card.style.transform = `perspective(900px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-6px) translateZ(0)`;
    });
    card.addEventListener('mouseleave', () => {
      card.classList.remove('tilting');
      card.style.transform = '';
    });
  });
}

// Nav mobile toggle
const navToggle = document.querySelector('.nav-toggle');
const navLinksBox = document.querySelector('.nav-links');
if (navToggle) {
  navToggle.addEventListener('click', () => navLinksBox.classList.toggle('open'));
  navLinksBox.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinksBox.classList.remove('open')));
}

// Contatori animati
const counters = document.querySelectorAll('[data-count]');
const countIo = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const el = entry.target;
    const target = el.getAttribute('data-count');
    const numMatch = target.match(/[\d.]+/);
    if (!numMatch) { countIo.unobserve(el); return; }
    const num = parseFloat(numMatch[0]);
    const suffix = target.replace(numMatch[0], '');
    const duration = 1200;
    const start = performance.now();
    function tick(now) {
      const p = Math.min(1, (now - start) / duration);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (num < 10 ? (eased * num).toFixed(0) : Math.round(eased * num)) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
    countIo.unobserve(el);
  });
}, { threshold: 0.6 });
counters.forEach(el => countIo.observe(el));

// Parallasse leggera degli anelli orbitali in hero, guidata dal mouse
const heroOrbit = document.querySelector('.hero-orbit-svg');
if (heroOrbit && matchMedia('(min-width:901px)').matches) {
  window.addEventListener('mousemove', (e) => {
    const x = (e.clientX / window.innerWidth - 0.5) * 18;
    const y = (e.clientY / window.innerHeight - 0.5) * 18;
    heroOrbit.style.transform = `translateY(-50%) translate(${x}px, ${y}px)`;
  }, { passive: true });
}

// Contact form -> mailto fallback (static site, no backend)
const form = document.getElementById('contact-form');
if (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const name = document.getElementById('f-name').value;
    const email = document.getElementById('f-email').value;
    const msg = document.getElementById('f-msg').value;
    const subjects = Array.from(document.querySelectorAll('input[name="materia"]:checked')).map(c => c.value).join(', ') || 'Non specificate';
    const body = `Nome: ${name}%0AEmail: ${email}%0AMaterie di interesse: ${subjects}%0A%0AMessaggio:%0A${msg}`;
    window.location.href = `mailto:ripetizioni.matteocasadei@gmail.com?subject=Richiesta%20info%20da%20sito&body=${body}`;
  });
}
