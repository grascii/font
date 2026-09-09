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
  url.search = new URLSearchParams([["grascii", grascii]]);
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
  rawTextArea.style.fontSize = `${e.target.value}rem`;
  rawTextArea.style.lineHeight = `${3 * e.target.value}rem`;
  grasciiTextArea.style.fontSize = `${3 * e.target.value}rem`;
  grasciiTextArea.style.lineHeight = `${3 * e.target.value}rem`;
}
