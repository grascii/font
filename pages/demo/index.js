const initialText = new URLSearchParams(window.location.search).get("grascii");

const rawTextArea = document.getElementById("raw-text");
const grasciiTextArea = document.getElementById("grascii-text")
const scaleInput = document.getElementById("scale")

if (initialText) {
  rawTextArea.value = initialText;
  grasciiTextArea.value = initialText;
}

function updateUrl(grascii) {
  const url = new URL(window.location);
  url.search = new URLSearchParams({ grascii });
  window.history.replaceState(null, "", url);
}

rawTextArea.oninput = (e) => {
  grasciiTextArea.value = e.target.value;
  updateUrl(e.target.value);
}

grasciiTextArea.oninput = (e) => {
  rawTextArea.value = e.target.value;
  updateUrl(e.target.value);
}

scaleInput.oninput = (e) => {
  rawTextArea.style.fontSize = `${0.75 * e.target.value}rem`;
  rawTextArea.style.lineHeight = `${3 * e.target.value}rem`;
  grasciiTextArea.style.fontSize = `${3 * e.target.value}rem`;
  grasciiTextArea.style.lineHeight = `${3 * e.target.value}rem`;
}

fetch("./commit.txt").then(res => {
  if (!res.ok) {
    throw new Error(`Bad status: ${res.status}`);
  } else {
    return res.text();
  }
}).then(commit => {
  const footer = document.getElementsByTagName("footer")[0];
  footer.innerHTML = `Grascii font built from commit <a href="https://github.com/grascii/font/commit/${commit}">${commit.substring(0, 7)}</a>`;
}).catch(err => {
  console.warn("Failed to fetch build info", err);
})
