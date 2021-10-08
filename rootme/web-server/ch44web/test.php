#!/usr/bin/php
<?php
	$auth = @json_decode($_POST[’auth’], true) ;
	#’adminsdfqsdfqsdf’
	#’tedfgqsfqsdfslqzjqsd1247823st’
	$USER = 'someadmin' ;
	$PASSWORD_SHA256 = 'somepassword' ;

	if(0 == $USER )	
		if(!strcmp($argv[2], $PASSWORD_SHA256))
			echo "status : OK granted"."\n" ;
		else
			echo "status : password failed !"."\n" ;
	else
		echo "status : login failed !"."\n" ;
?>