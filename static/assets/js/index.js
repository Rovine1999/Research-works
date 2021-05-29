let picModal = document.getElementById('changeProfilePic')
let outputpicel = document.getElementById('profile-pic-img-output')
let picinput = document.getElementById('pic-input')

picModal.addEventListener('show.bs.modal', function (event) {
  let button = event.relatedTarget
  let picDiv = picModal.querySelector('#profile-pic-img')
  let img = document.querySelector('#profile-pic-img').src
  picDiv.src = img;
})

function preview_image(event) {
    let reader = new FileReader();
    reader.onload = function() {
        outputpicel.src = reader.result;
        outputpicel.parentNode.classList.remove('d-none')
    }
    reader.readAsDataURL(event.target.files[0]);
}

picinput.addEventListener('change', e => {
    preview_image(e)
})