async function checkPassword() {
  const password = document.getElementById("password").value;

  const response = await fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ password: password })
  });

  const data = await response.json();

  document.getElementById("strength").innerText =
    `Strength: ${data.strength} | Score: ${data.score}`;

  const feedbackList = document.getElementById("feedback");
  feedbackList.innerHTML = "";

  data.feedback.forEach(item => {
    const li = document.createElement("li");
    li.innerText = item;
    feedbackList.appendChild(li);
  });
}