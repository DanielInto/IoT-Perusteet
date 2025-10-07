const express = require("express");
const app = express();
const PORT = 3000;
const DISCORD_WEBHOOK_URL =
  "https://discordapp.com/api/webhooks/1425175227389841429/rNKPJeMi3koyHqHuIjF1VH9GPKQkmWKcLXyq_yUx2NZsAHpmtJwv8HO39tK-2SAlMRhM";

app.use(express.json());

app.post("/notify", (req, res) => {
  const { message } = req.body;

  if (!message) {
    return res.status(400).json({ error: "Message is required" });
  }

  fetch(DISCORD_WEBHOOK_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ content: message }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Discord responded with status ${response.status}`);
      }
      res.json({ status: "Message sent..." });
    })
    .catch((error) => {
      console.error("Error sendind to Discord", error);
      res.status(500).json({ error: "Failed sending your message" });
    });
});

app.listen(PORT, () => {
  console.log(`Server running at localhost: ${PORT}`);
});
