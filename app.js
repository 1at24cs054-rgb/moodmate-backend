async function fetchEmotion() {
  try {
    const response = await fetch(
       "https://moodmate-backend-dzkq.onrender.com/latest-emotion"
    );

    const data = await response.json();

    document.getElementById("emotion").innerText =
      "Emotion: " + data.emotion;

    document.getElementById("confidence").innerText =
      "Confidence: " + (data.confidence * 100).toFixed(1) + "%";

  } catch (err) {
    console.error("Failed to fetch emotion", err);
  }
}

// fetch every 5 seconds
setInterval(fetchEmotion, 5000);
fetchEmotion();
