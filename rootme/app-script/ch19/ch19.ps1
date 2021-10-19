$KeyFile = "AES.key" 
$key = Get-Content $KeyFile 
$SecurePassword = Get-Content .passwd.crypt | ConvertTo-SecureString -key $Key  

echo $SecurePassword
