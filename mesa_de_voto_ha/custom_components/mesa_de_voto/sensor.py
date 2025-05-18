import logging
import voluptuous as vol
from datetime import timedelta
from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv
import requests
from bs4 import BeautifulSoup

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(hours=12)

CONF_CC = "cartao_cidadao"
CONF_NASC = "data_nascimento"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_CC): cv.string,
    vol.Required(CONF_NASC): cv.string,
    vol.Optional(CONF_NAME, default="Mesa de Voto"): cv.string
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    cc = config[CONF_CC]
    nasc = config[CONF_NASC]
    name = config[CONF_NAME]

    add_entities([MesaDeVotoSensor(name, cc, nasc)], True)

class MesaDeVotoSensor(SensorEntity):
    def __init__(self, name, cc, nasc):
        self._name = name
        self._cc = cc
        self._nasc = nasc
        self._state = None
        self._attrs = {}

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attrs

    def update(self):
        try:
            resp = requests.post(
                "https://www.recenseamento.mai.gov.pt/",
                data={
                    "numCC": self._cc,
                    "dataNascimento": self._nasc,
                },
                timeout=10
            )
            soup = BeautifulSoup(resp.text, "html.parser")
            info = soup.find_all("p")
            dados = [x.get_text(strip=True) for x in info]
            self._state = "Disponível"
            self._attrs = {
                "resultado": dados
            }
        except Exception as e:
            _LOGGER.error("Erro ao consultar mesa de voto: %s", e)
            self._state = "Erro"