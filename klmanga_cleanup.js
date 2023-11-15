const dialogTimer = 1000;
const bodyClearTimer = 100;
const imgMargin = "5px";
const clearBody = () => {
  document.body.setAttribute("class", "")
  document.body.setAttribute("style", "background-image:none !important; background-color: #181a1b !important;")
}
window.onload = () => {
  if (window.location.hostname.includes("klz9.com")) {
    const devMode = localStorage.getItem("devMode") === "true";
    if (devMode) {
      localStorage.removeItem("devMode");
      return;
    } else {
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
    }
    let i = 0;
    clearBody();
    const intv = setInterval(() => {
      clearBody();
    }, bodyClearTimer)
    const name = document.querySelector(".manga-name").innerText;
    const chapterNum = document.querySelector("#zlist-chs > select > option[selected]").innerText;
    const images = [...document.querySelectorAll(".chapter-content p > img")];
    const header = document.querySelector("#header");
    if (images.length > 0) {
      // clear body
      document.body.innerHTML = "";
      document.body.append(header);
      // create title
      const title = document.createElement("div");
      title.style.width = "fit-content";
      title.style.margin = "10px auto 0 auto";
      title.innerHTML = `${name}<br/>${chapterNum}`;
      title.style.textAlign = "center";
      title.style.fontSize = "2em";
      document.body.append(title);
      // create image container
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
