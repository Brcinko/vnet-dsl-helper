function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}

function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}


products = {
	'product_list' : [
		{
			'name' : 'ADSL Partner Naked',
			'speed': ['L', 'M', 'H']
		},
		{
			'name' : 'VDSL Partner Naked',
			'speed' : ['L', 'H']
		}
	]
}

function setProductDropdown(){
	var box = document.getElementById("productSelect");
	products.product_list.forEach(function(item){

	for (var i = 0, len = item.speed.length; i < len; i++) {
		var opt = document.createElement("option");
		console.log(item.name, item.speed[i]);
		var opt = document.createElement("option");
	    name = item.name + ' ' + item.speed[i];
	    opt.value = name;
	    opt.innerHTML = name;
	    box.appendChild(opt);	  
	}

	});
}

function getNewReqValues(){
	request = {}
	check_flag = 0;
	//get product name from dropdown menu
	var x =  document.getElementById("productSelect").selectedIndex;
	var products = document.getElementById("productSelect").options;
	if (x == 0) {
		check_flag = 1;
		document.getElementById("productWarning").style.display = "block";
	}

	console.log(products[x].text);
	request.product_name = products[x].text;
	
	// Get contanct person data
	request.contact = {};
	request.contact.FirstName = document.getElementById("contactFirstName").value;
	if (request.contact.FirstName == null || request.contact.FirstName == "") {
		check_flag = 1;
		document.getElementById("firstNameWarning").style.display = "block";
	}
	request.contact.LastName = document.getElementById("contactLastName").value;
	if (request.contact.LastName == null || request.contact.LastName == "") {
		check_flag = 1;
		document.getElementById("lastNameWarning").style.display = "block";
	}
	request.contact.ContPhone = document.getElementById("contactNumber").value;
	if (request.contact.ContPhone == null || request.contact.ContPhone == "") {
		check_flag = 1;
		document.getElementById("phoneNumberWarning").style.display = "block";
	}

	//Get address data
	request.address= {}
	request.address.StreetName = document.getElementById("StreetName").value;
	if (request.contact.StreetName == null || request.contact.StreetName == "") {
		check_flag = 1;
		document.getElementById("streetWarning").style.display = "block";
	}
	request.address.AddressNum = document.getElementById("AddressNum").value;
	request.address.ApartmentNum = document.getElementById("ApartmentNum").value;
	request.address.BlockNum = document.getElementById("BlockNum").value;
	request.address.EvidencialNum = document.getElementById("EvidencialNum").value;
	request.address.Floor = document.getElementById("Floor").value;
	request.address.ZIPCode = document.getElementById("ZIPCode").value;
	if (request.contact.ZIPCode == null || request.contact.ZIPCode == "") {
		check_flag = 1;
		document.getElementById("ZIPCodeWarning").style.display = "block";
	}
	request.address.City = document.getElementById("City").value;
	if (request.contact.City == null || request.contact.City == "") {
		check_flag = 1;
		document.getElementById("CityWarning").style.display = "block";
	}
	request.address.Country = 'Slovakia (Slovak Republic)';

	console.log(request);

	if (check_flag != 0){
		alert("Je nutne vyplnit vsetky povinne polia oznacene hviezdickou");
		return 1
	}
	if (check_flag == 0){
		//API call na backend
	}
}