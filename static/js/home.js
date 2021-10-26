//      HANDLING CARDS ONCLICK EVENT (OPENS MODAL)

var cards = document.querySelectorAll('.card');

cards.forEach( card => {
    var splitted = card.innerHTML.split('>');          
    var stockx = card.getAttribute('stockx_link');
    var google_im = card.getAttribute('g_im_link');
    var name = splitted[3].slice(0, splitted[3].length-4);
    console.log(name)         
    card.addEventListener('click', () => {
        var modal = new bootstrap.Modal(document.getElementById('sneaker-modal'));
        editModal(String(name), stockx, google_im)
        modal.show()
    })
})


function editModal(name, stockx, google_im){
    var selected_modal = document.getElementById('sneaker-modal')
    console.log(name)
    selected_modal.children[0].children[0].children[0].children[0].innerHTML = name //assigning title (name of the sneaker)
    selected_modal.children[0].children[0].children[1].children[0].href = google_im
    
    

}
