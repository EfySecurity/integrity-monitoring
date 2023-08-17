<div align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="python-logo-generic.svg">
</div>

# Monitoramento de Integridade de Arquivos

Este é um projeto simples em Python para monitorar a integridade de arquivos em um diretório específico. O projeto verifica regularmente se houve alterações nos arquivos e notifica por e-mail e mensagem de texto (SMS) quando são detectadas alterações. Além disso, o projeto cria um relatório em HTML das alterações ocorridas.

## Funcionalidades

- Monitoramento contínuo da integridade dos arquivos em um diretório.
- Notificações de alteração por e-mail usando o Gmail.
- Notificações de alteração por mensagem de texto (SMS) usando o Twilio.
- Criação de relatório em HTML das alterações detectadas.
- Armazenamento de informações sobre alterações em um log.
- Limitação do tamanho do log para evitar crescimento excessivo.

## Configuração

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/EfySecurity/integrity-monitoring.git
```

```bash
cd integrity-monitoring
```

2. Instale as dependências necessárias usando o pip:

```bash
pip install smtplib twilio
```

`Lembre-se de ajustar as configurações de e-mail, Twilio, diretório monitorado e outras variáveis conforme necessário. Este exemplo é uma versão mais completa que incorpora notificações por e-mail e SMS, criação de relatórios em HTML e monitoramento contínuo da integridade dos arquivos em um diretório específico. Certifique-se de ter as bibliotecas smtplib, twilio e suas dependências instaladas.`

`Lembre-se de substituir as variáveis, como yourusername e os detalhes de configuração do Gmail e do Twilio, pelas suas informações reais.`

3. Configure as variáveis no início do arquivo `monitor.py`:

- `EMAIL_FROM`: Seu endereço de e-mail do Gmail.
- `EMAIL_PASSWORD`: A senha do seu e-mail do Gmail.
- `EMAIL_TO`: O endereço de e-mail para onde os alertas serão enviados.
- `TWILIO_SID`: SID da sua conta Twilio.
- `TWILIO_AUTH_TOKEN`: Token de autenticação da sua conta Twilio.
- `TWILIO_PHONE_NUMBER`: Seu número Twilio.
- `DESTINATION_PHONE_NUMBER`: O número de telefone para receber mensagens de texto.
- `LOG_FILE`: Nome do arquivo de log para registrar as alterações.
- `MAX_LOG_ENTRIES`: Número máximo de entradas no log.

4. Execute o programa:

```bash
python monitor.py
```

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver melhorias a sugerir, fique à vontade para criar um Pull Request.

## Autor

Nome: Efy Security

Email: efy.security@proton.me

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).






