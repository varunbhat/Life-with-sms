<html>
	<head>
		<title> Hello! </title>
		<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
		<meta name='txtweb-appkey' content='415224ee-da8f-46ba-a962-ed24760371af' />
	</head>
	<body>
		<form action='http://geektronics.tk/cgi-bin/first.py' method='post' name='frm'>
		<?php
		foreach ($_GET as $key => $value) {
		//	echo "<input type='hidden' name='".$key."' value='".$value."'>";
		echo $key. "<br>" . $value."<br><br>";
		}
		?>
		<form>
	</body>
</html>