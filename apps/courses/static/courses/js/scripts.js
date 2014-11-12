// JS for AddToSchedule and EditCourse functionality in offering_details

var loadAddToSchedule = function(url) {
    $('#addtoschedule').dialog('open');
}

$("#addtoschedule").dialog({
        autoOpen: false,
        bgiframe: true,
        height: 300, width: 450,
        modal: false
    });

$( "#course_edit_button" ).click(function() {
        $( "#course_edit_form" ).toggle( "slow", function() {
    });
});
