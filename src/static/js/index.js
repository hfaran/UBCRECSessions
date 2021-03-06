var isAdmin = false;
var isStudent = false;
var isGuest = true;

// Wait for document to load before doing anything
$( document ).ready(function() {

    $('.input-daterange').datepicker({
		format: "yyyy-mm-dd",
		autoclose: true,
		orientation: "top left"
	});

	// Because are database entries are from the past, make the
	// default start date a fixed date
	var dateRightNow = new Date();
	var date7DaysFromNow = new Date();
	date7DaysFromNow.setDate(dateRightNow.getDate() + 7);
	dateRightNow.setDate(dateRightNow.getDate() - 7);
	$('#start-day').datepicker('setDate', dateRightNow);
	$('#end-day').datepicker('setDate', date7DaysFromNow);
	$('#start-day').datepicker('update');
	$('#end-day').datepicker('update');


	loadVenueOptions();
	loadSportsOptions();
	checkLoginStatus();
	

	// Add the loadSessions method to the 'Search Sessions' button
	$("#search-sessions").on("click", loadSessions);
	$("#my-sessions").on("click", loadMySessions);
});

function loadMySessions() {
	$.ajax({
		url : "/api/player/sessions/",
		type : "GET",
		data : null,
		success : loadSessionsSuccess,
		dataType : "json"
	}).fail(function(response){
		alert(response.data)
		}).error(function(response){alert(response.message)});;
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
	sessionsQueryData["venues"] = ["SRC_A","SRC_B","Thunderbird","Aquatic_Center","SRC_GYM","Testing"];
	// Add all selected venues to the venue list
	var noVenues = true;
	var venues = [];
	$("#venues option").each(function() {
		// Check if this venue is selected
		if($(this).is(':selected')) {
			venues.push($(this).text());
			noVenues = false;
		}
	});

	if(!noVenues) {
		sessionsQueryData["venues"] = venues;
	}

	// Clear the sport list
	sessionsQueryData["sports"] = ["Basketball","Croquet","Indoor Soccer","Table Tennis","Volleyball"];
	// Add all selected venues to the sport list
	var noSports = true;
	var sports = [];
	$("#sports option").each(function() {
		// Check if this sport is selected
		if($(this).is(':selected')) {
			sports.push($(this).text());
			noSports = false;
		}
	});

	if(!noSports) {
		sessionsQueryData["sports"] = sports;
	}

	// Get the start date
	var startDate = $('#start-day').datepicker('getDate');
	// Assign it within our object
	// JavaScript getTime is UNIX time in milliseconds, API wants seconds
	sessionsQueryData["started_after"] = startDate.getTime() / 1000;

	console.log("started_after: "+sessionsQueryData["started_after"]);

	// Get the end date
	var endDate = $('#end-day').datepicker('getDate');
	// Assign it within our object
	// JavaScript getTime is UNIX time in milliseconds, API wants seconds
	sessionsQueryData["ended_before"] = endDate.getTime() / 1000;
	console.log("ended_before: "+sessionsQueryData["ended_before"]);

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
	}).fail(function(response){
		alert(response.data)
		}).error(function(response){alert(response.message)});;
}

function loadSessionsSuccess(response) {
	// console.log("Load Session Success!\n");
	console.log(response.data);
	
	$("#session-holder").html('<div class="row session-table-header"><div class="col-sm-3">	<strong>Sport</strong></div><div class="col-sm-3">	<strong>Venue</strong></div><div class="col-sm-3">	<strong>Time</strong></div><div class="col-sm-3">	<strong id="results-actions">Results</strong></div></div>');
	
	// Go through each response and add it to the div
	for(var i = 0; i < response.data.length; i++) {
		var endTime = response.data[i]['end_time'];
		var startTime = response.data[i]['start_time'];
		var results = response.data[i]['results'];
		var venue = response.data[i]['venue_name'];
		var sport = response.data[i]['sport_name'];
		var sessionID = response.data[i]['session_id'];
		var numPlayers = response.data[i]['num_registered_players'];
		var numTeams = response.data[i]['num_teams'];
		var address = response.data[i]['venue_address'];
		
		var startDate = new Date(startTime * 1000);
		var endDate = new Date(endTime * 1000);

		var customHTML = results;

		if(isAdmin) {
			customHTML = '<button id="edit-results-'+sessionID+'" class="btn btn-sm btn-primary">Edit Results</button><button id="delete-session-'+sessionID+'" class="btn btn-sm btn-danger">Delete</button>';
		}

		$("#session-holder").append('<div class="row session-table-row"><div class="col-sm-3">	<strong>'+sport+'</strong>	<span class="sub-field">'+numTeams+' teams | '+numPlayers+' players</span></div><div class="col-sm-3">	<strong>'+venue+'</strong>	<span class="sub-field">'+address+'</div><div class="col-sm-3">	<strong>'+startDate.toLocaleString()+'</strong> - <strong>'+endDate.toLocaleString()+'</strong></div><div class="col-sm-3">'+customHTML+'</div></div>')

		if(!isAdmin) {
			$("#session-holder").append('<div id="session-'+sessionID+'" class="session-team-list"><div class="row">	<div class="col-sm-4 col-sm-offset-1 session-table-team-header">		<strong>Team Name</strong>	</div>	<div class="col-sm-4 session-table-team-header">		<strong>Max Players</strong>	</div>	<div class="col-sm-2 session-table-team-header">		<strong>Actions</strong>	</div></div></div>');

			// Open team list event, only call if user is student
			$(".session-table-row").off("click");
			$(".session-table-row").on("click", openTeams);
			$.ajax({
				url : "/api/team/teams/"+sessionID,
				type : "GET",
				data : null,
				success : loadTeamSuccess,
				dataType : "json"
			}).fail(function(response){
				alert(response.data)
				}).error(function(response){alert(response.message)});;
		} else {
			$("#delete-session-"+sessionID).on("click", function() {
					var sID = $(this).attr('id').split('-')[2];
					$.ajax({
						url : "/api/session/session/"+sID,
						type : "DELETE",
						data : null,
						success : deleteSessionSuccess,
						dataType : "json"
					}).fail(function(response){
						alert(response.data)
						}).error(function(response){alert(response.message)});
			});

			$("#edit-results-"+sessionID).on("click", function() {
					var results = prompt("What are the results?", "0 - 0");
					var sID = $(this).attr('id').split('-')[2];
					if (results != null) {
						var resData = {
							'results' : results,
							'session_id' : parseInt(sID)
						}
						$.ajax({
							url : "/api/session/session/",
							type : "PATCH",
							data : JSON.stringify(resData),
							success : function() {
								alert("Results updated!");
							},
							dataType : "json"
						}).fail(function(response){
							alert(response.data)
							}).error(function(response){alert(response.message)});
					}
			});
		}
	}

}

