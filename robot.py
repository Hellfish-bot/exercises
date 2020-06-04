# Se deben crear una clase de un robot, cada robot tiene unas caracteristicas y se emsabla con una parte del cuerpo.
# El programa arranca creando la clase del robot, luego se crean los robots, y escriben una funcion que finalmente une todos los robots en una lista.
# La funcion se debe llamar armar megatron, entonces agarra todos los robots y los muestra en una solo comentario algo como: "en la cabeza, tal man, en la pierna derecha: tal otro" y así.

class Zords:
    _ZORDS = ['''
    MIGTHY POWER RANGERS!
    ''',
    '''
                                                ____
    ___                                      .-~    '.
    `-._~-.                                  / /  ~@\   )
        \  \                               | /  \~\.  `\
        ]  |                              /  |  |< ~\(..)
        /   !                        _.--~T   \  \<   .,,
        /   /                 ____.--~ .    _  /~\ \< /
        /   /             .-~~'        /|   /o\ /-~\ \_|
        /   /             /     )      |o|  / /|o/_   '--'
        /   /           .-'(     l__   _j \_/ / /\|~    .
        /    l          /    \       ~~~|    `/ / / \.__/l_
        |     \     _.-'      ~-\__     l      /_/~-.___.--~
        |      ~---~           /   ~~'---\_    __[o,
        l  .                _.    ___     _>-/~
        \  \     .      .-~   .-~   ~>--'  /
        \  ~---'            /         _.-'
        '-.,_____.,_  _.--~\     _.-~
                    ~~     (   _}
                            `. ~(
                            )  \
                        /,`--'~\--'~\
    ''',
    '''
                         ____
                    .---'-    \
        .-----------/           \
        /           (         ^  |   __
    &   (             \        O  /  / .'
    '._/(              '-'  (.   (_.' /
        \                    \     ./
        |    |       |    |/ '._.'
        )   @).____\|  @ |
    .  /    /       (    |
    \|, '_:::\  . ..  '_:::\ ..\).
    
    ''',
    '''
                        _. - ~ ~ ~ - .
      ..       __.    .-~               ~-.
    ((\     /   `}.~                     `.
        \ \ \   {     }               /     \   \
    (\   \ \~~       }              |       }   \
    \`.-~ -@~     }  ,-,.         |       )    \
    (___     ) _}  (    :        |    / /      `.
    `----._-~.     _\ \ |_       \   / /- _      `.
            ~~----~~  \ \| ~~--~~~(  + /     ~-.     ~- _
                    /  /         \  \          ~- . _ _~_-_.
                    __/  /          _\  )
                .<___.'         .<___/
    ''',
    '''
        ("`-''-/").___..--''"`-._ 
    `6_ 6  )   `-.  (     ).`-.__.`) 
    (_Y_.)'  ._   )  `._ `. ``-..-' 
    _..`--'_..-_/  /--'_.'
    ((((.-''  ((((.'  (((.-'
    ''',
    '''
                              <\              _
                                \\          _/{
                         _       \\       _-   -_
                       /{        / `\   _-     - -_
                     _~  =      ( @  \ -        -  -_
                   _- -   ~-_   \( =\ \           -  -_
                 _~  -       ~_ | 1 :\ \      _-~-_ -  -_
               _-   -          ~  |V: \ \  _-~     ~-_-  -_
            _-~   -            /  | :  \ \            ~-_- -_
         _-~    -   _.._      {   | : _-``               ~- _-_
       _-~   -__..--~    ~-_  {   : \:}
     =~__.--~~              ~-_\  :  /
                               \ : /__
                              //`Y'--\\
                             <+       \\
                              \\      WWW
    ''',
    '''
                _____
               X_____\
       .-^-.  ||_| |_||  .-^-.
      /_\_/_\_|  |_|  |_/_\_/_\
      ||(_)| __\_____/__ |(_)||
      \/| | |::|\```/|::| | |\/
      /`---_|::|-+-+-|::|_---'\
     / /  \ |::|-|-|-|::| /  \ \
    /_/   /|`--'-+-+-`--'|\   \_\
    | \  / |===/_\ /_\===| \  / |
    |  \/  /---/-/-\-\  o\  \/  |
    | ||| | O / /   \ \   | ||| |
    | ||| ||-------------|o|||| |
    | ||| ||----\ | /----|o|||| |
    | _|| ||-----|||-----|o|||_ |
    \/|\/  |     |||     |o|\/|\/
    \_o/   |----|||||----|-' \o_/
           |##  |   |  ##|
           |----|   |----|
           ||__ |   | __||
          [|'  `|] [|'  `|]
          [|`--'|] [|`--'|]
          /|__| |\ /| |__|\
          ||  | || || |  ||
          ||__|_|| ||_|__||
          ||    || ||    ||
          \|----|/ \|----|/ 
          /______\ /______\
          |__||__| |__||__|
    ''']

    def __init__(self, present):
        self.present = True
        
    def red_ranger(self):
        self.tyrannosaurus = True
        self._display_image()

    def black_ranger(self):
        self.mamut = True
        self._display_image()

    def blue_ranger(self):
        self.triceratops = True
        self._display_image()

    def yellow_ranger(self):
        self.saber_toothed = True
        self._display_image()

    def pink_ranger(self):
        self.pterodactyl = True
        self._display_image()

    def mega_zord(self):
        self.megazord = True
        self._display_image()

    def _display_image(self):
        if self.present:
            print('')
            print('Now we call the: ')
            print(self._ZORDS[0])
        elif self.tyrannosaurus:
            print('The tyrannosaurus is the head and torso of the Megazord')
            print('')
            print(self._ZORDS[1])
        elif self.mamut:
            print('The mamut are the arms of the Megazord')
            print('')
            print(self._ZORDS[2])
        elif self.triceratops:
            print('The triceratops is the left leg of the Megazord')
            print('')
            print(self._ZORDS[3])
        elif self.saber_toothed:
            print('The saber toothed is the right leg of the Megazord')
            print('')
            print(self._ZORDS[4])
        elif self.pterodactyl:
            print('The pterodactyl is the chest of the Megazord')
            print('')
            print(self._ZORDS[5])
        elif self.megazord:
            print('This is the Power Rangers Megazord: ')
            print('The tyrannosaurus is the head and torso of the Megazord')
            print('The mamut are the arms of the Megazord')
            print('The triceratops is the left leg of the Megazord')
            print('The saber toothed is the right leg of the Megazord')
            print('The pterodactyl is the chest of the Megazord')
            print('')
            print(self._ZORDS[6])
        else:
            print('Goodbye')

def run():
    zord = Zords(present=True)

    while True:
        command = str(input('''
            Which is the zord of the Power Rangers you want to see?

            [t]tyrannosaurus
            [m]mamut
            [tr]triceratops
            [s]saber toothed
            [p]pterodactyl
            [mega]megazord
            [e]exit

        '''))

        if command == 't':
            zord.red_ranger()
        elif command == 'm':
            zord.black_ranger()
        elif command == 'tr':
            zord.blue_ranger()
        elif command == 's':
            zord.yellow_ranger()
        elif command == 'p':
            zord.pink_ranger()
        elif command == 'mega':
            zord.mega_zord()
        else:
            break

if __name__ == '__main__':
    run()