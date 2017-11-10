// Get the modal
var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img1 = document.getElementById('myImg1');
var modalImg1 = document.getElementById("imgmodal");
var captionText1 = document.getElementById("caption");
img1.onclick = function(){
    modal.style.display = "block";
    modalImg1.src = this.src;
    modalImg1.alt = this.alt;
    captionText1.innerHTML = this.alt;
}

var img2 = document.getElementById('myImg2');
var modalImg2 = document.getElementById("imgmodal");
var captionText2 = document.getElementById("caption");
img2.onclick = function(){
    modal.style.display = "block";
    modalImg2.src = this.src;
    modalImg2.alt = this.alt;
    captionText2.innerHTML = this.alt;
}

var img3 = document.getElementById('myImg3');
var modalImg3 = document.getElementById("imgmodal");
var captionText3 = document.getElementById("caption");
img3.onclick = function(){
    modal.style.display = "block";
    modalImg3.src = this.src;
    modalImg3.alt = this.alt;
    captionText3.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}
