//Gallery which will be connected to posts

$(document).ready(function() {
    let images = [
      { src: "static/images/cosmetics.jpg" , slug:"glowing-skin"},
      { src: "static/images/medicinal.jpg", slug:"the-power-of-medicinal-products"},
      { src: "static/images/beauty-products.jpg"},
      { src: "static/images/self-care.jpg", slug:"the-wellness-ritual" },
      { src: "static/images/bag.jpg", text: "Image 5" },
      { src: "static/images/parfume.jpg", text: "Image 6", slug:"scented-serenity"},
      { src: "static/images/creams.jpg", text: "Image 7", slug:"glowing-skin" },
      { src: "static/images/beauty-product.jpg", text: "Image 8" },
      { src: "static/images/cream.jpg", text: "Image 9", slug:"eye-care"},
      { src: "static/images/spa-products.jpg", text: "Image 10"}
    ];
    // Shuffle images
    images.sort(() => Math.random() - 0.5);

    // Display 6 images
    let gallery = $(".images");
    for (let i = 0; i < 6; i++) {
      let imageContainer = $("<div>").addClass("image-container");
      let image = $("<div>").addClass("image");
      let img = $("<img>").attr("src", images[i].src);
      let text = $("<div>").addClass("text").text(images[i].text);
  
      image.append(img);
      image.append(text);
      imageContainer.append(image);
      gallery.append(imageContainer);
  
      // Click event to redirect to article page
      image.click(function() {

        let postSlug = images[i].slug;
        window.location.href =`/${postSlug}/`;  // Need to test if it works
      }); 
    }
  });

let backBtn = document.getElementById("back");
let nextBtn = document.getElementById ("next");
let scrollGallery = document.querySelector(".gallery");

// Add event listener for mouse wheel scrolling

scrollGallery.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    scrollGallery.scrollLeft += evt.deltaY;
});

// Add event listeners for back and next buttons
backBtn.addEventListener("click", function()  {
    scrollGallery.scrollLeft -= 100; // Adjust scroll distance 
});

nextBtn.addEventListener("click", function()  {
    scrollGallery.scrollLeft += 100; 
});