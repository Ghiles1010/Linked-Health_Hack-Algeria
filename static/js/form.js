const selectedAll = document.querySelectorAll(".select");
const maladies_container = document.querySelector(".container.maladies");

$(".field.spe").hide(1);

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
	
	label.appendChild(textnode);
	
	div.appendChild(label);
	
	div.addEventListener("click",() => {
		
		div.remove();
	});
	
	chip_cont.appendChild(div);
	
	
	

	
}

/***********************************************************************************************/

const sang = document.querySelector(".select_box.sang .select label");
const rhesus = document.querySelector(".select_box.rhesus .select label");



options_rh = document.querySelector(".select_box.rhesus .container").querySelectorAll(".options");
options_sang = document.querySelector(".select_box.sang .container").querySelectorAll(".options");


options_sang.forEach( (bld) =>{

	bld.addEventListener("click", () => {
		
		txt = bld.querySelector("label").innerText;
		selectBlood(txt);
	});

}
)

options_rh.forEach( (rh) =>{

	rh.addEventListener("click", () => {
		
		txt = rh.querySelector("label").innerText;
		selectRH(txt);
	});

}
)

function selectRH(txt)
{

	rhesus.removeChild(rhesus.firstChild)
	
	var textnode = document.createTextNode(txt); 
	rhesus.appendChild(textnode);

	rh_container = document.querySelector(".select_box.rhesus .container")
	rh_container.classList.toggle("active");

}

function selectBlood(txt)
{

	
	sang.removeChild(sang.firstChild)
	var textnode = document.createTextNode(txt); 
	sang.appendChild(textnode);

	rh_container = document.querySelector(".select_box.sang .container")
	rh_container.classList.toggle("active");
}





/***********************************************************************************************/

$('#myform').submit(function(){ //listen for submit event

	$('<input />').attr('type', 'hidden')
		.attr('name', 'sang')
		.attr('value', sang.innerText)
		.appendTo('#myform');

	$('<input />').attr('type', 'hidden')
		.attr('name', 'rhesus')
		.attr('value', rhesus.innerText)
		.appendTo('#myform');

		




return true;
}); 

/************************************************************************************/

const switch_in = document.querySelector(".switch input");

med_section = document.querySelector("#dossier_medical");

switch_in.addEventListener("change", () => {

	
		if(med_section.style.display=="none")
		{
			$(".field.spe").show(500);
			$("#dossier_medical").show(500);
		}
		else
		{
			$(".field.spe").hide(500);
			$("#dossier_medical").hide(500);
		}



});
