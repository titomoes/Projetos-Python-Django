@extends('layout.principal')
@section('conteudo')
<h1>Novo  Candidato</h1>
<form action="/adiciona" method="post">
<input type="hidden" name="_token" value="{{{csrf_token()}}}"/> 
  <div class="form-group">
    <label>Nome</label>
    <input name="nome" class="form-control" value="{{ old('nome') }}" />
  </div>
  <div class="form-group">
    <label>Sigla</label>
    <select name="sigla">
    @for  
 		<option value="PL">PL</option>
 		<option value="PPL">PPL</option>
 		<option value="ZL">ZL</option>
 		<option value="ZN">ZN</option>
	</select>
  </div>
  <button type="submit" class="btn btn-primary btn-block">Adicionar</button>
</form>
 @stop