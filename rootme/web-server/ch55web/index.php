<?php
function gen_secured_random() { // cause random is the way
    $a = rand(1337,2600)*42;
    $b = rand(1879,1955)*42;

    $a < $b ? $a ^= $b ^= $a ^= $b : $a = $b;

    return $a+$b;
}

function secured_hash_function($plain) { // cause md5 is the best hash ever
    $secured_plain = sanitize_user_input($plain);
    return md5($secured_plain);
}

function sanitize_user_input($input) { // cause someone told me to never trust user input
    $re = '/[^a-zA-Z0-9]/';
    $secured_input = preg_replace($re, "", $input);
    return $secured_input;
}

if (isset($_GET['source'])) {
    show_source(__FILE__);
    die();
}


require_once "secret.php";
echo "\n";
$string = $argv[1];
$hash  = $argv[2];
if (isset($string) && isset($hash)){
    $s = sanitize_user_input($string);
    print 's is: '.$s;
    print "\n";
    $h = secured_hash_function($hash);
    print 'h is: '.$h;
    print "\n";
    $r = gen_secured_random();
    print 'r is: '.$r;
    print "\n";
    if($s != false && $h != false) {

        print 'Concatenation is: '.$s.$r."\n";
        if($s.$r == $h) {
            print "Well done! Here is your flag: ".$flag;
        }
        else {
            print "Fail..."."\n";
        }
    }
    else {
        print "<p>Hum ...</p>"."\n";
    }
}
?>