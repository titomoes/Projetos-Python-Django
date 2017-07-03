<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', 'CandidatoController@lista' );{

}
//get padrao.
Route::get('/novo', 'CandidatoController@novo' );{}

// /Route::get('/edita/{id}','CandidatoController@update');{}
//para fazer o metodo post funcionar 
Route::match(array('GET','POST'),'/adiciona','CandidatoController@adiciona' );{}

Route::get('/remove/', 'CandidatoController@remove')->where('id','[0-9]+');{}