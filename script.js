document.addEventListener('DOMContentLoaded', () => {
  // ----- Nav toggle (mobile) -----
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');

  navToggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('is-open');
    navToggle.classList.toggle('is-open', isOpen);
    navToggle.setAttribute('aria-expanded', isOpen);
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('is-open');
      navToggle.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });

  // ----- Menu tabs -----
  const tabs = document.querySelectorAll('.menu__tab');
  const panels = document.querySelectorAll('.menu__panel');

  function activateTab(target) {
    tabs.forEach(t => {
      const isActive = t.dataset.target === target;
      t.classList.toggle('is-active', isActive);
      t.setAttribute('aria-selected', isActive);
    });
    panels.forEach(p => p.classList.toggle('is-active', p.id === target));
  }

  tabs.forEach(tab => {
    tab.addEventListener('click', () => activateTab(tab.dataset.target));
  });

  // ----- Open #menu directly (for the QR) and keep the Carta tab in sync -----
  function handleHash() {
    if (window.location.hash === '#menu') {
      activateTab('comidas');
    }
  }
  handleHash();
  window.addEventListener('hashchange', handleHash);

  // ----- Footer year -----
  document.getElementById('year').textContent = new Date().getFullYear();
});
