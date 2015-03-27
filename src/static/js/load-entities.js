// This function starts an AJAX call to load the venues
function loadVenueOptions() {
	$.ajax({
		url : "/api/venue/venues/?",
		type : "GET",
		data : "",
		success : loadVenueOptionsSuccess,
		dataType : "json"
	});
}

function loadVenueOptionsSuccess(response) {
	// console.log("+loadVenueOptionsSuccess");
	//console.log(response);
	
	// Go through each response and add it to the div
	for(var i = 0; i < response.data.length; i++)
	{
		var venue = response.data[i].name;
		//console.log(venue);
		venueOption = new Option(venue, venue, false, false);
		document.all.venues.options.add(venueOption);
	}
	// console.log("-loadVenueOptionsSuccess")
}

// This function starts an AJAX call to load the sports
function loadSportsOptions() {
	$.ajax({
		url : "/api/sport/sports/?",
		type : "GET",
		data : "",
		success : loadSportsOptionsSuccess,
		dataType : "json"
	});
}

function loadSportsOptionsSuccess(response) {
	// console.log("+loadSportsOptionsSuccess");
	//console.log(response);
	
	// Go through each response and add it to the div
	for(var i = 0; i < response.data.length; i++)
	{
		var sport = response.data[i].name;
		var sport_id = response.data[i].sport_id;
		//console.log(sport);
		sportOption = new Option(sport, sport_id, false, false);
		document.all.sports.options.add(sportOption);
	}
	
	// console.log("-loadSportsOptionsSuccess")
}

