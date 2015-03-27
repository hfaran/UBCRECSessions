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
	checkLoginStatus();

	// Add the loadSessions method to the 'Search Sessions' button
	$("#search-sessions").on("click", loadSessions);

	// Open team list event, only call if user is student
	$(".session-table-row").on("click", openTeams);
});


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

function checkLoginStatus() {
	console.log("+checkLoginStatus");
	// Check if Admin is logged in
	
	$("#guest-mask").show();
	
	//$.ajax({
	//	url : "/api/auth/employeelogin/",
	//	type : "GET",
	//	data : null, 
	//	success : checkAdminSuccess,
	//	dataType : "json"
	//}).fail(checkStudentLoggedIn);
	
	console.log("-checkLoginStatus");
}

function checkAdminSuccess() {
	console.log("+checkAdminSuccess");
	$("#guest-mask").hide();
	$("#student-mask").hide();
	$("#admin-mask").show();
	console.log("-checkAdminSuccess");
}

function checkStudentLoggedIn() {
	console.log("+checkStudentLoggedIn");
	
	$.ajax({
		url : "/api/auth/employeelogin/",
		type : "POST",
		data : JSON.stringify(sessionsQueryData),
		success : loadSessionsSuccess,
		dataType : "json"
	}).fail(function(){
			$("#guest-mask").show();
			$("#student-mask").hide();
			$("#admin-mask").hide();
			console.log("No user logged in");
		});
		
	console.log("-checkStudentLoggedIn");
}

function checkStudentSuccess() {
	console.log("+checkStudentSuccess");
	$("#guest-mask").hide();
	$("#student-mask").show();
	$("#admin-mask").hide();
	console.log("-checkStudentSuccess");
}