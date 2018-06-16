$(function() {
    $(".button").click(function() {
        $.ajax({
            url: "../php_files/response.php",
            method: "POST",
            data: {
                action: "update_response",
                hash: $("#buttons_container").attr("data-hash"),
                response: $(this).attr("data-response"),
            },
            success: function(data) {
                alert(data);
            },
        })
    });
});
