$( document ).ready(function() {
	$("#start-time").datetimepicker({sideBySide: true});
	$("#end-time").datetimepicker({sideBySide: true});
	$("#remove-team-field").on("click", removeTeamField);
	$("#add-team-field").on("click", addTeamField);
});

function addTeamField() {
	$("#teams").append('<div class="form-group"><input type="text" class="form-control team" placeholder="Team Name"></div>');
}

function removeTeamField() {
	$(".form-group:last-child","#teams").remove();
}