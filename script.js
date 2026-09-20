const DIV_principal = ["overlay",]

function open(const DIV){
  for(let i = 0; i < DIV_principal.length;++i){
    document.getElementById(DIV_principal[i]).style.display =  "none";
  }
  document.getElementById(DIV).style.display = "block";
  document.getElementById("overlay").style.display = "block";
}
