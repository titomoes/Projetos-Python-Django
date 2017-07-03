@extends('layout.principal')
@section('conteudo')
	@if(empty($candidatos))
		<div>Você não tem nenhum produto cadastrado.</div>
	@else
		<h1>Listagem de Candidatos</h1>
		<table class="table table-striped table-bordered table-hover" >
			 @foreach ($candidatos as $c)
			  <tr>
			 	<td> {{$c->nome}} </td>
				<td> {{$c->sigla}} </td>
				<td>
		<!-- 		<a href="{{action('CandidatoController@remove')}}">
					 <span class="glyphicon glyphicon-search"></span>
					</a>
		 -->	
					<a href="/remove/<?= $c->id ?>">
					 <span class="glyphicon glyphicon-search"></span>
					</a>
		 	</td>
			   </tr>	
			 @endforeach 
		</table>
	@endif
	@if (old('nome'))
	<div class="alert alert-sucess">
	<strong>Sucesso!</strong> O {{old('nome')}} foi adicionado com sucesso!	
	</div>
	@endif
@stop