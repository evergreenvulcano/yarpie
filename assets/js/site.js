(function () {
  const path = window.location.pathname.split('/').pop() || 'index.html';
  const links = document.querySelectorAll('.nav-list a[data-page]');

  links.forEach((link) => {
    if (link.getAttribute('data-page') === path) {
      link.setAttribute('aria-current', 'page');
    }
  });

  const yearNode = document.querySelector('[data-year]');
  if (yearNode) {
    yearNode.textContent = new Date().getFullYear().toString();
  }
})();
