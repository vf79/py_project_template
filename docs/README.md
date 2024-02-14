# Python Project Template #

## Sobre ##
Modelo de estrutura para projetos em python

## Tabela de Conteúdos ##
* [Sobre](#sobre)
* [Tabela de conteúdos](#tabela-de-conteúdos)
* [Status do projeto](#status-do-projeto)
* [Recursos](#recursos)
* [Pré-requisitos](#pré-requisitos)
* [Dependências](#dependências)
* [Tecnologias](#tecnologias)
* [Testes](#testes)
* [Desenvolvimento](#desenvolvimento)
* [Deploy](#deploy)
* [API](#api)
* [Código de Conduta](#código-de-conduta)
* [Contribuindo](#contribuindo)
* [Autor](#autor)
* [Licença](#licença)

## Status do projeto ##
Em desenvolvimento

### Recursos ###
- [X] Aplicação base
- [ ] Logging
- [ ] Todo

### Pré-requisitos ###
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://python.org).  
Para o python utilizo o pacote [Winpython](https://winpython.github.io/).  
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

### Dependências ###

#### Utilizando Powershell ####
Acessar o diretório da aplicação
```powershell
cd <Nome do projeto/aplicação>
```
Instalar o Ambiente virtual python VirtualEnv
```powershell
python -m venv .venv --upgrade-deps
```
Habilitar o ambiente virtual python
```powershell
.venv\Script\activate
```
Instalar as dependências do projeto:
```powershell
.\run.cmd --install
```
Instalar as dependências de desenvolvimento do projeto:
```powershell
.\run.cmd --install-dev
```
Instalar as dependências de documentação do projeto:
```powershell
.\run.cmd --install-doc
```
Instalar as dependências de qualidade do código:
```powershell
.\run.cmd --install-lint
```
Instalar as dependências de testes do projeto:
```powershell
.\run.cmd --install-test
```

#### Gerar Secret Key ####
Para gerar o secret key da aplicação usando python execute:
```python
import secrets
secrets.token_urlsafe(32)
```
Inserir a chave gerada no arquivo .secrets.toml

#### Extras #####
Se o powershell não estiver permissão de execução,
Para ver as permissões execute:
```powershell
Get-ExecutionPolicy -List
```
Para alterar as permissões execute o powershell no modo administrador e execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

### Tecnologias ###
[Dynaconf](https://www.dynaconf.com/), [Python](https://python.org)

### Testes ###
Para realizar testes, alterar a constante env do arquivo settings.toml para "testing"

#### Utilizando Powershell ####
Para realizar todos os testes:
```powershell
.\run.cmd --test
```
Para realizar apenas alguns testes.
Adicionar no arquivo de teste o decorator @pytest.mark.run e executar o comando:
```powershell
.\run.cmd --test-run
```
Para realizar testes com debug.
Adicionar ao codigo no ponto de checagem:
```python
import ipdb
ipdb.set_trace()
```
Executar o comando:

```powershell
.\run.cmd --test-debug
```
Para ver o relatório de testes em html:  
Abrir no navegador o arquivo index.html da pasta htmlcov.

### Desenvolvimento ###
Para rodar o programa:
```powershell
engage
```

### Deploy ###

## Código de Conduta ##
[Código de Conduta](./code_of_conduct.md)

## Contribuindo ##
[Contribuindo](./contributing.md)

## Autor ##
[Valmir França](https://vf79.com.br)

## Licença ##
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE.txt)
