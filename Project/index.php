<?php
if (isset($_POST['light'])) {
	echo $_POST['light'];
	$myfile = fopen("light.txt", "w");
	fwrite($myfile, $_POST['light']);
	fclose($myfile);
} else if (isset($_POST['temp'])) {
	echo $_POST['temp'];
	$myfile = fopen("temp.txt", "w");
	fwrite($myfile, $_POST['temp']);
	fclose($myfile);
} else if(isset($_GET['temp'])){
	$myfile = fopen("temp.txt", "r");
	echo fread($myfile,filesize("temp.txt"));
	fclose($myfile);
} else if(isset($_GET['light'])){
	$myfile = fopen("light.txt", "r");
	echo fread($myfile,filesize("light.txt"));
	fclose($myfile);
} else if(isset($_GET['light'])){
	$myfile = fopen("light.txt", "r");
	echo fread($myfile,filesize("light.txt"));
	fclose($myfile);
} 
?>
