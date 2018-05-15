
jQuery(document).ready(function($) {
/***
sidebar navigation
**/
    $('[data-click] li').click(function() {
    $('#target').text($(this).find('span').text())
    });

/*
    $('[data-details]').click(function() { alert("details")
    })
*/

    $('[data-tourney]').click(function() { alert("tourney")
    })


/*
    $('[data-player]').click(function() {

                $('#ApllyTournament :input').each(function(){
                    $(this).val('');
                });
    })*/


    $('#new_player').click(function() {
        $( "input[name='email']" ).val('');
        $( "input[name='name']" ).val('');
        $( "input[name='number']" ).val('');
    })

    $('[data-settings]').click(function() { alert("settings")
    })


});


$(function(){
  $('[data-toggle="popover"]').popover({ trigger: "hover" })
});


// this is the id of the form
$(function() {
    $('#tag-form-submit').on('click', function(e) {
        $('#loading-indicator').show();
        $("#result").html("");
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: url_ajax,
            data: $('#ApllyTournament').serialize(),
            dataType: 'json',
            success: function(response) {
              if (response.is_taken) {
               // alert(response.error_message);
                $("#result").html(response.error_message);
              //adding class
                $("#result").addClass("alert alert-success");
                $('#result').fadeIn();
                $('#result').fadeOut( 2500,"linear" );
                $('#loading-indicator').hide();
              }
            },
            error: function (result) {
                $("#result").html(result);
              //adding class
                $("#result").addClass("alert alert-danger");
                $('#result').fadeIn();
                $('#result').fadeOut( 2500,"linear" );
                $('#loading-indicator').hide();

            }
        });

        return false;
    });
});

function remove_tr(id){
var element_tr = "tr[data-id="+id+"]"
// Chrome don't hide popover after remove it's parent reference
$(element_tr).find("[data-toggle=popover]").popover('hide');
$(element_tr).remove()

return false;
};