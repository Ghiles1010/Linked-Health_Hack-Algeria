const selectedAll = document.querySelectorAll(".select");
const maladies_container = document.querySelector(".container.maladies");


selectedAll.forEach( (selected) => {
	
	const container = selected.nextElementSibling;
	const searchBox = container.querySelector(".search_box input");

	const options = document.querySelectorAll(".options");


	selected.addEventListener("click",() => {
	
		container.classList.toggle("active");
	});

	
	if(searchBox != null){
		
		searchBox.addEventListener("keyup", function(e){
		
			filterList(e.target.value);
		});
	}

	const filterList = searchTerm => {
	searchTerm = searchTerm.toLowerCase();
	
	options.forEach(option => {
	let label = option.firstElementChild.nextElementSibling.innerText.toLowerCase();
	
	if (label.indexOf(searchTerm) != -1) {
		
		option.style.display = "block";
	} else {
	  option.style.display = "none";
    }
  });
};
	
	
})



const mal_options = maladies_container.querySelectorAll(".options");

mal_options.forEach( (maladie) =>{

		maladie.addEventListener("click", () => {
			
			
			addChip(maladie.firstElementChild.nextElementSibling.innerText);
		});

	}
)

function addChip(text){
	
	const chip_cont = document.querySelector("#selected");
	
	var div = document.createElement("div");
	div.setAttribute("class", "chip");

	var label = document.createElement("label");
	
	var textnode = document.createTextNode(text);
	textnode.setAttribute("name", 'maladie');

	label.appendChild(textnode);
	
	div.appendChild(label);
	
	div.addEventListener("click",() => {
		
		div.remove();
	});
	
	chip_cont.appendChild(div);
	
	
	
}
