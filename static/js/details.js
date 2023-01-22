function calc(price)
{
  console.log('hello')
  var e = document.getElementById("selection");
  var value = e.options[e.selectedIndex].value;
  amount=price*value
  document.getElementById('price').innerHTML=amount+"$"
  console.log(amount)

}


// var btn = document.getElementById("btn");

// btn.addEventListener("click", function() {
// 	console.log("id")
// }, false);

