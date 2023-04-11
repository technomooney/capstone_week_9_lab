var deleteButtons = document.querySelectorAll('.delete')

deleteButtons.forEach(function(button) {
    button.addEventListener('click', function(event){
        var okToDelete = confirm("Are you sure you want to delete this place?")
        if (!okToDelete) {
            event.preventDefault()
        }
    })
});