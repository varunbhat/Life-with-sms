<!DOCTYPE html>
<html>
	<head>
		<title>Donate Blood!!</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
		<script src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
		<script src="http://code.jquery.com/mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
	</head>
	<body>
		<div data-role="page">

			<div data-role="header" data-theme="b">
				<h1>Blood4Reva</h1>
			</div><!-- /header -->

			<div data-role="content">
				<form action="form.php" method="post">
					<div data-role="fieldcontain" class="ui-hide-label">
						
						<input type="text" name="regNo" id="regNo" value="" placeholder="USN Number"/>
					</div>
					<div data-role="fieldcontain" class="ui-hide-label">
						
						<input type="text" name="mob" id="mob" value="" placeholder="Mobile Number"/>
					</div>
					<div data-role="fieldcontain">
						<fieldset data-role="controlgroup">
							<legend>
						
							</legend>
							<input type="radio" name="radio-choice-1" id="radio-choice-1" value="male"  />
							<label for="radio-choice-1">Male</label>

							<input type="radio" name="radio-choice-1" id="radio-choice-2" value="female"  />
							<label for="radio-choice-2">female</label>
						</fieldset>
					</div>
					<div data-role="fieldcontain">
						<label for="select-choice-a" class="select">Your Blood Group</label>
						<select name="select-choice-a" id="select-choice-a" data-native-menu="false">
							<option>Blood Group</option>
							<option value="a">A</option>
							<option value="b">B</option>
							<option value="ab">AB</option>
							<option value="o">O</option>
							<option value="dunno">I Dont Know!</option>
						</select>
						<select name="select-choice-b" id="select-choice-b" data-native-menu="false">
							<option>Rhesus Factor:</option>
							<option value="p">Positive</option>
							<option value="n">Negative</option>
							<option value="dunno">Dunno!</option>
						</select>
					</div>
					<div data-role="fieldcontain">
						<label for="slider">Weight:</label>
						<input type="range" name="slider" id="slider" value="50" min="0" max="100" data-highlight="true"  />
					</div>
					<button type="submit" data-theme="b" name="submit" value="submit-value">Submit</button>
				</form>

			</div><!-- /content -->

		</div><!-- /page -->

	</body>
</html>
