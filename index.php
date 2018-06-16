<?php 

    function redirect() {
        $db_host = "localhost";
        $db_user = "guest";
        $db_passw = "password";
        $mysqli = new mysqli($db_host, $db_user, $db_passw, "invite");

        if($mysqli->connect_error) {
            echo "DB connection error";
            return 0;
        }

        $hash = ltrim($_SERVER["REQUEST_URI"], "/");
        $query = "SELECT name, hash FROM invited_people WHERE hash='$hash'";

        try {
            $result = $mysqli->query($query);
        }
        catch(Exception $e){
            echo "Error connecting to db";
            return 0;
        }

        $row_count = $result->num_rows;
        $row = $result->fetch_row();
        $name = $row[0];
        $hash = $row[1];
        
        if($row_count > 0 ) {
            session_start();
            $_SESSION["name"] = $name;
            $_SESSION["hash"] = $hash;
            header("Location: php_files/homepage.php");
            exit();
        }
        else {
            header("Location: html/error.html");
            exit();
        }
    }

    redirect()

?>