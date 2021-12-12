<html>
    
<head>
<title></title><!--'Sushi' 'Italian' 'Chinese' 'Thai' 'Indian' 'Mexican' 'Koren' 'Ethiopian' 'Caribbean' 'Bars' 'Beer, Wine, & Spirits' 'Gastropubs' 'Whiskey Bars'-->
<?PHP
    if(isset($_POST['spin_btn'])){
        echo shell_exec("python yelp.py 'inputLocation' 'inputRange'");
        //header('...Website\index.html:index.html?status=success');//redirect to your html with status
    }
    $cate =array("Sushi", "Italian", "Chinese", "Thai", "Indian", "Mexican", "Koren", "Ethiopian", "Caribbean", "Bars", "Beer, Wine, & Spirits" "Gastropubs", "Whiskey Bars");
?>

</head>


</html>