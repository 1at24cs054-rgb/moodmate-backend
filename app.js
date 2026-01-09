const BACKEND_URL =
  "https://moodmate-backend-dzkq.onrender.com/latest-emotion";

function applyUI(emotion) {
  const emojiEl = document.getElementById("emoji");
  const body = document.body;

  if (emotion === "happy") {
    emojiEl.innerText = "😊";
    body.style.backgroundColor = "#FFF9C4";
  } else if (emotion === "sad") {
    emojiEl.innerText = "😢";
    body.style.backgroundColor = "#BBDEFB";
  } else if (emotion === "angry") {
    emojiEl.innerText = "😡";
    body.style.backgroundColor = "#FFCDD2";
  } else if (emotion === "surprised") {
    emojiEl.innerText = "😲";
    body.style.backgroundColor = "#E1BEE7";
  } else {
    emojiEl.innerText = "😐";
    body.style.backgroundColor = "#E0E0E0";
  }
}

async function fetchEmotion() {
  try {
    const res = await fetch(BACKEND_URL);
    const data = await res.json();

    document.getElementById("emotion").innerText =
      "Emotion: " + data.emotion;

    document.getElementById("confidence").innerText =
      "Confidence: " + (data.confidence * 100).toFixed(1) + "%";

    applyUI(data.emotion);

  } catch (err) {
    console.error("Fetch error", err);
  }
}

setInterval(fetchEmotion, 5000);
fetchEmotion();
