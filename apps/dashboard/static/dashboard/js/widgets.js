
function order_tasks(data) {
    // JQuery .sortable() provides a serialize() function which provides the re-ordered
    // data in a list. We POST that list to a Django view
    // to save the re-ordered data into the database.

    $.post("/dashboard/reorder", data, "json");
    return false;
};

$(function() {
	$(document).ready(function() {
		$('#sortable').sortable({
	    	update: function() {
	        	var data = $('#sortable').sortable('serialize');
	        	order_tasks(data);
	        }
	    });
	});
});
