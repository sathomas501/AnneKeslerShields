/* ── Mobile nav ──────────────────────────────────────────── */
const toggle = document.querySelector('.menu-toggle');
const nav    = document.getElementById('main-nav');

if (toggle && nav) {
  toggle.addEventListener('click', () => nav.classList.toggle('open'));
}

document.querySelectorAll('nav > ul > li').forEach(li => {
  li.addEventListener('click', (e) => {
    if (window.innerWidth <= 768 && li.querySelector('.dropdown')) {
      e.stopPropagation();
      li.classList.toggle('open');
    }
  });
});

/* ── Fade-in on scroll ───────────────────────────────────── */
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.08 });

document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

/* ── Lightbox ────────────────────────────────────────────── */
const lightbox = document.getElementById('lightbox');
if (lightbox) {
  const lbImg     = lightbox.querySelector('img');
  const lbCaption = document.getElementById('lightbox-caption');
  const lbClose   = document.getElementById('lightbox-close');
  const lbPrev    = document.getElementById('lightbox-prev');
  const lbNext    = document.getElementById('lightbox-next');
  const figures   = Array.from(document.querySelectorAll('.gallery-grid figure'));
  let current = 0;

  function openLightbox(idx) {
    current = idx;
    const fig   = figures[idx];
    lbImg.src   = fig.querySelector('img').src;
    lbImg.alt   = fig.querySelector('img').alt;
    const title = fig.dataset.title || '';
    if (lbCaption) lbCaption.textContent = title;
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('open');
    lbImg.src = '';
    document.body.style.overflow = '';
  }

  figures.forEach((fig, i) => fig.addEventListener('click', () => openLightbox(i)));

  lbClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', e => { if (e.target === lightbox) closeLightbox(); });

  lbPrev.addEventListener('click', e => {
    e.stopPropagation();
    openLightbox((current - 1 + figures.length) % figures.length);
  });
  lbNext.addEventListener('click', e => {
    e.stopPropagation();
    openLightbox((current + 1) % figures.length);
  });

  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape')      closeLightbox();
    if (e.key === 'ArrowLeft')   openLightbox((current - 1 + figures.length) % figures.length);
    if (e.key === 'ArrowRight')  openLightbox((current + 1) % figures.length);
  });
}

/* ── Prints series filter ────────────────────────────────── */
const filterBtns = document.querySelectorAll('.filter-btn');
if (filterBtns.length) {
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const series = btn.dataset.filter;
      document.querySelectorAll('.print-card').forEach(card => {
        if (series === 'all' || card.dataset.series === series) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });
}
