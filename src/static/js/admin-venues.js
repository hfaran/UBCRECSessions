$( document ).ready(function() {
	$("#add-venue").on("click", addVenue);
});


function addVenue() {
	console.log("Admin Sign In");
	
	var addVenueData = {
		"address" : '',
		"name" : ''
	}
	
	
	// Obtain username/password from HTML
	var name = document.getElementById('venue-name').value;
	var address = document.getElementById('venue-address').value;
	
	if(name == '') {
		console.log("Missing Venue Name!");
		return;
	}
	console.log("Adding new venue:");
	console.log(name)
	console.log(address);
	
	// Create query data
	addVenueData["address"] = address;
	addVenueData["name"] = name;
	
	console.log(addVenueData);
	
	// Make asynchronous callback
	$.ajax({
		url : "/api/venue/venue",
		type : "PUT",
		data : JSON.stringify(addVenueData),
		success : employeeLoginSuccess,
		dataType : "json"
	}).fail(function(response){
		alert(response.data)
		}).error(function(response){alert(response.message)});

}

function employeeLoginSuccess(response) {
	console.log(response);
	
	success = (response.status == "success");

	console.log(success);
	
	window.location.assign("/static/index.html");
}






