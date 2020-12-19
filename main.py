import  discord
import random
from jokeapi import Jokes
import os
from os.path import join, dirname
from dotenv import load_dotenv
import formatting as f
import time

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client = discord.Client()
TOKEN = os.environ.get('DISCORD_TOKEN')


def getJoke():
    j = Jokes()
    joke = j.get_joke(joke_type="twopart")
    x = (joke["setup"])
    y =(joke["delivery"])
    yFinal = "***"+y+"***"
    return x, yFinal


def roll(number):
    diceList = [4, 6, 8, 10, 12, 20, 100]

    if (number in diceList):
        die = random.randint(1,number)
        return " has rolled a {die} from {number}.".format(die=die, number=number)
    else :
        return "Invalid die. "


def help ():

    helpText = 'type !roll and a die number **(4, 6, 8, 10, 12, 20, 100).**The bot will roll once for each die you type in.***Correct format : !roll 4 12***'
    return helpText

if __name__ == '__main__':
    


    @client.event
    async def on_ready():
        print(f.Warn + 'We are logged on as' + f.LogOn +' {0.user}'.format(client)+f.Reset)

    @client.event
    async def on_message(message):
        sender = f.Sender+'from user : '+f.Sender+'{a}'.format(a=message.author)+f.Reset
        content = f.Content+' {b}'.format(b=message.content)+f.Reset
        warn = f.Warn+'Incoming message : '+f.Reset
        
        print(warn +'\n\t' + sender + '\n\t' + content+'\n')

        if message.author == client.user:
            return

        if message.content.startswith('!hello'):
             await message.channel.send('Hello!')

        if message.content.startswith('!roll'):
            print(f.Warn + 'received roll!'+f.Reset)
            x = message.content
            myList = [int(s) for s in x.split() if s.isdigit()]

            if (len(myList)<1) :
                await message.channel.send('Enter a number. or type "!help"')
            else:
                for i in myList:
                    msg = roll(i)
                    complete = '{user} {message}'.format(user=message.author, message = msg)
                    await message.channel.send(complete);

        if message.content.startswith('!help'):
            #msg = 'Tsetsiolee : {msg}'.format(msg = help())
            #msg = help()
            await message.channel.send(help());

        if message.content.startswith('!joke'):
            first, second = getJoke()
            await message.channel.send(first);
            time.sleep(2)
            await message.channel.send(second)

    client.run(TOKEN)
