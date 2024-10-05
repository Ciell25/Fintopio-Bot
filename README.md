> [<img src="https://img.shields.io/badge/Telegram-%40Me-orange">](https://t.me/Van_Qish)

## HOW TO REGISTER 

 1. Visit [👉 Register for Fintopio](https://fintop.io/VUxUN5CD )
 2. Start the bot
 3. Create a Wallet & Backup
 

## Features

- **Telegram Authentication:** Automatically authenticate with Fintopio using your Telegram credentials.
- **Profile Management:** Fetch and display your profile details, including username and balance.
- **Daily Check-In:** Automate daily check-ins to collect rewards.
- **Farming Automation:** Start, monitor, and claim farming rewards with ease.
- **Task Management:** Automatically start, verify, and claim tasks for diamond rewards.
- **Diamond Collection:** Automate diamond collection tasks and monitor next available timings.

## Requirements

This bot is built using Python and requires several dependencies. Install them via the `requirements.txt` file.

### Python Version

- Python 3.7 or higher

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ciell25/Fintopio-Bot.git
    cd Fintopio-Bot
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create and configure your `config.json` file to manage bot settings.
    ```json
        {
            "auto_break_asteroid": true,
            "auto_complete_task": true,
            "account_delay": 5,
            "data_file": "data.txt"
        }
    ```

## Usage

1. Use PC/Laptop or Use USB Debugging Phone
2. open the `fintopio wallet bot`
3. Inspect Element `(F12)` on the keyboard
4. at the top of the choose "`Application`" 
5. then select "`Session Storage`" 
6. Select the links "`fintopio wallet`" and "`tgWebAppData`"
7. Take the value part of "`tgWebAppData`"
8. take the part that looks like this: 

```txt 
query_id=xxxxxxxxx-Rxxxxuj&user=%7B%22id%22%3A1323733375%2C%22first_name%22%3A%22xxxx%22%2C%22last_name%22%3A%22%E7%9A%BF%20xxxxxx%22%2C%22username%22%3A%22xxxxx%22%2C%22language_code%22%3A%22id%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=xxxxx&hash=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
9. add it to `data.txt` file or create it if you dont have one


You can add more and run the accounts in turn by entering a query id in new line like this:
```txt
query_id=xxxxxxxxx-Rxxxxuj&user=%7B%22id%22%3A1323733375%2C%22first_name%22%3A%22xxxx%22%2C%22last_name%22%3A%22%E7%9A%BF%20xxxxxx%22%2C%22username%22%3A%22xxxxx%22%2C%22language_code%22%3A%22id%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=xxxxx&hash=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
query_id=xxxxxxxxx-Rxxxxuj&user=%7B%22id%22%3A1323733375%2C%22first_name%22%3A%22xxxx%22%2C%22last_name%22%3A%22%E7%9A%BF%20xxxxxx%22%2C%22username%22%3A%22xxxxx%22%2C%22language_code%22%3A%22id%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=xxxxx&hash=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
## RUN THE BOT
after that run the Fintopio bot by writing the command

```bash
python main.py
```

## Configuration

- **auto_break_asteroid**: Enable or disable automatic diamond collection (Boolean).
- **auto_complete_task**: Enable or disable automatic task completion (Boolean).
- **account_delay**: Delay between switching accounts in seconds (Integer).
- **data_file**: Path to the file containing user data (String).

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.


 
