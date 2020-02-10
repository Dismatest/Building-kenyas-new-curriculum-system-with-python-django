//set button id on click to hide first modal
$("#signin").on("click", function() {
  $("#myModal1").modal("hide");
});
//trigger next modal
$("#signin").on("click", function() {
  $("#myModal2").modal("show");
});

//accordian script
const accordian = document.querySelector(".accordian");
const item = accordian.querySelectorAll(".li");
const questions = accordian.querySelectorAll(".question");

function toggleAccordian() {
  const thiseItem = this.parentNode;
  thiseItem.classList.toggle("open");
}

questions.forEach(question =>
  question.addEventListener("click", toggleAccordian)
);
//end of accordian script
