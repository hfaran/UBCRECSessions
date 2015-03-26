$( document ).ready(function() {
	$("#start-time").datetimepicker({sideBySide: true});
	$("#end-time").datetimepicker({sideBySide: true});
	
	
	$("#admin-sign-in").on("click", signIn);
});


function signIn() {
	console.log("Admin Sign In");
	
	var loginQueryData = {
		//"properties": {
			"username" : '',
			"password" : ''
		//}//,
		//"type" : "object"
	}
	
	
	// Obtain username/password from HTML
	var username = document.getElementById('employee-username').value;
	var password = document.getElementById('employee-password').value;
	
	if(username == '' || password == '') {
		console.log("Missing credentials!");
		return;
	}
	console.log("Username/Password");
	console.log(username);
	console.log(password);
	
	// Create query data
	loginQueryData["username"] = username;
	loginQueryData["password"] = password;
	
	console.log(loginQueryData);
	
	// Make asynchronous callback
	$.ajax({
		url : "/api/auth/employeelogin/?",
		type : "POST",
		data : JSON.stringify(loginQueryData),
		success : employeeLoginSuccess,
		dataType : "json"
	}).fail(function(){
		alert("Incorrect username/password!")
		});

}

function employeeLoginSuccess(response) {
	console.log(response);
	
	success = (response.status == "success");

	console.log(success);
	
	window.location.assign("/static/index.html");
}






