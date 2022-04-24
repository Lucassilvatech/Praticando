const $body = document.querySelector('body')
const $light = document.querySelectorAll('p')
const $title = document.querySelectorAll('h2')
const $h3 = document.querySelector('h3')
const $ul = document.querySelector('ul')
const $creditos = document.querySelector('#créditos')

let statusDoTema = false

const $tema = document.querySelector('#imgTema')
$tema.addEventListener('click', () =>{
    if(statusDoTema == false){
        adicionar()
        statusDoTema = true

    }else if(statusDoTema == true){
        remover()
        statusDoTema = false
    }
   
})

function adicionar(){
    $body.classList.add('dark')
    $h3.classList.add('white')
    $ul.classList.add('light')
    $creditos.classList.add('white')

    for(itens of $light){
         itens.classList.add('light')
    }
    for(coisado of $title){
        coisado.classList.add('white')
    }
}
function remover(){
    $body.classList.remove('dark')
    $h3.classList.remove('white')
    $ul.classList.remove('light')
    $creditos.classList.remove('white')

    for(itens of $light){
         itens.classList.remove('light')
    }
    for(coisado of $title){
        coisado.classList.remove('white')
    } 
}
