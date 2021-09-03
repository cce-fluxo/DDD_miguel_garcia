# DDD_miguel_garcia

Link: https://dashboard.heroku.com/apps/ddd-miguel-garcia
***
## Índice

- [Modelo Entidade Relacionamento](#mer)
- [Rotas](#rotas)
- [Exemplos](#exemplos)

***
## MER

![MERDDD](https://user-images.githubusercontent.com/72623443/132075155-139c92b8-17a3-449b-9d68-4bbc37d66b53.jpeg)

### Médico
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|nome|string(20)|nullable(False)|Nome do médico|
|cpf|string(40)|nullable(False)|cpf do médico|
|crm|string(40)|nullable(False)|crm do médico|
|idade|Integer|nullable(False)|cpf do médico|
|email|string(40)|nullable(False) unique(True)|E-mail do médico|
|especialidade|string(40)|nullable(False) |especialidade|
|senha_hash|largebinary(128)|nullable(False)|Senha hashed do médico|
|avatar|string(100)|default(foto_base)|Foto de identificação do médico relacionada ao digital ocean|
|consulta|relationship|backref(médicos) lazy(True)|consulta do medico|


### Pacientes
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|nome|string(50)|nullable(False)|Nome do paciente|
|cpf|string(14)|nullable(False) unique(True)|cpf do médico|
|email|string(50)|nullable(False) unique(True)|E-mail do paciente|
|idade|Integer|nullable(False)|cpf do médico|
|senha_hash|string(100)|nullable(False)|Senha hashed do paciente|
|consulta|relationship|backref(paciente) lazy(True)|consulta do paciente|

### consulta
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|hora|string|nullable(False)|Horario da consulta|
|data|string|nullable(False)|data da consulta|
|médico|foreign_key||Médico  da consulta|
|paciente|foreign_key||Paciente da consulta|

***
## Rotas
|Endpoint|Metodo|Descrição|
|-----|-----|-----|
|/login|POST|Usuario qualquer envia email e senha para fazer login|
|/send_mail/reset|POST| caso tenha esquecido a senha, token enviado por email|
|/reset/<string:token>|PATCH|Usuario registrado envia nova senha|
|/medico/create|GET|visualização de todos os médicos|
|/medico/create|POST|cadastro de novo médico|
|/medico/details/<int:id>|GET|Medico logado pode ver suas informações|
|/medico/details/<int:id>|PUT|Medico logado pode alterar todas suas informações|
|/medico/details/<int:id>|PATCH|Medico logado pode alterar alguma de suas informações|
|/medico/details/<int:id>|DELETE|Medico logado pode deletar seu perfil|
|/paciente/create|GET|visualização de todos pacientes|
|/paciente/create|POST|cadastro de novo paciente|
|/paciente/details/<int:id>|GET|paciente logado pode ver suas informações|
|/paciente/details/<int:id>|PUT|paciente logado pode alterar todas suas informações|
|/paciente/details/<int:id>|PATCH|paciente logado pode alterar alguma de suas informações|
|/paciente/details/<int:id>|DELETE|paciente logado pode deletar seu perfil|
|/files/put_url/formato|GET|para pegar o caminho do digital ocean|

|/consulta|GET|para visualizar todas as consultas do sistema|
|/consulta|POST|Criar nova consulta com a data, hora, id do medico e do paciente|











***
## Exemplos

### POST /login
```
{
    "email": "rogerinho@gmail.com",
    "senha": "123"
}
```
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNzY3Mzk0MiwianRpIjoiYzczYjY0MzEtMjk4Ni00YTUxLWJhNDEtOGIwZjQwY2IxMGFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjI3NjczOTQyLCJleHAiOjE2Mjc2NzQ4NDJ9.GS16yvd8gkkWjdhV09DDMtz9Qedd0rcQwJmjC1yNLq4"
}
```
### /medico/create|POST
```