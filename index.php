<html>
<head>
<title>run my python files</title>
<?PHP
    echo shell_exec("python yelp.py 'inputRange' 'inputLocation' 'Sushi' 'Italian' 'Chinese' 'Thai' 'Indian' 'Mexican' 'Koren' 'Ethiopian' 'Caribbean' 'Bars' 'Beer, Wine, & Spirits' 'Gastropubs' 'Whiskey Bars'");
?>
</head>