let time = 3000,
    imageIndex = 0,
    imagens = document.querySelectorAll(".slider img"),
     maxImagens = imagens.length;

function nextImagen(){
    imagens[imageIndex].classList.remove("selected")
    imageIndex++
    if(imageIndex >=maxImagens){
        imageIndex = 0
    }
    imagens[imageIndex].classList.add("selected")
}
function start(){
    setInterval(() => {
    nextImagen()    
    }, time)
}
window.addEventListener("load", start())