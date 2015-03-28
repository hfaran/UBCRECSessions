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
	$("#teams").append('<div class="row"><div class="form-group col-sm-8"><input type="text" class="form-control team" id="team-name" placeholder="Team Name"></div><div class="form-group col-sm-4"><input type="number" class="form-control team" id="max-players" placeholder="Max"></div></div>');
}

function removeTeamField() {
	$(".row:last-child","#teams").remove();
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
	}).fail(function(response){
		alert(response.data)
		}).error(function(response){alert(response.message)});

	console.log("-addSession");
}


function addSessionSuccess(response) {
	console.log("+addSessionSuccess");
	console.log(response.data.session_id);
	// Add session completed successfully
	// Register the teams
	alert("Session Added");
	registerTeams(response.data.session_id);
	console.log("-addSessionSuccess");
}

function registerTeams(sessionID) {
	// Register each team in the HTML field
	$("#teams").children(".row").each(function() {
		// console.log($(this).children(".form-group").children("#team-name").val());
		// console.log($(this).children(".form-group").children("#max-players").val());
		var teamData = {
			name : $(this).children(".form-group").children("#team-name").val(),
			num_max_players : parseInt($(this).children(".form-group").children("#max-players").val()),
			session_id : sessionID
		};

		$.ajax({
			url : "/api/team/team/",
			type : "PUT",
			data : JSON.stringify(teamData),
			success : function(data) {
				alert(teamData['name'] + " was added to the session.")
			},
			dataType : "json"
		}).fail(function(response){
			alert(response.data)
			}).error(function(response){alert(response.message)});
	});
	
	window.location.assign("/static/index.html");
}