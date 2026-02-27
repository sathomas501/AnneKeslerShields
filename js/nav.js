// Mobile nav toggle
const toggle = document.querySelector('.menu-toggle');
const nav    = document.getElementById('main-nav');

if (toggle && nav) {
  toggle.addEventListener('click', () => nav.classList.toggle('open'));
}

// Mobile: tap gallery item to expand dropdown
document.querySelectorAll('nav > ul > li').forEach(li => {
  li.addEventListener('click', (e) => {
    if (window.innerWidth <= 768 && li.querySelector('.dropdown')) {
      e.stopPropagation();
      li.classList.toggle('open');
    }
  });
});

// Lightbox
const lightbox = document.getElementById('lightbox');
if (lightbox) {
  const lbImg   = lightbox.querySelector('img');
  const lbClose = document.getElementById('lightbox-close');
  const lbPrev  = document.getElementById('lightbox-prev');
  const lbNext  = document.getElementById('lightbox-next');
  const figures = Array.from(document.querySelectorAll('.gallery-grid figure'));
  let current = 0;

  function openLightbox(idx) {
    current = idx;
    const src = figures[idx].querySelector('img').src
      .replace('/images/', '/images/');
    lbImg.src = src;
    lbImg.alt = figures[idx].querySelector('img').alt;
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('open');
    lbImg.src = '';
    document.body.style.overflow = '';
  }

  figures.forEach((fig, i) => {
    fig.addEventListener('click', () => openLightbox(i));
  });

  lbClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => { if (e.target === lightbox) closeLightbox(); });

  lbPrev.addEventListener('click', (e) => {
    e.stopPropagation();
    openLightbox((current - 1 + figures.length) % figures.length);
  });
  lbNext.addEventListener('click', (e) => {
    e.stopPropagation();
    openLightbox((current + 1) % figures.length);
  });

  document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') openLightbox((current - 1 + figures.length) % figures.length);
    if (e.key === 'ArrowRight') openLightbox((current + 1) % figures.length);
  });
}
