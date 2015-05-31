<html>
<body>

<p>
Showing data for the zip code: <b><?php echo $_POST["zip"]; ?></b><br>
</p>

<form action="service.php" method="POST">

<table>
<col width="200">
<col width="200">
<tr><td>
Population:</td>
<td>
<input type="text" name="population" value="<?php echo $var[''];?>">
</td></tr>

<tr><td>
Schools:</td><td>
<input type="text" name="schools" >
</td></tr>

<tr><td>Parks:</td><td>
<input type="text" name="parks">
</td></tr>

<tr><td>Landmarks:</td><td>
<input type="text" name="landmarks">
</td></tr>

<tr><td>Libraries: </td><td>
<input type="text" name="libraries">
</td></tr>

<tr><td>High Schools: </td><td>
<input type="text" name="high_schools">
</td></tr>

<tr><td>Traffic Cameras: </td><td>
<input type="text" name="cameras">
</td></tr>

<tr><td>Picnic Sites: </td><td>
<input type="text" name="picnic">
</td></tr>

<tr><td>Childrens Play Areas: </td><td>
<input type="text" name="play_areas">
</td></tr>

<tr><td>Hospitals:</td><td>
<input type="text" name="hospitals">
</td></tr>
</table>
<h3>Please List the counts of business organizations below:</h3>

<table>
<col width="200">
<col width="200">
<tr><td>Corporation:</td><td>
<input type="text" name="corp">
</td></tr>

<tr><td>LLC*Limited Liability Co:</td><td>
<input type="text" name="liability">
</td></tr>

<tr><td>Sole Proprietor:</td><td>
<input type="text" name="sole">
</td></tr>

<tr><td>Partnership:</td><td>
<input type="text" name="partner">
</td></tr>

<tr><td>LLP Limited Liability Partners:</td><td>
<input type="text" name="llp">
</td></tr>

<tr><td>PLLC Prof Limited Liability Co:</td><td>
<input type="text" name="pllc">
</td></tr>

<tr><td>Municipal:</td><td>
<input type="text" name="municipal">
</td></tr>

<tr><td>Partnership/Nonprofit:</td><td>
<input type="text" name=nonprofit">
</td></tr>

<tr><td>Others:</td><td>
<input type="text" name="other">
</td></tr>

<tr><td></td>
<td>
<input type="submit" value="Submit">
</td></tr>
</table>

</form>

</body>
</html>
