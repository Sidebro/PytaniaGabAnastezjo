const drawButtons = document.querySelectorAll(".draw-button");
const resetButtons = document.querySelectorAll(".reset-button");

async function fetchQuestion(category, button) {
  const questionElement = document.getElementById(`question-${category}`);
  const statusElement = document.getElementById(`status-${category}`);

  button.disabled = true;
  button.textContent = "Losowanie...";

  try {
    const response = await fetch(`/api/question/${category}`);

    if (!response.ok) {
      throw new Error("Nie udalo sie pobrać pytania.");
    }

    const data = await response.json();
    questionElement.textContent = data.question;
    statusElement.textContent = `Pozostało pytań: ${data.remaining} z ${data.total}.`;
  } catch (error) {
    questionElement.textContent = "Wystąpił problem podczas pobierania pytania.";
    statusElement.textContent = "Nie udało sie pobrać pytania.";
  } finally {
    button.disabled = false;
    button.textContent = "Losuj pytanie";
  }
}

async function resetCategory(category, button) {
  const questionElement = document.getElementById(`question-${category}`);
  const statusElement = document.getElementById(`status-${category}`);

  button.disabled = true;
  button.textContent = "Resetowanie...";

  try {
    const response = await fetch(`/api/reset/${category}`, {
      method: "POST",
    });

    if (!response.ok) {
      throw new Error("Nie udało sie zresetować puli pytań.");
    }

    const data = await response.json();
    questionElement.textContent = "Kliknij przycisk, aby wylosowac pytanie.";
    statusElement.textContent = `${data.message} Dostepnych: ${data.remaining} z ${data.total}.`;
  } catch (error) {
    statusElement.textContent = "Wystąpił problem podczas resetowania puli.";
  } finally {
    button.disabled = false;
    button.textContent = "Resetuj";
  }
}

drawButtons.forEach((button) => {
  button.addEventListener("click", () => {
    fetchQuestion(button.dataset.category, button);
  });
});

resetButtons.forEach((button) => {
  button.addEventListener("click", () => {
    resetCategory(button.dataset.category, button);
  });
});
