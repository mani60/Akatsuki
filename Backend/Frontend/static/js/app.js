const categories = document.querySelectorAll('.category_link')
const logo = document.querySelector('.logo')
logo.addEventListener('click',play)
let isPlaying = true;
function play() {
  var audio = document.getElementById("my_audio");
  if (isPlaying) {
    audio.play();
    audio.volume = 0.6; 
  } else {
    audio.pause();
    audio.currentTime = 0;
  }
  isPlaying = !isPlaying;
}
function startfun(music){
  const audio = new Audio(music);
  audio.play();
}