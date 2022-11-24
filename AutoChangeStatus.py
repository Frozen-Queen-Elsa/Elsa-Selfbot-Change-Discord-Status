from time import sleep,strftime,localtime
from color import color

from data import data

try:
    from discum import *
    from discum.utils.slash import SlashCommander

except:
    from setup import install

    install()
    from discum import *
    from discum.utils.slash import SlashCommander

wbm = [13, 16]
client=data()
token = client.token
stt1=client.status1
stt2=client.status2
time1=client.time1
time2=client.time2


elsa = '''\
███████╗██╗     ███████╗ █████╗                                                           
██╔════╝██║     ██╔════╝██╔══██╗                                                          
█████╗  ██║     ███████╗███████║                                                          
██╔══╝  ██║     ╚════██║██╔══██║                                                          
███████╗███████╗███████║██║  ██║                                                          
╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝                                                          

███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   

'''

bot = discum.Client(token=token, log=False, build_num=0, x_fingerprint="None", user_agent=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36/PAsMWa7l-11',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.115 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.7.2) Gecko/20100101 / Firefox/60.7.2'])


def at():
    return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'


@bot.gateway.command
def on_ready(resp: object) -> None:
    if resp.event.ready_supplemental:
        user = bot.gateway.session.user
        username = user['username']
        userid = user['id']
        print(f'{elsa}')
        print('')
        print('══════════════════════════════════════')
        print(f"Logged in as {user['username']}#{user['discriminator']}")
        sleep(0.5)
        print('══════════════════════════════════════')

        ChangeStatus(stt1,stt2,client.time1,client.time2)



def ChangeStatus(status1,status2,time1,time2):


    while True:
        bot.gateway.setCustomStatus(status1)
        print(f"{at()}{color.reset}{color.okblue} [Change Status]{color.green} {status1}{color.reset}")
        sleep(time1)
        bot.gateway.setCustomStatus(status2)
        print(f"{at()}{color.reset}{color.okblue} [Change Status]{color.green} {status2}{color.reset}")
        sleep(time2)
        print(f"===========================================================")

bot.gateway.run()



