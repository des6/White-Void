import os
try:
    import requests
except:
    os.system('pip install requests')

try:
    from colorama import *
except:
    os.system('pip install colorama')

init(autoreset=False)

print(Fore.LIGHTMAGENTA_EX + '''
 _       ____    _ __          _    __      _     __
| |     / / /_  (_) /____     | |  / /___  (_)___/ /
| | /| / / __ \/ / __/ _ \    | | / / __ \/ / __  / 
| |/ |/ / / / / / /_/  __/    | |/ / /_/ / / /_/ /  
|__/|__/_/ /_/_/\__/\___/     |___/\____/_/\__,_/  V1
                                                                                                                                                                              
                                                  By DeSiDeR 
                                                    https://instagram.com/DeSiDeR.X

1 ~ > One Domain
2 ~ > Get SubDomains
3 ~ > Exit :D
 
                
''')
choose = input('[+]Choose : ')



def one_domain():

    domain = input('[+]Enter the Domain : ')
    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={domain}').text

    print(Fore.LIGHTGREEN_EX + '-' * 25)
    print(Fore.LIGHTGREEN_EX + r)
    print(Fore.LIGHTGREEN_EX + '-' * 25)

    with open(f'{domain}.txt', 'a') as save:
        save.write(r)
        save.close()

    print(Fore.LIGHTMAGENTA_EX + f'Sites Saved In {domain}.txt :3')
    input('Press Enter To Exit...')


def sub_domain():
    subdomain = input('[+]Enter the Domain : ')

    r = requests.get(f'https://sonar.omnisint.io/subdomains/{subdomain}').text

    if r == '[]':
        print(Fore.LIGHTRED_EX + 'Ops... There Is No Subdomains for this site :^')
        input('Press Enter To Exit...')
    else:
        print(Fore.LIGHTGREEN_EX + '-' * 25)
        print(Fore.LIGHTGREEN_EX + r)
        print(Fore.LIGHTGREEN_EX + '-' * 25)

        with open(f'sub-{subdomain}.txt', 'a') as save:
            save.write(r)
            save.close()

        print(Fore.LIGHTMAGENTA_EX + f'Sub Domains Saved In {subdomain}.txt :3')
        input('Press Enter To Exit...')


if choose == '1':
    one_domain()

elif choose == '2':
    sub_domain()

elif choose == '3':
    print(Fore.LIGHTRED_EX + '[+]Bye Idiot ;:(')
    exit()

else:
    print(Fore.LIGHTRED_EX + '[+]STUPID BITCH U DONT KNOW HOW TO CHOOSE?!')
    exit()
