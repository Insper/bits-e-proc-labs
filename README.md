## Configurando infra lab

Python:

```bash
python3.8 -m venv env
. env/bin/activate
pip3 install -r requirements.txt
```

Sempre que for trabalhar no lab, lembre de ativar o ambiente virtual (se estiver usando o vscode, instale o plugin):

```bash
. env/bin/activate
```

Para os labs de hardware que precisa programar a fpga, precisa ser no linux e ter quartus instalado:

- Instalar Quartus 21 lite
- Configurar `.bashrc`: `export PATH=$PATH:/home/vann/intelFPGA_lite/21.1/quartus/bin/`

Sugestão: Usar a VM fornecida, M1 e M2 não funcionam.
