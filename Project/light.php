<!DOCTYPE HTML>  
<html>
<head>
<title>Study Buddy</title>
<style>
.error {color: #FF0000;}
</style>
</head>
<body> 

<h1>Study Buddy</h1>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["light"])) {
    $lightErr = "Light is requibright";
  } else {
    $light = test_input($_POST["light"]);
    echo $light; 
  }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

?>


<form id="mail_subscribe">
  <input type="radio" name="light" <?php if (isset($light) && $light=="bright") echo "checked";?> value="bright">bright
  <input type="radio" name="light" <?php if (isset($light) && $light=="medium") echo "checked";?> value="medium">medium
  <input type="radio" name="light" <?php if (isset($light) && $light=="low") echo "checked";?> value="low">low
  <input type="radio" name="light" <?php if (isset($light) && $light=="30") echo "checked";?> value="30">auto
  <span class="error">* <?php echo $lightErr;?></span>
  <br><br>

  <input type="submit" name="submit" value="Submit">  
</form>



</body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

<script>
$('#mail_subscribe').submit(function() {
  var post_data = $('#mail_subscribe').serialize();
  $.post('http://128.199.190.200/index.php?light=2', post_data, function(data) {
    $('#notification').show();
  });
});
$('#mail_subscribe').submit(function() {
  var post_data = $('#mail_subscribe').serialize();
  $.post('http://128.199.190.200/index.php', post_data, function(data) {
    $('#notification').show();
  });
});
</script>
</html>
