# braiins
Home assistant component for Braiins pool mining

## Installation

### Manual

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `braiins`.
1. Download _all_ the files from the `custom_components/braiins/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Add wanted currency to `configuration.yaml`
   ```
   sensor:   
     - platform: braiins
       api_key: "YoUrApiKey"  from Braiins pool website
   ```
1. Restart Home Assistant
1. Sensors created:
   ```
   sensor.braiins_pool
   sensor.braiins_account
   sensor.braiins_api
   ```   
1. Specific sensors could be created :
   ```
    braiins_pool_hash_rate_unit:
      friendly_name: unit used for the hash rate values
      unit_of_measurement: 'Gh/s'
      value_template: "{{ state_attr('sensor.braiins_pool', 'pool_hash_rate_unit') }}"

    braiins_pool_pool_active_workers:
      friendly_name: active workers
      value_template: "{{ state_attr('sensor.braiins_pool', 'pool_active_workers') }}"
    braiins_pool_pool_5m_hash_rate:
      friendly_name: pool hash rate for the last 5 minutes
      unit_of_measurement: 'Gh/s'
      value_template: "{{ state_attr('sensor.braiins_pool', 'pool_5m_hash_rate') }}"
    braiins_pool_pool_60m_hash_rate:
      friendly_name: pool hash rate for the last 60 minutes
      unit_of_measurement: 'Gh/s'
      value_template: "{{ state_attr('sensor.braiins_pool', 'pool_60m_hash_rate') }}"
    braiins_pool_pool_24h_hash_rate:
      friendly_name: pool hash rate for the last 24 hours
      unit_of_measurement: 'Gh/s'
      value_template: "{{ state_attr('sensor.braiins_pool', 'pool_24h_hash_rate') }}"
    #braiins_pool_update_ts:
    #  friendly_name: timestamp when the stats were updated
    #  value_template: "{{ state_attr('sensor.braiins_pool', 'update_ts') }}"
    #braiins_pool_blocks:
    #  friendly_name: information for the last 15 blocks (breakdown below)
    #  value_template: "{{ state_attr('sensor.braiins_pool', 'blocks') }}"
    braiins_pool_fpps_rate:
      friendly_name: pay par share rate 
      unit_of_measurement: 'Gh/s'
      value_template: "{{ state_attr('sensor.braiins_pool', 'fpps_rate') }}"

    braiins_username:
      friendly_name: username
      value_template: "{{ state_attr('sensor.braiins_account', 'username') }}"
    braiins_user_all_time_reward:
      friendly_name: cumulative all-time reward
      unit_of_measurement: 'Gh/s'
      value_template: "{{ state_attr('sensor.braiins_account', 'all_time_reward') }}"
    braiins_user_hash_rate_unit:
      friendly_name: unit used for the hash rate values
      value_template: "{{ state_attr('sensor.braiins_account', 'hash_rate_unit') }}"
    braiins_user_hash_rate_5m:
      friendly_name: average hash rate for the last 5 minutes
      unit_of_measurement: 'Gh/s'
      value_template: "{{ state_attr('sensor.braiins_account', 'hash_rate_5m') }}"
    braiins_user_hash_rate_60m:
      friendly_name: average hash rate for the last 60 minutes
      unit_of_measurement: 'Gh/s'
      value_template: "{{ state_attr('sensor.braiins_account', 'hash_rate_60m') }}"
    braiins_user_hash_rate_24h:
      friendly_name: average hash rate for the last 24 hours
      unit_of_measurement: 'Gh/s'
      value_template: "{{ state_attr('sensor.braiins_account', 'hash_rate_24h') }}"
    braiins_user_hash_rate_yesterday:
      friendly_name: average hash rate for the previous UTC day
      unit_of_measurement: 'Gh/s'
      value_template: "{{ state_attr('sensor.braiins_account', 'hash_rate_yesterday') }}"
    braiins_user_low_workers:
      friendly_name: number of workers with low state
      value_template: "{{ state_attr('sensor.braiins_account', 'low_workers') }}"
    braiins_user_off_workers:
      friendly_name: number of workers with off state
      value_template: "{{ state_attr('sensor.braiins_account', 'off_workers') }}"
    braiins_user_ok_workers:
      friendly_name: number of workers with ok state
      value_template: "{{ state_attr('sensor.braiins_account', 'ok_workers') }}"
    braiins_user_dis_workers:
      friendly_name: number of workers with disabled monitoring
      value_template: "{{ state_attr('sensor.braiins_account', 'dis_workers') }}"
    braiins_user_current_balance:
      friendly_name: current reward balance
      unit_of_measurement: ''
      value_template: "{{ state_attr('sensor.braiins_account', 'current_balance') }}"
    braiins_user_today_reward:
      friendly_name: confirmed reward for this day
      unit_of_measurement: ''
      value_template: "{{ state_attr('sensor.braiins_account', 'today_reward') }}"
    braiins_user_estimated_reward:
      friendly_name: estimated reward for the current block
      unit_of_measurement: ''
      value_template: "{{ state_attr('sensor.braiins_account', 'estimated_reward') }}"
    braiins_user_shares_5m:
      friendly_name: active shares for last 5 minutes
      unit_of_measurement: 'shares'
      value_template: "{{ state_attr('sensor.braiins_account', 'shares_5m') }}"
    braiins_user_shares_60m:
      friendly_name: active shares for last hour
      unit_of_measurement: 'shares'
      value_template: "{{ state_attr('sensor.braiins_account', 'shares_60m') }}"
    braiins_user_shares_24h:
      friendly_name: active shares for last day
      unit_of_measurement: 'shares'
      value_template: "{{ state_attr('sensor.braiins_account', 'shares_24h') }}"
    braiins_user_shares_yesterday:
      friendly_name: active shares for yesterday
      unit_of_measurement: 'shares'
      value_template: "{{ state_attr('sensor.braiins_account', 'shares_yesterday') }}"

    braiins_daily_rewards_date_0:
      friendly_name: Unix time (the first second of the date)
      unit_of_measurement: ''
      value_template: "{{ state_attr('sensor.braiins_api', 'rewards_date_0') }}"
    braiins_daily_rewards_total_reward_0:
      friendly_name: the sum of all reward types for the day
      unit_of_measurement: ''
      value_template: "{{ state_attr('sensor.braiins_api', 'rewards_total_reward_0') }}"
    braiins_daily_rewards_mining_reward_0:
      friendly_name: the standard mining reward
      unit_of_measurement: ''
      value_template: "{{ state_attr('sensor.braiins_api', 'rewards_mining_reward_0') }}"
    braiins_daily_rewards_bos_plus_reward_0:
      friendly_name: the amount refunded (pool fee refund) for mining with Braiins OS
      unit_of_measurement: ''
      value_template: "{{ state_attr('sensor.braiins_api', 'rewards_bos_plus_reward_0') }}"
    braiins_daily_rewards_referral_bonus_0:
      friendly_name: bonus received by being referred to Braiins OS
      unit_of_measurement: ''
      value_template: "{{ state_attr('sensor.braiins_api', 'rewards_referral_bonus_0') }}"
    braiins_daily_rewards_referral_reward_0:
      friendly_name: reward earned for HR referred to Braiins OS
      unit_of_measurement: ''
      value_template: "{{ state_attr('sensor.braiins_api', 'referral_reward_0') }}"
    braiins_daily_rewards_calculation_date_0:
      friendly_name: calculation date timestamp
      value_template: "{{ state_attr('sensor.braiins_api', 'rewards_calculation_date_0') }}"
      
   ```         
