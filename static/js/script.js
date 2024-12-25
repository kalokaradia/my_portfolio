// NavHamburgerMenu
const hamburgerMenu = document.getElementById("hamburger-menu")
const navbarUl = document.getElementById("navbar-default")

if (navbarUl && hamburgerMenu) {
    hamburgerMenu.addEventListener('click', () => {
        navbarUl.classList.toggle("hidden")
    })
} else {
    console.error("Element with id 'navbarUl' and 'hamburgerMenu' not found!");
}


// NavScrolling
const nav = document.getElementById("navbar");
if (nav) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 0) {
            nav.classList.add("nav-scroll");
        } else {
            nav.classList.remove("nav-scroll");
        }
    });
} else {
    console.error("Element with id 'navbar' not found!");
}
