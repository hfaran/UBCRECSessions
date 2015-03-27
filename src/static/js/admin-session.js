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
		"sport_id" : -1,
		"venue_name" : ""
	};

	// Obtain date-time values
	var sport_id = parseInt($("#sports").val());
	var venue_name = $("#venues").val();
	var start_time = $('#start-time').data("DateTimePicker").date();
	var end_time = $('#end-time').data("DateTimePicker").date();

	// Error Check Time
	if(start_time == null || end_time == null) {
		alert("Please enter valid start and end dates.");
		return;
	}

	// Check for valid venue
	if(venue_name == "") {
		alert("Choose a valid venue");
	}

	// Check for valid sport
	if(sport_id == -1) {
		alert("Choose a valid sport");
	}


	// Check if any teams were added
	var numTeams = $("#teams > div").length;
	for(i = 0; i < $("#teams > div").length; i++){
		formDiv = $("#teams > div")[i];

		console.log(formDiv.length);
	}

	console.log(numTeams);

	// Convert to unix time
	start_time = start_time.unix();
	end_time = end_time.unix();

	addSessionData["start_time"] = start_time;
	addSessionData["end_time"] = end_time;
	addSessionData["venue_name"] = venue_name;
	addSessionData["sport_id"] = sport_id;

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