<html>
    
<head>
<title></title><!--'Sushi' 'Italian' 'Chinese' 'Thai' 'Indian' 'Mexican' 'Koren' 'Ethiopian' 'Caribbean' 'Bars' 'Beer, Wine, & Spirits' 'Gastropubs' 'Whiskey Bars'-->

<?PHP
    if(isset($_POST['spin_btn'])){
        echo shell_exec("python3  yelp.py 'inputL' 'inputR'");
        //header('...Website\index.html:index.html?status=success');//redirect to your html with status
    }
    //$cate =array("Sushi", "Italian", "Chinese", "Thai", "Indian", "Mexican", "Koren", "Ethiopian", "Caribbean", "Bars", "Beer, Wine, & Spirits" "Gastropubs", "Whiskey Bars");
    //E:\RestaurantRoulette\Website\yelp.py
?>

</head>


</html>