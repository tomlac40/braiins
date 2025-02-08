import json
import httpx
import voluptuous as vol
import datetime
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.event import async_track_time_interval
import homeassistant.helpers.config_validation as cv
import time
import logging

CONF_API_KEY = "api_key"

DEFAULT_NAME_POOL = "Braiins Pool"
DEFAULT_NAME_ACCOUNT = "Braiins Account"
SCAN_INTERVAL_POOL = datetime.timedelta(minutes=2)
SCAN_INTERVAL_ACCOUNT = datetime.timedelta(minutes=4)

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
})

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    api_key = config[CONF_API_KEY]
    sensorPool = BraiinsPoolSensor(DEFAULT_NAME_POOL, api_key)
    sensorAccount = BraiinsAccountSensor(DEFAULT_NAME_ACCOUNT, api_key)

    async_add_entities([sensorPool, sensorAccount])

    async_track_time_interval(hass, sensorPool.async_update, SCAN_INTERVAL_POOL)
    async_track_time_interval(hass, sensorAccount.async_update, SCAN_INTERVAL_ACCOUNT)


class BraiinsPoolSensor(Entity):
    def __init__(self, name, api_key):
        self._name = name
        self._state = None
        self._api_key = api_key
        self._attributes = {}

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes
        
    async def async_update(self):
        # Pool stats
        url = "https://pool.braiins.com/stats/json/btc/"
        headers = {
            "Pool-Auth-Token": self._api_key
        }
        response = httpx.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            self._attributes["hash_rate_unit"] = data["btc"]["hash_rate_unit"]
            self._attributes["pool_active_workers"] = data["btc"]["pool_active_workers"]
            self._attributes["pool_5m_hash_rate"] = data["btc"]["pool_5m_hash_rate"]
            self._attributes["pool_60m_hash_rate"] = data["btc"]["pool_60m_hash_rate"]
            self._attributes["pool_24h_hash_rate"] = data["btc"]["pool_24h_hash_rate"]
            self._attributes["update_ts"] = data["btc"]["update_ts"]
            #self._attributes["blocks"] = data["btc"]["blocks"]
            self._attributes["fpps_rate"] = data["btc"]["fpps_rate"]
        else:
            _LOGGER.error("Error during Pool stat request: %s", response.status_code)

class BraiinsAccountSensor(Entity):
    def __init__(self, name, api_key):
        self._name = name
        self._state = None
        self._api_key = api_key
        self._attributes = {}

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes
        
    async def async_update(self):
        # Account stats    
        url = "https://pool.braiins.com/accounts/profile/json/btc/"
        headers = {
            "Pool-Auth-Token": self._api_key
        }
 
        response = httpx.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
#            _LOGGER.error("data =  %s",str(data))
            self._attributes["username"] = data["username"]
            self._attributes["all_time_reward"] = data["btc"]["all_time_reward"]
            self._attributes["hash_rate_unit"] = data["btc"]["hash_rate_unit"]
            self._attributes["hash_rate_5m"] = data["btc"]["hash_rate_5m"]
            self._attributes["hash_rate_60m"] = data["btc"]["hash_rate_60m"]
            self._attributes["hash_rate_24h"] = data["btc"]["hash_rate_24h"]
            self._attributes["hash_rate_yesterday"] = data["btc"]["hash_rate_yesterday"]
            self._attributes["low_workers"] = data["btc"]["low_workers"]
            self._attributes["off_workers"] = data["btc"]["off_workers"]
            self._attributes["ok_workers"] = data["btc"]["ok_workers"]
            self._attributes["dis_workers"] = data["btc"]["dis_workers"]
            self._attributes["current_balance"] = data["btc"]["current_balance"]
            self._attributes["today_reward"] = data["btc"]["today_reward"]
            self._attributes["estimated_reward"] = data["btc"]["estimated_reward"]
            self._attributes["shares_5m"] = data["btc"]["shares_5m"]
            self._attributes["shares_60m"] = data["btc"]["shares_60m"]
            self._attributes["shares_24h"] = data["btc"]["shares_24h"]
            self._attributes["shares_yesterday"] = data["btc"]["shares_yesterday"]
        else:
            _LOGGER.error("Error during Account stat request: %s", response.status_code)
            


class BraiinsDailyRewardSensor(Entity):
    def __init__(self, name, api_key):
        self._name = name
        self._state = None
        self._api_key = api_key
        self._attributes = {}

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    def update(self):
        # Daily Reward API stats     
        url = "https://pool.braiins.com/accounts/rewards/json/btc"
        headers = {
            "Pool-Auth-Token": self._api_key
        }    
            
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
#            _LOGGER.error("data =  %s",str(data))
            self._attributes["daily_rewards_date"] = data["btc"]["daily_rewards"][0]["date"]
#            self._attributes["daily_rewards_total_reward"] = data["btc"]["daily_rewards"]["total_reward"]
#            self._attributes["daily_rewards_mining_reward"] = data["btc"]["daily_rewards"]["mining_reward"]
#            self._attributes["daily_rewards_bos_plus_reward"] = data["btc"]["daily_rewards"]["bos_plus_reward"]
#            self._attributes["daily_rewards_referral_bonus"] = data["btc"]["daily_rewards"]["referral_bonus"]
#            self._attributes["daily_rewards_referral_reward"] = data["btc"]["daily_rewards"]["referral_reward"]
#            self._attributes["daily_rewards_calculation_date"] = data["btc"]["daily_rewards"]["calculation_date"]
        else:
            _LOGGER.error("Error during Daily Reward API stat request: %s", response.status_code) 
