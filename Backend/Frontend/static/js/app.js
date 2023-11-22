const myCarouselElement = document.querySelector('#carouselExampleCaptions')
const logo = document.querySelector('.logo')
const carousel = new bootstrap.Carousel(myCarouselElement, {
  interval: 2200,
  touch: false
})

aud = false
window.onload = function(){
  logo.addEventListener('click',play)
}
let isPlaying = true;
function play() {
  var audio = document.getElementById("my_audio");
  if (isPlaying) {
    audio.play();
  } else {
    audio.pause();
    audio.currentTime = 0;
  }
  isPlaying = !isPlaying;
}