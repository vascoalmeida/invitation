<!DOCTYPE html>
<html>
    <head>
        <title>Convite</title>
        <meta charset="utf-8">
        <link href="https://fonts.googleapis.com/css?family=Playfair+Display" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="../css/index.css">
        <script src="../js/jquery.js"></script>
        <script src="../js/index.js"></script>
    </head>
    <body>
        <?php session_start() ?>
        <div id="title" class="slide_down_fade">Bem-vindo/a, <?php echo $_SESSION["name"] ?></div>
        <div id="video_container">
            <iframe id="pres_video"  class="slide_down_fade" src="https://www.youtube.com/embed/aYsaC2CADs0?ecver=2" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        </div>
        <div id="answer" class="slide_down_fade">
            <div id="answer_text">Contamos consigo?</div>
            <div id="buttons_container" data-hash="<?php echo $_SESSION['hash'] ?>">
                <div class="button_wrap">
                    <div class="button" data-response="1">Vou</div>
                </div>
                <div class="button_wrap">
                    <div class="button" data-response="0">Não vou</div>
                </div>
            </div>
        </div>
    </body>
</html>