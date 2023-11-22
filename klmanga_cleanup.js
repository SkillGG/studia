// code to make klmanga w/o ads and other junk
const dialogTimer = 1000;
const bodyClearTimer = 100;
const imgMargin = "5px";
const imageSize = "90vh";


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
    const select = document.querySelector(".chapter-select select.form-control");
    const ChapterSelect = document.createElement("div");
    const newSelect = document.createElement("select");
    {
    	for(const opt of [...select.children].toReversed()){
      		newSelect.append(opt);
    	}
      	newSelect.selectedIndex = [...newSelect.children].findIndex(o=>o.getAttribute("selected")!==null)
    }
    newSelect.onchange = (e)=>window.location = e.target.value;
    if (images.length > 0) {
      // clear body
      document.body.innerHTML = "";
      
      // create chapter select
      document.body.append(ChapterSelect);
      ChapterSelect.style.position = "fixed";
      ChapterSelect.style.top = "20%";
      ChapterSelect.style.left = "10px";
      const prevBtn = document.createElement("button");
      prevBtn.innerText = "Prev";
      prevBtn.onclick = (e)=>{
        newSelect.selectedIndex--;
        newSelect.dispatchEvent(new Event("change"))
      }
      const nextBtn = document.createElement("button");
      nextBtn.innerText = "Next";
      nextBtn.onclick = (e)=>{
        newSelect.selectedIndex++;
        newSelect.dispatchEvent(new Event("change"))
      }
      if(newSelect.selectedIndex > 0)
        ChapterSelect.append(prevBtn);
      ChapterSelect.append(newSelect)
      if(newSelect.selectedIndex < newSelect.children.length-1)
        ChapterSelect.append(nextBtn)
      ChapterSelect.append(document.createElement("br"));
      ChapterSelect.append("Press D to show full page after refresh!")
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
          nimg.style.maxHeight = imageSize;
          nimg.style.justifySelf = "center";
          nimg.style.marginBottom = imgMargin;
          // console.log("adding image", nimg)
          div.append(nimg);
        }
      })
      document.body.append(div);
    }
  }
}
