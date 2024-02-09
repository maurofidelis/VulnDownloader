import os
import requests
import xml.etree.ElementTree as ET
import logging

# Configuração de Logging
logging.basicConfig(filename='./logs/download_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Configuração de Proxy
proxies = {
    "http": "http://endereco_do_proxy:porta",
    "https": "http://endereco_do_proxy:porta",
}

# Configuração de proxy com autenticação
# proxies = {
#     "http": "http://usuario:senha@endereco_do_proxy:porta",
#     "https": "http://usuario:senha@endereco_do_proxy:porta",
# }

def download_file(url, folder_name):
    """Faz o download do arquivo da URL e salva na pasta especificada."""
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        local_filename = url.split('/')[-1]
        local_path = os.path.join(folder_name, local_filename)
        with requests.get(url, stream=True, proxies=proxies) as r:  # Adiciona suporte a proxy
            r.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        logging.info(f"Arquivo {local_filename} salvo em {folder_name}/")
    except Exception as e:
        logging.error(f"Erro ao baixar {url} para {folder_name}: {e}")

def main(xml_file):
    """Lê o arquivo XML e executa os downloads."""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for provider in root.findall('provider'):
            name = provider.get('name')
            enabled = provider.find('enabled').text
            source = provider.find('source').text.strip('"')  # Remove as aspas
            if enabled.lower() == 'yes':
                logging.info(f"Iniciando download para o provedor: {name}")
                download_file(source, name)
    except Exception as e:
        logging.error(f"Erro ao processar o arquivo XML {xml_file}: {e}")

if __name__ == "__main__":
    main("vulnerabilities-database.conf")
