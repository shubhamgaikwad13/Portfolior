let forms = document.querySelectorAll(".form");
let icons = document.querySelectorAll(".side-icon");
let currentStep = 0;
const nextBtn = document.querySelector("#nextbtn");
const prevBtn = document.querySelector("#prevbtn");
const submitBtn = document.querySelector("#submitBtn");

function changeStep(action) {
  forms[currentStep].style.display = "none";
  icons[currentStep].style.display = "none";
  console.log(currentStep)
  currentStep = action == "prev" ? currentStep - 1 : currentStep + 1;
  forms[currentStep].style.display = "block";
  icons[currentStep].style.display = "block";
  console.log(currentStep)
  nextBtn.style.display = "inline-block";
  submitBtn.style.display = "none";

  if (currentStep == 0) prevBtn.style.display = "none";
  else prevBtn.style.display = "inline-block";

  if (currentStep == forms.length - 1) {
    nextBtn.style.display = "none";
    submitBtn.style.display = "inline-block";
  }
}

nextBtn.addEventListener("click", function () {
  changeStep("next");
});

prevBtn.addEventListener("click", function () {
  changeStep("prev");
});
