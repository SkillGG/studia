const dialogTimer = 1000;
const bodyClearTimer = 100;
const imgMargin = "5px";
const clearBody = () => {
  document.body.setAttribute("class", "")
  document.body.setAttribute("style", "background-image:none !important; background-color: #181a1b !important;")
}
window.onload = () => {
  if (window.location.hostname.includes("klz9.com")) {
    if (localStorage.getItem("devMode") === "true") {
      localStorage.removeItem("devMode");
      return;
    }
    window.onkeydown = ({
      code
    }) => {
      if (code === "KeyD") {
        if (localStorage.getItem("devMode") !== "true") {
          localStorage.setItem("devMode", "true");
          const dialog = document.createElement("dialog");
          dialog.innerHTML = "Dev mode!<br>Next refresh won't remove everything!";
          dialog.style.position = "fixed";
          dialog.style.top = "15px";
          dialog.style.fontSize = "1.5em";
          dialog.style.margin = "0 auto";
          document.body.append(dialog);
          dialog.show()
          setTimeout(() => dialog.close(), dialogTimer);
        }
      }
    }
    let i = 0;
    clearBody();
    const intv = setInterval(() => {
      clearBody();
    }, bodyClearTimer)
    const name = document.querySelector(".manga-name").innerText;
    const images = [...document.querySelectorAll(".chapter-content p > img")];
    if (images.length > 0) {
      document.body.innerHTML = "";
      const div = document.createElement("div")
      div.style.width = "fit-content";
      div.style.margin = "0 auto";
      div.style.display = "grid";
      images.forEach(img => {
        if (img.src.includes("jpg")) {
          const nimg = document.createElement("img")
          nimg.src = img.src;
          nimg.style.justifySelf = "center";
          nimg.style.marginBottom = imgMargin;
          console.log("adding image", nimg)
          div.append(nimg);
        }
      })
      document.body.append(div);
    }
  }
}
