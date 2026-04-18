// AISprint — minimal JS
// Mobile nav toggle + scroll reveal for elements with [data-reveal]

(function () {
  'use strict';

  // --- Mobile nav ------------------------------------------------------------
  const toggle = document.querySelector('.nav-toggle');
  const topbar = document.querySelector('.topbar');
  if (toggle && topbar) {
    toggle.addEventListener('click', () => {
      topbar.classList.toggle('nav-open');
      toggle.textContent = topbar.classList.contains('nav-open') ? '✕' : '☰';
      toggle.setAttribute(
        'aria-expanded',
        topbar.classList.contains('nav-open') ? 'true' : 'false'
      );
    });

    // Close on link click (mobile)
    document.querySelectorAll('.nav-primary a').forEach((a) => {
      a.addEventListener('click', () => {
        topbar.classList.remove('nav-open');
        toggle.textContent = '☰';
      });
    });
  }

  // --- Scroll reveal ---------------------------------------------------------
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('reveal');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -60px 0px' }
    );
    document.querySelectorAll('[data-reveal]').forEach((el) => io.observe(el));
  } else {
    document.querySelectorAll('[data-reveal]').forEach((el) => el.classList.add('reveal'));
  }

  // --- Contact form demo submit ---------------------------------------------
  const form = document.querySelector('form[data-demo-form]');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const msg = form.querySelector('.form-msg');
      if (msg) msg.style.display = 'block';
      const btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.disabled = true;
        btn.textContent = 'Inquiry received ✓';
      }
    });
  }

  // --- Current year in footer ------------------------------------------------
  const yearEl = document.querySelector('[data-year]');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
