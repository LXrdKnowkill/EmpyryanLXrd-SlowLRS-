# EmpyryanLXrd-SlowLRS- é um simples DOS em Python 

## Oq é isso? SlowLRS/SlowLoris?
SlowLRS é basicamente um HTTP de negação de serivço  que afeta servidores em varias escalas. ele tem uma funcionalidade desse jeito:


<li>
  <b> 1): </b> Ele começa a fazer muitas requisição HTTP
</li>
<li>
<b> 2): </b> Ele fara enviamentos de Headers periodicamente (ele tem um tempo ali de 15 a 20s ) para que as conexões continuem abertas.
</li>
<li>
<b> 3): </b> Ele não parana de fazer conecção ate que o servidor corte sua conecção, assim se quiser atacar novamente iremos continuar a fazer a mesma coisa
</li>

<br>
Isso acaba deixando a pool de threads dos servidores esgotadas e os servidores não podendo responder as outras pessoas.
<br>
<br>

###Aviso: 

Se você achou este trabalho de uma maneira que te ajude, por favor, me ajude citando como 

```bibtex
@article{EmpyryanLXrd-SlowLRS,
  title = "EmpyryanLXrd-SlowLRSs",
  author = "MazumiYuki/LXrdKnowkill",
  journal = "github.com",
  year = "2022",
  url = "https://github.com/LXrdKnowkill/EmpyryanLXrd-SlowLRS"
}
```

## Como instalar e rodar o bonitinho 

Você pode clonar o repositório git ou instalar usando (pip)em seu linux. abaixo mostra como voce pode executar ele.

* `sudo pip3 install slowloris`
* `slowloris example.com`

Isso aqui é tudinho o que voce  precisa para instalar e executar o slowloris.py.

Se você quiser clonar usando git em vez de pip, voce pode fazer assim.

* `git clone https://github.com/LXrdKnowkill/EmpyryanLXrd-SlowLRS-.git`
* `cd slowLRS`
* `python3 slowLRS.py example.com`

### SOCKS5 Proxy Suporte 

Contudo, se tu planjea usar a opção `-x` acaba que para usar essa opção tu precisa usar uma proxy SOCKS5 para conexão em vez de uma conexão direta pelo seu endereço IP, você precisará instalar a biblioteca `PySocks`(ou qualquer outra implementação da biblioteca `socks`) tambem. [`PySocks`](https://github.com/Anorov/PySocks) é um fork de [`SocksiPy`](http://socksipy.sourceforge.net/) feito pelo usuário do GitHub @Anorov e pode ser facilmente instalado e adicionando `PySocks` ao comando `pip` acima ou executando-o novamente assim:

* `sudo pip3 install PySocks`

Você pode usar a opção `-x` para ativar o suporte SOCKS5 e a opção `--proxy-host` e `--proxy-port` para especificar o host proxy SOCKS5 e sua porta, se forem diferentes do padrão ` 127.0.0.1:8080`.

## Opções de configuração
É possível modificar o comportamento do slowloris com linha de comando
argumentos. Se tu precisar de um comando de ajuda que seja atualizado ao projeto, digite o comando:
`slowloris -h`.
## Outras funções de confuraçção 
* -p, --port
* * Porta do servidor, geralmente é 80
* -s, --sockets
* * Numero de sockets para ser usados no teste 
* -v, --verbose
* * Aumenta a taxa de loggins no site
* -ua, --randuseragents
* * Randomiza os loggins de usuário com cada solicitação
* -x, --useproxy
* * Use o proxy SOCKS5 para conectar
* --https
* * Use a HTTP para fazer os ataques
* --sleeptime
* * Tempo de envio a cada requisição enviada ( tempo para ele parar de enviar)

## License
O código é licenciado sob a Licença MIT.
