<?php 
    if($_POST["action"] == "update_response") {
        
        if($_POST["response"] == "0" || $_POST["response"] == "1") {
            update_response($_POST["response"], $_POST["hash"]);
        }
        else {
            echo "error";
        }
    }

    function update_response($response, $hash) {
        $db_host = "localhost";
        $db_user = "guest";
        $db_passw = "password";
        $mysqli = new mysqli($db_host, $db_user, $db_passw, "invite");
        $error_msg = "Infelizmente ocorreu um erro. Por favor tente mais tarde";

        if($mysqli->connect_error) {
            echo $error_msg;
            return 0;
        }

        $query = "UPDATE invited_people SET response='$response' WHERE hash='$hash';";

        try{
            $mysqli->query($query);
        }
        catch(Exception $e) {
            echo $error_msg;
            return 0;
        }

        echo "A sua resposta foi submetida com sucesso, obrigado";
    }
?>