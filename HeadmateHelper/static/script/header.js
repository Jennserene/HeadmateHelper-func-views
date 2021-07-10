let openSwitchMenu = false
let openMainMenu = false

function switchExpand() {
  if (openSwitchMenu) {
    let html = document.querySelector("html")
    html.removeEventListener("click", closeSwitchMenu)
    openSwitchMenu = false
  }
  let divMenu = document.getElementById("switchMenu")
  divMenu.classList.toggle("switchClose")
  divMenu.classList.toggle("switchExpand")
  if (divMenu.classList.contains("switchExpand")) {
    let html = document.querySelector("html")
    html.addEventListener("click", closeSwitchMenu)
    openSwitchMenu = true
  }
}

function closeSwitchMenu(e) {
  let divMenu = document.getElementById("switchMenu")
  let html = document.querySelector("html")
  let switchButton = document.getElementById("switchButton")
  if (e.target !== switchButton  && !divMenu.contains(e.target)) {
    divMenu.classList.toggle("switchClose")
    divMenu.classList.toggle("switchExpand")
    html.removeEventListener("click", closeSwitchMenu)
    openSwitchMenu = false
  }
}

function mainExpand() {
  if (openMainMenu) {
    let html = document.querySelector("html")
    html.removeEventListener("click", closeMainMenu)
    openMainMenu = false
  }
  let divMenu = document.getElementById("mainMenu")
  divMenu.classList.toggle("mainClose")
  divMenu.classList.toggle("mainExpand")
  if (divMenu.classList.contains("mainExpand")) {
    let html = document.querySelector("html")
    html.addEventListener("click", closeMainMenu)
    openMainMenu = true
  }
}

function closeMainMenu(e) {
  let divMenu = document.getElementById("mainMenu")
  let html = document.querySelector("html")
  let menuButton = document.getElementById("mainButton")
  if (e.target !== menuButton  && !divMenu.contains(e.target)) {
    divMenu.classList.toggle("mainClose")
    divMenu.classList.toggle("mainExpand")
    html.removeEventListener("click", closeMainMenu)
    openMainMenu = false
  }
}