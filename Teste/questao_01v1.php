<!DOCTYPE html>
<html>
<body>

<?php	
  	$teste=[
  				["ID"=>"segunda","ENTRADA"=>40  ,"SAIDA"=>20],
  				["ID"=>"Terça"  ,"ENTRADA"=>50  ,"SAIDA"=>33],
  				["ID"=>"Quarta" ,"ENTRADA"=>20  ,"SAIDA"=>21],
  				["ID"=>"Quinta" ,"ENTRADA"=>100 ,"SAIDA"=>90],
  				["ID"=>"Sexta"  ,"ENTRADA"=>23  ,"SAIDA"=>13],
  				["ID"=>"Sabado" ,"ENTRADA"=>90  ,"SAIDA"=>65],
  				["ID"=>"Domingo","ENTRADA"=>1230,"SAIDA"=>982]
  			];
  	$arrlength = count($teste);
  	for ($i=0,$i < $arrlength; $i++)
  	{
    	for ($x=0; $x < $arrlength ; $x++) 
    	{ 
			echo $teste[0][0];
			echo "<br>";	       	
       	}	
    }
?>
</body>
</html>
