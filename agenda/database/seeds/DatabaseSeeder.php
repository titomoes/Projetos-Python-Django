<?php

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
class DatabaseSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
    	$this->call('CandidatoTableSeeder');
    }
    
}

class CandidatoTableSeeder extends Seeder{
	public function run()
	{
        DB::insert('insert into candidatos
			(nome, sigla)
			values (?,?)',
 			array('Claudio', 'PL'));
        DB::insert('insert into candidatos
			(nome, sigla)
			values (?,?)',
 			array('Fernanda', 'PSOL'));
    }
}