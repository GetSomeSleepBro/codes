const form = document.querySelector("#expertForm");
const result = document.querySelector("#result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  // Send all selected symptoms to the rule engine.
  const data = Object.fromEntries(new FormData(form).entries());
  result.textContent = "Checking rules...";

  const response = await fetch("/api/evaluate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const answer = await response.json();

  result.innerHTML = `
    <h2>${answer.decision}</h2>
    <p>${answer.reason}</p>
  `;
});

