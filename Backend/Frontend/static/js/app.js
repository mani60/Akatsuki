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

async function up(ele){
  const id = ele.getAttribute('id').toString()
  let eml = ele.parentNode.children[1]  
  let response = await fetch(
    `/IncCart/?prod_id=${id}`,
    {
        method: 'GET',
        headers:new Headers({
            'Content-type': 'application/x-www-form-urlencoded',
        }),
    });

  let data = await response.json();
  eml.innerText = data.quantity;
  document.getElementById("amt").innerText = "$"+data.amount;
  document.getElementById("t_amt").innerText = "$"+data.total_amount; 
}
async function down(ele){
  const id = ele.getAttribute('id').toString()
  let eml = ele.parentNode.children[1]
  let response = await fetch(
    `/DecCart/?prod_id=${id}`,
    {
        method: 'GET',
        headers:new Headers({
            'Content-type': 'application/x-www-form-urlencoded',
        }),
    });
  let data = await response.json();
  eml.innerText = data.quantity;
  document.getElementById("amt").innerText = "$"+data.amount;
  document.getElementById("t_amt").innerText = "$"+data.total_amount;
}
async function del(ele){
  const id = ele.getAttribute('id').toString();
  let eml = ele.parentNode.children[1];
  let response = await fetch(
    `/RemoveItem/?prod_id=${id}`,
    {
        method: 'GET',
        headers:new Headers({
            'Content-type': 'application/x-www-form-urlencoded',
        }),
    });
  let data = await response.json();
  location.reload();
  document.getElementById("amt").innerText = "$"+data.amount;
  document.getElementById("t_amt").innerText = "$"+data.total_amount;
  ele.parentNode.parentNode.remove()
}