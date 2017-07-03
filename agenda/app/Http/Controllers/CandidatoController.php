<?php

namespace App\Http\Controllers;
use App\Candidato;
use Illuminate\Support\Facades\DB;
use Request;


class CandidatoController extends Controller{

	public function lista(){
		//cria um array com todos os valores de produtos
		$candidatos=Candidato::all();
		
		return view('candidato/listagem')->with('candidatos',$candidatos);
	}
	public function novo(){
		//chama a tela formulario
		return view('candidato.formulario');
	}
	public function adiciona(){
		//pega os valores do formulario
		$nome=Request::input('nome');
		$sigla=Request::input('sigla');
		//persiste no banco (query builder)
		DB::table('candidatos')->insert(
			['nome'=>$nome,
			'sigla'=>$sigla]
			);
		//retorna a view
		//view('candidato/adicionado')->with('nome',$nome)
		//recupereando valores da requisiçao anterior
		return redirect()
			->action('CandidatoController@lista')
			->withInput(Request::only('nome'));

	}
	 public function remove($id){
		$candidato= Candidato::find($id);
		$candidato->delete();
		return view('candidato/listagem')->with('candidatos',$candidatos);
		//return redirect()->action('CandidatoController@lista');
	}
	// public function deleta($id){
	// 	$candidato=Candidato::find($id);
	// 	//DB::table('candidatos')
	// 	return redirect()
	// 	->action('CandidatoController@lista');

	// }
	}	