function deleteSessionSuccess(response) {
	loadSessions();
}

function loadTeamSuccess(response) {
	// console.log(response);
	for(var i = 0; i < response.data.length; i++) {
		var teamName = response.data[i]['name'];
		var maxPlayers = response.data[i]['num_max_players'];
		var teamID = response.data[i]['team_id'];
		var sessionID = response.data[i]['session_id'];

		var customHTML = '<button class="btn btn-sm btn-primary" disabled>You must be Signed In to join</button>';

		if(isStudent || true) {
			customHTML = '<button id="join-team-'+teamID+'" class="btn btn-sm btn-primary">Join</button>';
		}

		$("#session-"+sessionID).append('<div id="team-'+teamID+'" class="row session-table-team-row"><div class="col-sm-4 col-sm-offset-1">'+teamName+'</div><div class="col-sm-4">'+maxPlayers+'</div><div class="col-sm-2">'+customHTML+'</div></div>');

		$("#join-team-"+teamID).on("click", function(){
			var tID = $(this).attr('id').split('-')[2];
			console.log("tID:" + tID);
			var data = {
				team_id : parseInt(tID)
			};

			$.ajax({
				url : "/api/team/register/",
				type : "POST",
				data : JSON.stringify(data),
				success : teamRegisterSuccess,
				dataType : "json"
			}).fail(function(response){
				alert(response.data)
				}).error(function(response){alert(response.message)});
		});
	}
}

function teamRegisterSuccess(response) {
	var teamID = response.data.team_id;
	$("#join-team-"+teamID).html("Joined").prop('disabled', true);
}

function openTeams(sender) {
	$(sender.currentTarget).next('.session-team-list').toggleClass('picked-session').slideToggle();
	$(sender.currentTarget).toggleClass('picked-session');
}

function checkLoginStatus() {
	// console.log("+checkLoginStatus");
	// Check if Admin is logged in

	checkAdminLoggedIn();

	// console.log("-checkLoginStatus");
}

function checkAdminLoggedIn() {
	$.ajax({
		url : "/api/auth/employeelogin/",
		type : "GET",
		data : "",
		success : checkAdminSuccess,
		dataType : "json"
	}).fail(checkStudentLoggedIn);
}

function checkAdminSuccess() {
	// console.log("+checkAdminSuccess");
	isAdmin = true;
	isStudent = false;
	isGuest = false;
	updateHeader();
	// console.log("-checkAdminSuccess");
}

function checkStudentLoggedIn() {
	// console.log("+checkStudentLoggedIn");

	$.ajax({
		url : "/api/auth/playerlogin/",
		type : "GET",
		data : "",
		success : checkStudentSuccess,
		dataType : "json"
	}).fail(function(){
		isAdmin = false;
		isStudent = false;
		isGuest = true;
		updateHeader();
	});

	// console.log("-checkStudentLoggedIn");
}

function checkStudentSuccess() {
	// console.log("+checkStudentSuccess");
	isAdmin = false;
	isStudent = true;
	isGuest = false;
	updateHeader();
	// console.log("-checkStudentSuccess");
}

function updateHeader() {
	console.log("Admin : " + isAdmin);
	console.log("Student : " + isStudent);
	console.log("isGuest : " + isGuest);

	// Force student
	// isStudent = true;
	// isGuest = false;
	// isAdmin = false;
	loadSessions();

	if(isAdmin) {
		$("#admin-mask").show();
		$("#guest-mask").hide();
		$("#student-mask").hide();
		$("#results-actions").text("Actions");
	} else if(isStudent) {
		$("#admin-mask").hide();
		$("#guest-mask").hide();
		$("#student-mask").show();
		$("#results-actions").text("Results");
	} else {
		$("#admin-mask").hide();
		$("#guest-mask").show();
		$("#student-mask").hide();
		$("#results-actions").text("Results");
	}

}
