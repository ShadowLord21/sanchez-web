// Mark JS as running before anything else, so CSS can gate the reveal-on-scroll
// hidden state behind it (.js-ready .reveal). If JS never runs or errors out
// below, content stays visible instead of stuck at opacity:0.
document.documentElement.classList.add('js-ready');

document.addEventListener('DOMContentLoaded', () => {
  // Each feature is isolated in its own try/catch so one failing part
  // (e.g. a missing element) can't block the others from running.

  // ----- Nav toggle (mobile) -----
  try {
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
  } catch (err) { console.error('nav toggle init failed', err); }

  // ----- Menu jump-to tabs ("Ir a:") -----
  // Las categorías de la Carta (Comidas, Pizzas, Empanadas, Menú del Día,
  // Cafetería, Promos) ya no se ocultan/muestran: están todas visibles en
  // un solo scroll continuo, así que .menu__tab son simples anclas <a> y
  // el scroll suave nativo (scroll-behavior + scroll-padding-top en el CSS)
  // ya resuelve el salto. No hace falta JS para esto.

  // ----- Footer year -----
  try {
    document.getElementById('year').textContent = new Date().getFullYear();
  } catch (err) { console.error('footer year init failed', err); }

  // ----- Nav shadow on scroll -----
  try {
    const nav = document.getElementById('nav');
    function toggleNavShadow() {
      nav.classList.toggle('is-scrolled', window.scrollY > 10);
    }
    toggleNavShadow();
    window.addEventListener('scroll', toggleNavShadow, { passive: true });
  } catch (err) { console.error('nav shadow init failed', err); }

  // ----- Scroll reveal -----
  try {
    const revealEls = document.querySelectorAll('.reveal, .reveal-stagger');
    if ('IntersectionObserver' in window && revealEls.length) {
      const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            revealObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
      revealEls.forEach(el => revealObserver.observe(el));
    } else {
      revealEls.forEach(el => el.classList.add('is-visible'));
    }
  } catch (err) { console.error('scroll reveal init failed', err); }

  // ----- Nav active link on scroll (scroll-spy) -----
  try {
    const navAnchorLinks = document.querySelectorAll('.nav__links a[href^="#"]');
    const spySections = Array.from(navAnchorLinks)
      .map(link => document.querySelector(link.getAttribute('href')))
      .filter(Boolean);

    if ('IntersectionObserver' in window && spySections.length) {
      const spyObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            navAnchorLinks.forEach(link => {
              link.classList.toggle('is-active-link', link.getAttribute('href') === `#${entry.target.id}`);
            });
          }
        });
      }, { rootMargin: `-${72 + 40}px 0px -60% 0px`, threshold: 0 });
      spySections.forEach(section => spyObserver.observe(section));
    }
  } catch (err) { console.error('nav scroll-spy init failed', err); }

  // ----- Product modal (Destacados / Carta / Cafetería cards) -----
  // El botón "+" es visual ("ver más"), no un carrito: un solo listener
  // en toda la tarjeta cubre el click en cualquier parte, incluido el "+".
  try {
    const modal = document.getElementById('productModal');
    const modalImg = document.getElementById('productModalImg');
    const modalName = document.getElementById('productModalName');
    const modalPrice = document.getElementById('productModalPrice');
    const modalDesc = document.getElementById('productModalDesc');
    let lastFocused = null;

    function openModal(card) {
      lastFocused = document.activeElement;
      const { name, price, desc, img } = card.dataset;
      modalName.textContent = name || '';
      modalPrice.textContent = price || '';
      if (desc) {
        modalDesc.textContent = desc;
        modalDesc.hidden = false;
      } else {
        modalDesc.textContent = '';
        modalDesc.hidden = true;
      }
      modalImg.style.backgroundImage = img ? `url('${img}')` : '';
      modal.classList.add('is-open');
      modal.setAttribute('aria-hidden', 'false');
      document.body.classList.add('modal-open');
      modal.querySelector('.product-modal__close').focus();
    }

    function closeModal() {
      modal.classList.remove('is-open');
      modal.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('modal-open');
      if (lastFocused) lastFocused.focus();
    }

    document.querySelectorAll('.menu__card').forEach(card => {
      card.addEventListener('click', () => openModal(card));
    });

    modal.querySelectorAll('[data-close]').forEach(el => {
      el.addEventListener('click', closeModal);
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('is-open')) closeModal();
    });
  } catch (err) { console.error('product modal init failed', err); }

  // ----- Menú del Día: auto-detect today + day selector -----
  try {
    const dayButtons = document.querySelectorAll('.menudeldia__day');
    const dayPanels = document.querySelectorAll('.menudeldia__panel');
    const weekendNotice = document.getElementById('weekendNotice');

    function showDay(day) {
      dayButtons.forEach(btn => {
        btn.classList.toggle('is-active', btn.dataset.day === String(day));
      });
      dayPanels.forEach(panel => {
        panel.classList.toggle('is-active', panel.dataset.dayPanel === String(day));
      });
    }

    dayButtons.forEach(btn => {
      btn.addEventListener('click', () => showDay(btn.dataset.day));
    });

    // JS Date.getDay(): 0 = domingo, 1 = lunes ... 6 = sábado
    const todayIndex = new Date().getDay();
    const isWeekday = todayIndex >= 1 && todayIndex <= 5;

    if (weekendNotice) weekendNotice.hidden = isWeekday;
    showDay(isWeekday ? todayIndex : 1);
  } catch (err) { console.error('menú del día init failed', err); }
});
