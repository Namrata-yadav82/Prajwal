function responsiveHeader(){
    let navBar = document.querySelector('.nav-bar')
    let count = 0
    document.querySelector('#show').addEventListener('click',() => {
        if(count%2 === 1)navBar.style.display = 'flex'
        else navBar.style.display = 'none'
        count++
    })
}

responsiveHeader()