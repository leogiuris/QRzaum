# QRzaum
URL: http://leogiuris.pythonanywhere.com/
### Trabalho 1 da matéria Programação para a Web
Aluno: Leonardo Giuri Santiago (1520893)

Este site consiste em um portal para criar e administrar QR codes para fins diversos, desde o uso pessoal ao comercial. 

Cada usuário é capaz de:
- criar um ou mais QR codes (e declarar se é público ou não)
- editar seus QR codes
- remover seus QR codes
- acessar QR codes de outros usuários (apenas os que forem públicos)

Para criar um QR code é necessário fazer um cadastro no site. O cadastro pede um username, email e uma senha (que pode ser bem simples).

O usuário pode navegar pelo site usando a <i>navbar</i> que contem os links para a Homepage, Lista de QR codes públicos (<i>All Codes</i>) e área restrita do usuário (<i>Meus QRs</i>).

Em <i>All Codes</i> o usuário tem acesso a uma lista com todos os QR codes públicos criados no site, podendo ver o URL para onde redirecionam e quantas vezes o QR foi escaneado e acessado.

Em <i>Meus QRs</i> é o espaço do usuário. Lá ele pode criar, editar e apagar seus QR codes.

Para criar o QR code é necessário dar um nome/título e a URL para onde será redirecionado. O formulário marca a opção de ser público por default, podendo ser desmarcada caso o usuário queira que o QR code seja privado.

Para editar é o mesmo formulário que na criação, podendo alterar o nome, URL e privacidade do QR code.

Para remover é simples, basta selecionar o botão de Apagar e confirmar no modal que aparece em seguida.

### O que funciona:
 - criação, edição e remoção dos QR codes
 - leitura dos QR codes e redirecionamento para as URLs corretas
 - registro de usuário
 - login e logout de usuário
 - área restrita para usuário autenticado

 ### O que não funciona
 - troca e recuperação de senha
 - remoção de cadastro
 - pesquisa e filtragem por usuário ou título de QR code
