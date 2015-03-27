$( document ).ready(function() {
	$("#start-time").datetimepicker({sideBySide: true});
	$("#end-time").datetimepicker({sideBySide: true});
	$("#remove-team-field").on("click", removeTeamField);
	$("#add-team-field").on("click", addTeamField);
	$("#add-session").on("click", addSession);
	
	
	loadVenueOptions();
	loadSportsOptions();
});

function addTeamField() {
	$("#teams").append('<div class="form-group"><input type="text" class="form-control team" placeholder="Team Name"></div>');
}

function removeTeamField() {
	$(".form-group:last-child","#teams").remove();
}

function addSession() {
	console.log("+addSession");
	
	var addSessionData = {
		"start_time" : 0,
		"end_time" : 0,
		"sport_id" : 0,
		"venue_name" : ""
	};
	
	// Obtain date-time values
	var sport_id = $("#sports").val();
	var venue_name = $("#venues").val();
	var start_time = $('#start-time').data("datetimepicker").getDate();
	// Assign it within our object
	// JavaScript getTime is UNIX time in milliseconds, API wants seconds
	addSessionData["start_time"] = start_time / 1000;
	var end_time = $('#end-time').data("datetimepicker").getDate();
	// Assign it within our object
	// JavaScript getTime is UNIX time in milliseconds, API wants seconds
	addSessionData["end_time"] = end_time / 1000;
	
	
	// Error Check Values
	if(start_time == 0 || end_time == 0) {
		alert("Please enter valid start and end dates.");
		return;
	}
	
	console.log(addSessionData);

	$.ajax({
		url : "/api/session/session/",
		type : "PUT",
		data : JSON.stringify(addSessionData),
		success : addSessionSuccess,
		dataType : "json"
	});
	
	console.log("-addSession");
}


function addSessionSuccess(response) {
	console.log("+addSessionSuccess");
	console.log(response);
	// Add session completed successfully
	// Register the teams
	registerTeams();
	console.log("-addSessionSuccess");
}

function registerTeams() {
	// Register each team in the HTML field
}