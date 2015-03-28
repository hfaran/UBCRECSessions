$( document ).ready(function() {
	loadSchedule();
});


function loadSchedule() {

	// Get days from now until 7 days from now
	var dateRightNow = new Date();
	var date7DaysFromNow = new Date();
	date7DaysFromNow.setDate(dateRightNow.getDate() + 365);

	var scheduleDates = {
		"end" : date7DaysFromNow.getTime(),
		"start" : 0
	}

	console.log(scheduleDates);

	$.ajax({
		url : "/api/employee/schedule/",
		type : "POST",
		data : JSON.stringify(scheduleDates),
		success : loadScheduleSuccess,
		dataType : "json"
	}).fail(function(response){
		alert(response.data)
		}).error(function(response){alert(response.message)});
}

function loadScheduleSuccess(response) {
	console.log("Load Schedule Success!");
	console.log(response)

	// Add each shift to the table
	for(var i = 0; i < response.data.length; i++)
	{
		var newShift = document.createElement('div');
		newShift.className = 'row schedule-table-row';


		// Unix Time is multiplied by 1000 for JS
		var startTime = new Date(response.data[i].start_time * 1000);
		var endTime = new Date(response.data[i].end_time * 1000);
		var username = response.data[i].username;

		var usernameDiv = document.createElement('div');
		usernameDiv.className = "col-md-4";
		usernameDiv.innerText = username;
		newShift.appendChild(usernameDiv);


		var startTimeDiv = document.createElement('div');
		startTimeDiv.className = "col-md-4";
		startTimeDiv.innerText = startTime.toLocaleTimeString()
			+ " " + startTime.toLocaleDateString();
		newShift.appendChild(startTimeDiv);

		var endTimeDiv = document.createElement('div');
		endTimeDiv.className = "col-md-4";
		endTimeDiv.innerText = endTime.toLocaleTimeString()
			+ " " + endTime.toLocaleDateString()
		newShift.appendChild(endTimeDiv);


		console.log(startTime);
		console.log(endTime);

		//console.log(shiftText);

		$("#body")[0].appendChild(newShift);

		//console.log(sport);
		//sportOption = new Option(sport, sport, false, false);
		//document.all.sports.options.add(sportOption);
	}
}



