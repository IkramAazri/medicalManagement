var li_elements = document.querySelectorAll(".wrapper_left ul li");
var item_elements = document.querySelectorAll(".item");
for (var i = 0; i < li_elements.length; i++) {
  li_elements[i].addEventListener("click", function() {
    li_elements.forEach(function(li) {
      li.classList.remove("active");
    });
    this.classList.add("active");
    var li_value = this.getAttribute("data-li");
    item_elements.forEach(function(item) {
      item.style.display = "none";
    });
    if (li_value == "pd") {
      document.querySelector("." + li_value).style.display = "block";
    } else if (li_value == "terrain") {
      document.querySelector("." + li_value).style.display = "block";
    }
    else if (li_value == "exploration") {
      document.querySelector("." + li_value).style.display = "block";
    } else if (li_value == "elem") {
      document.querySelector("." + li_value).style.display = "block";
    } else if (li_value == "decision") {
      document.querySelector("." + li_value).style.display = "block";
      document.getElementById(accountDiv.style.display="none");
      document.getElementById(profileDiv.style.display="none");
      document.getElementById(hintsDiv.style.display="none");
    } else {
      console.log("");
    }
  });
}
    function toggle_visibility(id) {
       var e = document.getElementById(id);
       if(e.style.display == 'block')
          e.style.display = 'none';
       else
          e.style.display = 'block';
    }