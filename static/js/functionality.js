let menu = document.querySelector('#menu-bars');
let navbar = document.querySelector('.navbar');

menu.addEventListener('click', ()=>{
    navbar.classList.toggle('active');
    menu.classList.toggle('la-times')
})

window.onscroll = ()=>{
    navbar.classList.remove('active');
    menu.classList.remove('la-times');
}