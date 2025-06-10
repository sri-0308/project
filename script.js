
  // Wait until the DOM is fully loaded
  document.addEventListener("DOMContentLoaded", function() {
    // Select all card elements
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
      // Add hover cursor to indicate clickability
      card.style.cursor = 'pointer';

      // When a card is clicked
      card.addEventListener('click', () => {
        // Find the anchor inside the card
        const link = card.querySelector('a');
        if (link && link.href) {
          // Navigate to the link's URL
          window.location.href = link.href;
        }
      });
    });
  });

