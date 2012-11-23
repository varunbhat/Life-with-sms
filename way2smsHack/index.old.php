<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<title>My SMS</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" type="text/css" href="message-css/demo.css" />
		<link rel="stylesheet" type="text/css" href="message-css/style2.css" />
		<script type="text/javascript" src="message-js/modernizr.custom.04022.js"></script>
		<!--[if lt IE 8]>
		<style>
		.af-wrapper{display:none;}
		.ie-note{display:block;}
		</style>
		<![endif]-->
	</head>
	<body>
		<div class="container">
			<header>
				<span>Send Message</span>
				<p>
					Do your stuff
				</p>
				<p class="ie-note">
					D'oh!
				</p>
			</header>

			<section class="af-wrapper">
				<h3>Message</h3>

				<!--	<input id="af-showreq" class="af-show-input" type="checkbox" name="showreq" />
				<label for="af-showreq" class="af-show">Show only required fields</label>-->

				<?php
				$correct = $_POST['simplePass'];
				$password = "hello";
				?>

				<?php
				if ($correct == $password) {
					echo '
				<form action="http://geektronics.tk/cgi-bin/smsv2.py" class="af-form" id="af-form" method="post">

					<div class="af-outer af-required">
						<div class="af-inner">
							<label for="input-name">Name/Number</label>
							<input type="text" name="to" id="input-name" required>
						</div>
					</div>

					<div class="af-outer-field af-required" style="width=300px">
						<div class="af-inner">
							<label for="input-email">Text to send</label>
							<textarea name="text" id="input-email" style="width: 400px;height: 200px" required></textarea>
						</div>
					</div>
					<input type="submit" value="Send it over!" />

				</form>';
				} else {
					echo '
				<form action="http://geektronics.tk/sms/index.php" class="af-form" id="af-form" method="post">

					<div class="af-outer af-required">
						<div class="af-inner">
							<label for="input-name">Password</label>
							<input type="password" name="simplePass" id="input-name" required>
						</div>
					</div>
				</form>';
				}
				?>
			</section>
		</div>
	</body>
</html>
