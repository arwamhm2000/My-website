function getPrompt() {
  const prompts = [
    "Write about a time traveler who gets stuck in the wrong decade.",
    "Describe a world where dreams are traded as currency.",
    "Write from the perspective of an AI gaining emotions."
  ];
  const randomPrompt = prompts[Math.floor(Math.random() * prompts.length)];
  document.getElementById('promptDisplay').innerText = randomPrompt;
}

function countWords() {
  const text = document.getElementById('textInput').value.trim();
  const wordCount = text ? text.split(/\s+/).length : 0;
  document.getElementById('wordCount').innerText = `Word count: ${wordCount}`;
}
