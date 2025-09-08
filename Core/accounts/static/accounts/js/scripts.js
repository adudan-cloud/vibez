// Smooth scroll for internal navigation buttons
function go(id) {
  const el = document.querySelector(id);
  if (!el) return;
  el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Set current year in footer
document.addEventListener('DOMContentLoaded', () => {
  const yearSpan = document.getElementById('year');
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }
});

// Accessibility: remove focus ring for mouse users
(function () {
  let usingMouse = false;

  document.addEventListener('mousedown', () => {
    usingMouse = true;
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      usingMouse = false;
    }
  });

  document.addEventListener('focusin', (e) => {
    if (usingMouse) {
      e.target.style.outline = 'none';
    }
  });
})();

// Optional: highlight active dashboard card on hover
const cards = document.querySelectorAll('.card');
cards.forEach(card => {
  card.addEventListener('mouseenter', () => {
    card.style.borderColor = '#d7efe3';
    card.style.boxShadow = '0 14px 28px rgba(0,0,0,0.08), 0 4px 10px rgba(0,0,0,0.05)';
  });
  card.addEventListener('mouseleave', () => {
    card.style.borderColor = '#e3efe9';
    card.style.boxShadow = '0 10px 20px rgba(0,0,0,0.06), 0 2px 6px rgba(0,0,0,0.04)';
  });
});
