import random
import classes

muse_list = []
confession_archive = []


def get_response(author, message: str) -> str:
    p_list = message.split(" ", 1)
    p_command = p_list[0].lower()

    if p_command == 'hello':
        print('im in hello command')
        done_notif = 'yo'
    elif p_command == 'confess':
        print('process confession')
        process_confession(author, p_list[1])
        done_notif = p_list[1]
    elif p_command == 'modsearch':
        done_notif = mod_search_match(p_list[1])
    elif p_command == 'help':
        print('help menu')
        done_notif = 'to post an anonymous confession, dm pipevine with a **?confess** followed by the confession'
    else:
        print('invalid command')
        done_notif = 'Please enter a valid command. Type ?help for a list of commands.'

    return done_notif


def process_confession(muse, confession):
    if muse in muse_list:
        print('user already present')
        confession_archive[muse_list.index(muse)].append(confession)
        print(muse_list)
        print(confession_archive)

    else:
        print('user not present')
        muse_list.append(muse)
        new_list = [confession]
        confession_archive.append(new_list)
        print(muse_list)
        print(confession_archive)
        return


def mod_search_match(confession):
    list_no = 0
    pos = 0
    for x in range(0, len(confession_archive)):
        try:
            list_no = x
            pos = confession_archive[x].index(confession)
            break
        except:
            pass
    return muse_list[list_no]


def show_lists():
    return
