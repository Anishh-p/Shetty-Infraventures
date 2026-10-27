(function () {
  'use strict';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* nav: solid on scroll, hide on scroll down, mobile menu */
  var nav = $('.nav'), last = 0;
  function onScroll() {
    var y = window.scrollY;
    nav.classList.toggle('scrolled', y > 60);
    nav.classList.toggle('hide', y > last && y > 400 && !document.body.classList.contains('menu-open'));
    last = y;
  }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  var burger = $('.burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded', open);
    });
    $$('.nav__links a').forEach(function (a) {
      a.addEventListener('click', function () { document.body.classList.remove('menu-open'); });
    });
  }

  /* scroll reveal */
  var rv = $$('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    rv.forEach(function (el) { io.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add('in'); }); }

  /* hero slideshow */
  var slides = $$('.hero__slide');
  if (slides.length > 1) {
    var i = 0, cur = $('.hero__cur');
    setInterval(function () {
      slides[i].classList.remove('on');
      i = (i + 1) % slides.length;
      slides[i].classList.add('on');
      if (cur) cur.textContent = String(i + 1).padStart(2, '0');
    }, 6000);
  }

  /* project filters */
  var fb = $$('.filters button');
  fb.forEach(function (b) {
    b.addEventListener('click', function () {
      fb.forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      var f = b.getAttribute('data-f');
      $$('.pgrid .card').forEach(function (c) {
        c.classList.toggle('hidden', f !== 'all' && c.getAttribute('data-cat') !== f);
      });
    });
  });

  /* lightbox */
  var items = $$('.gal button');
  if (items.length) {
    var lb = document.createElement('div');
    lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true');
    lb.innerHTML = '<button class="x" aria-label="Close">&times;</button><button class="p" aria-label="Previous">&#8592;</button><img alt=""><button class="n" aria-label="Next">&#8594;</button><div class="c"></div>';
    document.body.appendChild(lb);
    var im = $('img', lb), ct = $('.c', lb), idx = 0;
    function show(n) {
      idx = (n + items.length) % items.length;
      im.src = items[idx].getAttribute('data-full');
      im.alt = $('img', items[idx]).alt;
      ct.textContent = String(idx + 1).padStart(2, '0') + ' / ' + String(items.length).padStart(2, '0');
    }
    function open(n) { show(n); lb.classList.add('open'); document.body.style.overflow = 'hidden'; $('.x', lb).focus(); }
    function close() { lb.classList.remove('open'); document.body.style.overflow = ''; }
    items.forEach(function (b, n) { b.addEventListener('click', function () { open(n); }); });
    $('.x', lb).addEventListener('click', close);
    $('.p', lb).addEventListener('click', function () { show(idx - 1); });
    $('.n', lb).addEventListener('click', function () { show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
    var sx = 0;
    lb.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      var dx = e.changedTouches[0].clientX - sx;
      if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
    });
  }

  /* contact form -> opens the visitor's email app (no backend needed) */
  var form = $('#enquiry');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var body = 'Name: ' + d.get('name') + '\nPhone: ' + (d.get('phone') || '-') + '\nEmail: ' + d.get('email') +
        '\nEnquiry type: ' + d.get('type') + '\n\n' + d.get('message');
      window.location.href = 'mailto:' + form.getAttribute('data-to') +
        '?subject=' + encodeURIComponent('Website enquiry — ' + d.get('type')) + '&body=' + encodeURIComponent(body);
    });
  }
})();
