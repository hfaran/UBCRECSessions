// Wait for document to load before doing anything
$( document ).ready(function() {

    $('.input-daterange').datepicker({
		format: "yyyy-mm-dd",
		autoclose: true,
		orientation: "top left"
	});

	var dateRightNow = new Date();
	var date7DaysFromNow = new Date();
	date7DaysFromNow.setDate(dateRightNow.getDate() + 7);
	$('#start-day').datepicker('setDate', dateRightNow);
	$('#end-day').datepicker('setDate', date7DaysFromNow);
	$('#start-day').datepicker('update');
	$('#end-day').datepicker('update');

	loadVenueOptions();
	loadSportsOptions();
	loadSessions();
	// @TODO Load Venues options for search

	// Add the loadSessions method to the 'Search Sessions' button
	$("#search-sessions").on("click", loadSessions);

	// Open team list event, only call if user is student
	$(".session-table-row").on("click", openTeams);
});


// This function starts an AJAX call to load the venues
function loadVenueOptions() {
	$.ajax({
		url : "/api/venue/venues/?",
		type : "GET",
		data : null,
		success : loadVenueOptionsSuccess,
		dataType : "json"
	});
}

function loadVenueOptionsSuccess(response) {
	console.log("+loadVenueOptionsSuccess");
	//console.log(response);
	
	// Go through each response and add it to the div
	for(var i = 0; i < response.data.length; i++)
	{
		var venue = response.data[i].name;
		console.log(venue);
		venueOption = new Option(venue, venue, false, false);
		document.all.venues.options.add(venueOption);
	}
	console.log("-loadVenueOptionsSuccess")
}

// This function starts an AJAX call to load the sports
function loadSportsOptions() {
	$.ajax({
		url : "/api/sport/sports/?",
		type : "GET",
		data : null,
		success : loadSportsOptionsSuccess,
		dataType : "json"
	});
}

function loadSportsOptionsSuccess(response) {
	console.log("+loadSportsOptionsSuccess");
	//console.log(response);
	
	// Go through each response and add it to the div
	for(var i = 0; i < response.data.length; i++)
	{
		var sport = response.data[i].name;
		//console.log(sport);
		sportOption = new Option(sport, sport, false, false);
		document.all.sports.options.add(sportOption);
	}
	
	console.log("-loadSportsOptionsSuccess")
}


// This function builds the sessionsQueryData object and sends the AJAX call
function loadSessions() {
	// This data structure is sent to the API when searching for queries
	// Empty venues or sports will return all venues or sports
	// started_after and ended_before is UNIX timestamp
	var sessionsQueryData = {
		"venues" : [],
		"sports" : [],
		"started_after" : 0,
		"ended_before" : 0
	}

	// Clear the venue list
	sessionsQueryData["venues"] = [];
	// Add all selected venues to the venue list
	$("#venues option").each(function() {
		// Check if this venue is selected
		if($(this).is(':selected')) {
			sessionsQueryData["venues"].push($(this).val());
		}
	});

	// Clear the sport list
	sessionsQueryData["sports"] = [];
	// Add all selected venues to the sport list
	$("#sports option").each(function() {
		// Check if this sport is selected
		if($(this).is(':selected')) {
			sessionsQueryData["sports"].push($(this).val());
		}
	});

	// Get the start date
	var startDate = $('#start-day').datepicker('getDate');
	// Assign it within our object
	// JavaScript getTime is UNIX time in milliseconds, API wants seconds
	sessionsQueryData["started_after"] = startDate.getTime() / 1000;

	// Get the end date
	var endDate = $('#end-day').datepicker('getDate');
	// Assign it within our object
	// JavaScript getTime is UNIX time in milliseconds, API wants seconds
	sessionsQueryData["ended_before"] = endDate.getTime() / 1000;

	// Print it for debugging
	console.log(sessionsQueryData);

	// Perform the AJAX HTTP request
	// We're using a POST here which is bad practice when GETting data
	// But for the sake of time, we're using POST
	$.ajax({
		url : "/api/session/sessions/",
		type : "POST",
		data : JSON.stringify(sessionsQueryData),
		success : loadSessionsSuccess,
		dataType : "json"
	});
}

function loadSessionsSuccess(data) {
	// @TODO Generated rows for each sessions
	console.log("Load Session Success!\n");
	console.log(data);
}

function openTeams(sender) {
	console.log(sender.currentTarget);
	$(sender.currentTarget).next('.session-team-list').toggleClass('picked-session').slideToggle();
	$(sender.currentTarget).toggleClass('picked-session');
}