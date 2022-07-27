"use strict";
document.addEventListener("DOMContentLoaded", () => {
  add_autosuggestions();
  document.querySelectorAll("#suggestion-badge").forEach((badge) => {
    badge.addEventListener("click", handle_suggestion_click);
  });
});

const search_suggestions = ["abstract", "title", "claims", "country"];

function handle_suggestion_click(event) {
  var query_input = document.querySelector("#query-input");
  query_input.value += `${event.target.value.toUpperCase()}:"" `;
}

function add_autosuggestions() {
  var autocomplete_div = document.querySelector("#autocomplete-div");
  search_suggestions.forEach((suggestion) => {
    autocomplete_div.innerHTML += `
    <button type="button" class="btn btn-outline-secondary btn-sm" id="suggestion-badge" value="${suggestion}" onclick="handle_suggestion_click">${suggestion}</button>`;
  });
}
