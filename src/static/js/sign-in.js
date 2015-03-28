$( document ).ready(function() {
	$("#sign-in").on("click", signIn);
});


function signIn() {
	console.log("Student Sign In");
	
	var loginQueryData = {
		"student_number" : 0,
		"password" : ''
	}
	
	
	// Obtain username/password from HTML
	var student_number = document.getElementById('student-number').value;
	var password = document.getElementById('student-password').value;
	
	if(student_number == '' || password == '') {
		console.log("Missing credentials!");
		return;
	}
	console.log("Student_number/Password");
	console.log(student_number);
	console.log(password);
	
	// Create query data
	loginQueryData["student_number"] = parseInt(student_number, 10);
	loginQueryData["password"] = password;
	
	console.log(loginQueryData);
	
	// Make asynchronous callback
	$.ajax({
		url : "/api/auth/playerlogin/?",
		type : "POST",
		data : JSON.stringify(loginQueryData),
		success : studentLoginSuccess,
		dataType : "json"
	}).fail(function(){
		alert(response.data)
		}).error(function(){alert(response.message)});

}

function studentLoginSuccess(response) {
	console.log(response);
	
	success = (response.status == "success");

	console.log(success);
	
	window.location.assign("/static/index.html");
}






