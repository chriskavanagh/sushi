$(function(){

    $('#email_form').submit(function(event) {
        event.preventDefault();
        console.log("form submitted!")
        $.ajax({
            type: "POST",
            url: "customer/send-email/",
            dataType: "json",
            data: { 
                'email' : $('#email_text').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },

            success: searchSuccess,            
        });
        
    });

});

function searchSuccess(data, textStatus, jqXHR)
{    
    alert(data.message);
}

