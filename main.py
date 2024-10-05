import os
import json
import time
import sys
import asyncio
import aiohttp
import random
from datetime import datetime
from colorama import *
from dateutil import parser
from src.utils import (log,countdown_timer,_clear,log_line,read_config,
                       hju,pth,kng,htm,mrh,bru,reset,_banner,_number)

init(autoreset=True)
config = read_config()

class Fintopio:
    def __init__(self):
        self.base_url = "https://fintopio-tg.fintopio.com/api"
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://fintopio-tg.fintopio.com/",
            "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": '"Android"',
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
        }

    async def auth(self, user_data):
        url = f"{self.base_url}/auth/telegram"
        headers = {**self.headers, "Webapp": "true"}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{url}?{user_data}", headers=headers) as response:
                    data = await response.json()
                    return data['token']
        except Exception as error:
            log(f"Authentication error: {str(error)}")
            return None

    async def get_profile(self, token):
        url = f"{self.base_url}/fast/init"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {token}",
            "Webapp": "false, true",
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    return await response.json()
        except Exception as error:
            log(mrh + f"Error fetching profile: {kng}{str(error)}")
            return None

    async def check_in_daily(self, token):
        url = f"{self.base_url}/daily-checkins"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    data = await response.json()
                    if response.status == 200:
                        daily_reward = data.get('dailyReward', 0)
                        total_days = data.get('totalDays', 0)
                        
                        log(hju + f"Total Days Checked In: {pth}{total_days}")
                        log(hju + f"Daily Reward Available: {pth}{daily_reward}")

                    else:
                        log(kng + f"Failed to check-in: {response.status} Response: {data}")
        except Exception as error:
            log(mrh + f"Daily check-in error: {kng}{str(error)}")

    async def get_farming_state(self, token):
        url = f"{self.base_url}/farming/state"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {token}",
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    return await response.json()
        except Exception as error:
            log(mrh + f"Error fetching farming state: {kng}{str(error)}")
            return None

    async def start_farming(self, token):
        url = f"{self.base_url}/farming/farm"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        payload = {} 

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload) as response:
                    data = await response.json()
                    finish_timestamp = data.get('timings', {}).get('finish')
                    if finish_timestamp:
                        finish_time = datetime.fromtimestamp(finish_timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
                        log(hju + f"Starting farm successfully")
                        log(hju + f"Farming end time: {pth}{finish_time}")
                    else:
                        log(kng + f"Farm has no completion time available.")
        except Exception as error:
            log(mrh + f"Error starting farming: {kng}{str(error)}")

    async def claim_farming(self, token):
        url = f"{self.base_url}/farming/claim"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        payload = {} 
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload):
                    
                    log(hju + f"Farm claimed successfully! ")
        except Exception as error:
            log(mrh + f"Error claiming farm: {kng}{str(error)}")


    async def get_diamond_info(self, token):
        url = f"{self.base_url}/clicker/diamond/state"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    return await response.json()
        except Exception as error:
            log(hju + f"Error fetching diamond state: {kng}{str(error)}")
            return None

    async def claim_diamond(self, token, diamond_number, total_reward):
        url = f"{self.base_url}/clicker/diamond/complete"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        payload = {"diamondNumber": diamond_number}
        try:
            async with aiohttp.ClientSession() as session:
                await session.post(url, json=payload, headers=headers)
                log(hju + f"Success claim {pth}{total_reward} {hju}diamonds!")
        except Exception as error:
            log(mrh + f"Error claiming Diamond: {kng}{str(error)}")

    async def get_task(self, token):
        url = f"{self.base_url}/hold/tasks"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    return await response.json()
        except Exception as error:
            log(mrh + f"Error fetching task state: {kng}{str(error)}")
            return None

    async def start_task(self, token, task_id, slug):
        start_url = f"{self.base_url}/hold/tasks/{task_id}/start"
        verify_url = f"{self.base_url}/hold/tasks/{task_id}/verify"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
            "origin": "https://fintopio-tg.fintopio.com"
        }
        payload = {}

        try:
            async with aiohttp.ClientSession() as session:
                start_response = await session.post(start_url, headers=headers, json=payload)
                response_data = await start_response.json()
                if start_response.status == 200:
                    verify_response = await session.post(verify_url, headers=headers, json=payload)
                    verify_data = await verify_response.json()
                    if verify_response.status == 201 and verify_data.get("status") == "verifying":
                        log(hju + f"Task {pth}{slug} is being verified!")
                    else:
                        log(kng + f"Failed to verify task {pth}{slug}: {verify_response.status}")
                elif start_response.status == 201:
                    log(hju + f"Task {bru}{slug} {hju}in progress & verifying. ")
                else:
                    log(kng + f"Failed to start task {pth}{slug}: {start_response.status} Response: {pth}{response_data}")
        except Exception as error:
            log(mrh + f"Error starting task: {kng}{str(error)}")

    async def claim_task(self, token, task_id, slug, reward_amount):
        url = f"{self.base_url}/hold/tasks/{task_id}/claim"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
            "origin": "https://fintopio-tg.fintopio.com"
        }
        payload = {} 

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload) as response:
                    response_data = await response.json()
                    if response.status == 201 and response_data.get("status") == "completed":
                        log(hju + f"Task {bru}{slug}{hju}, reward {pth}{reward_amount} {hju}diamonds!")
                    else:
                        log(mrh + f"Failed to claim task {bru}{slug}. Response: {pth}{response_data}")
        except Exception as error:
            log(mrh + f"Error claiming task: {kng}{str(error)}")


    def calculate_wait_time(self, first_account_finish_time):
        if not first_account_finish_time:
            return None
        now = datetime.now()
        finish_time = datetime.fromtimestamp(first_account_finish_time / 1000)
        duration = (finish_time - now).total_seconds()
        return duration * 1000  

    async def main(self):
        _clear()
        _banner()
        log_line()
        auto_break_asteroid = config.get('auto_break_asteroid', False)
        auto_complete_task = config.get('auto_complete_task', False)
        account_delay = config.get('account_delay', 5)
        data_file = config.get('data_file', "data.txt")

        while True:
            data_file = os.path.join(os.path.dirname(__file__), data_file)
            with open(data_file, "r") as file:
                data = file.read().strip().split("\n")
            users = [user for user in data if user]

            first_account_finish_time = None
            log(hju + f"Number of accounts: {bru}{len(users)}")
            log_line()

            for i, user_data in enumerate(users):
                log(hju + f"Account: {bru}{i + 1}/{len(users)}")
                log(htm + "~" * 38)
                token = await self.auth(user_data)
                if token:
                    profile = await self.get_profile(token)
                    if profile:
                        username = profile['profile']['telegramUsername']
                        balance = profile['balance']['balance']
                        log(hju + f"Username: {pth}{username}")
                        log(hju + f"Balance: {pth}{balance}")

                        await self.check_in_daily(token)
                        if auto_break_asteroid == True:
                            diamond = await self.get_diamond_info(token)
                            if diamond['state'] == 'available':
                                log(hju + f"Trying to Break the Asteroid..")
                                await countdown_timer(int((random.random() * (21 - 10)) + 10))
                                await self.claim_diamond(token, diamond['diamondNumber'], diamond['settings']['totalReward'])
                                
                            else:
                                next_diamond_timestamp = diamond['timings'].get('nextAt')
                                if next_diamond_timestamp:
                                    next_diamond_time = datetime.fromtimestamp(next_diamond_timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
                                    log(hju + f"Next Asteroid: {pth}{next_diamond_time}")
                                    if i == 0:
                                        first_account_finish_time = next_diamond_timestamp

                        farming_state = await self.get_farming_state(token)

                        if farming_state:
                            current_state = farming_state.get('state')
                            current_farmed = farming_state.get('farmed')
                            reward_amount = farming_state.get('settings').get('reward')
                            
                            if current_state == "idling":
                                log(hju + "Farm is idling, starting farming session.")
                                await self.start_farming(token)
                            
                            elif current_state in ["farmed", "farming"]:
                                finish_timestamp = farming_state['timings'].get('finish')
                                if finish_timestamp:
                                    finish_time = datetime.fromtimestamp(finish_timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
                                    log(hju + f"Currently farming: {pth}{current_farmed} {hju}/ {pth}{reward_amount}")
                                    log(hju + f"Farming end time: {pth}{finish_time}")

                                    current_time = datetime.now().timestamp() * 1000
                                    if current_time > finish_timestamp:
                                        log(hju + "Farming session has ended, claiming rewards.")
                                        await self.claim_farming(token)
                                        await self.start_farming(token)
                                    else:
                                        log(hju + "Farming session is still ongoing.")

                        if auto_complete_task == True:
                            task_state = await self.get_task(token)

                            if task_state:
                                for item in task_state['tasks']:
                                    status = item['status']
                                    task_id = item['id']
                                    slug = item['slug']
                                    reward_amount = item['rewardAmount']

                                    if status == 'available':
                                        await self.start_task(token, task_id, slug)
                                    elif status == 'verified':
                                        await self.claim_task(token, task_id, slug, reward_amount)
                                    elif status == 'in-progress':
                                        log(hju + f"Task {bru}{slug}{hju} Skipping...")
                                    else:
                                        log(hju + f"Verifying task {bru}{slug}{hju} with status {pth}{status}!")

                log_line()
                await countdown_timer(account_delay)

            wait_time = self.calculate_wait_time(first_account_finish_time)
            if wait_time and wait_time > 0:
                await countdown_timer(int(wait_time / 1000))
            else:
                log(bru + f"Continuing loop immediately.")
                await countdown_timer(account_delay)

if __name__ == "__main__":
    try:
        fintopio = Fintopio()
        asyncio.run(fintopio.main())
    except KeyboardInterrupt as e:
        log(kng + f"Stopping Fintopio due to keyboard interrupt.")
        sys.exit()

