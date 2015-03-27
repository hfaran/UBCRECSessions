function logout() {
	console.log("Admin Sign In");
	
	// Make asynchronous callback
	$.ajax({
		url : "/api/auth/logout/?",
		type : "DELETE",
		data : null,
		success : logoutSuccess,
		dataType : "json"
	}).fail(function(){
			// Simply reload the page, user is not logged in
			window.location.assign("/static/index.html");
		});
	
}

function logoutSuccess(response) {
	console.log(response);
	
	success = (response.status == "success");

	console.log(success);
	console.log("Successfully logged out!");
	
	window.location.assign("/static/index.html");
}






