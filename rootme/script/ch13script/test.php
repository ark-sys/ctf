<?php
	$iterator=new DirectoryIterator(dirname(__FILE__));
	foreach ($iterator as $fileinfo) {
		if($fileinfo->isFile()){
			echo $fileinfo->getFilename()."\n";
		}
	}
?>