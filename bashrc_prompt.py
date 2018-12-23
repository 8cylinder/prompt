#!/usr/bin/env python3

import os
import sys
# import getpass
# import socket
import csv
import re
import random
from collections import OrderedDict
import datetime
import subprocess
import json
# import urllib.parse
# from pprint import pprint as pp


xterm_colors = {
    "0": "#000000",
    "1": "#800000",
    "2": "#008000",
    "3": "#808000",
    "4": "#000080",
    "5": "#800080",
    "6": "#008080",
    "7": "#c0c0c0",
    "8": "#808080",
    "9": "#ff0000",
    "10": "#00ff00",
    "11": "#ffff00",
    "12": "#0000ff",
    "13": "#ff00ff",
    "14": "#00ffff",
    "15": "#ffffff",
    "16": "#000000",
    "17": "#00005f",
    "18": "#000087",
    "19": "#0000af",
    "20": "#0000d7",
    "21": "#0000ff",
    "22": "#005f00",
    "23": "#005f5f",
    "24": "#005f87",
    "25": "#005faf",
    "26": "#005fd7",
    "27": "#005fff",
    "28": "#008700",
    "29": "#00875f",
    "30": "#008787",
    "31": "#0087af",
    "32": "#0087d7",
    "33": "#0087ff",
    "34": "#00af00",
    "35": "#00af5f",
    "36": "#00af87",
    "37": "#00afaf",
    "38": "#00afd7",
    "39": "#00afff",
    "40": "#00d700",
    "41": "#00d75f",
    "42": "#00d787",
    "43": "#00d7af",
    "44": "#00d7d7",
    "45": "#00d7ff",
    "46": "#00ff00",
    "47": "#00ff5f",
    "48": "#00ff87",
    "49": "#00ffaf",
    "50": "#00ffd7",
    "51": "#00ffff",
    "52": "#5f0000",
    "53": "#5f005f",
    "54": "#5f0087",
    "55": "#5f00af",
    "56": "#5f00d7",
    "57": "#5f00ff",
    "58": "#5f5f00",
    "59": "#5f5f5f",
    "60": "#5f5f87",
    "61": "#5f5faf",
    "62": "#5f5fd7",
    "63": "#5f5fff",
    "64": "#5f8700",
    "65": "#5f875f",
    "66": "#5f8787",
    "67": "#5f87af",
    "68": "#5f87d7",
    "69": "#5f87ff",
    "70": "#5faf00",
    "71": "#5faf5f",
    "72": "#5faf87",
    "73": "#5fafaf",
    "74": "#5fafd7",
    "75": "#5fafff",
    "76": "#5fd700",
    "77": "#5fd75f",
    "78": "#5fd787",
    "79": "#5fd7af",
    "80": "#5fd7d7",
    "81": "#5fd7ff",
    "82": "#5fff00",
    "83": "#5fff5f",
    "84": "#5fff87",
    "85": "#5fffaf",
    "86": "#5fffd7",
    "87": "#5fffff",
    "88": "#870000",
    "89": "#87005f",
    "90": "#870087",
    "91": "#8700af",
    "92": "#8700d7",
    "93": "#8700ff",
    "94": "#875f00",
    "95": "#875f5f",
    "96": "#875f87",
    "97": "#875faf",
    "98": "#875fd7",
    "99": "#875fff",
    "100": "#878700",
    "101": "#87875f",
    "102": "#878787",
    "103": "#8787af",
    "104": "#8787d7",
    "105": "#8787ff",
    "106": "#87af00",
    "107": "#87af5f",
    "108": "#87af87",
    "109": "#87afaf",
    "110": "#87afd7",
    "111": "#87afff",
    "112": "#87d700",
    "113": "#87d75f",
    "114": "#87d787",
    "115": "#87d7af",
    "116": "#87d7d7",
    "117": "#87d7ff",
    "118": "#87ff00",
    "119": "#87ff5f",
    "120": "#87ff87",
    "121": "#87ffaf",
    "122": "#87ffd7",
    "123": "#87ffff",
    "124": "#af0000",
    "125": "#af005f",
    "126": "#af0087",
    "127": "#af00af",
    "128": "#af00d7",
    "129": "#af00ff",
    "130": "#af5f00",
    "131": "#af5f5f",
    "132": "#af5f87",
    "133": "#af5faf",
    "134": "#af5fd7",
    "135": "#af5fff",
    "136": "#af8700",
    "137": "#af875f",
    "138": "#af8787",
    "139": "#af87af",
    "140": "#af87d7",
    "141": "#af87ff",
    "142": "#afaf00",
    "143": "#afaf5f",
    "144": "#afaf87",
    "145": "#afafaf",
    "146": "#afafd7",
    "147": "#afafff",
    "148": "#afd700",
    "149": "#afd75f",
    "150": "#afd787",
    "151": "#afd7af",
    "152": "#afd7d7",
    "153": "#afd7ff",
    "154": "#afff00",
    "155": "#afff5f",
    "156": "#afff87",
    "157": "#afffaf",
    "158": "#afffd7",
    "159": "#afffff",
    "160": "#d70000",
    "161": "#d7005f",
    "162": "#d70087",
    "163": "#d700af",
    "164": "#d700d7",
    "165": "#d700ff",
    "166": "#d75f00",
    "167": "#d75f5f",
    "168": "#d75f87",
    "169": "#d75faf",
    "170": "#d75fd7",
    "171": "#d75fff",
    "172": "#d78700",
    "173": "#d7875f",
    "174": "#d78787",
    "175": "#d787af",
    "176": "#d787d7",
    "177": "#d787ff",
    "178": "#d7af00",
    "179": "#d7af5f",
    "180": "#d7af87",
    "181": "#d7afaf",
    "182": "#d7afd7",
    "183": "#d7afff",
    "184": "#d7d700",
    "185": "#d7d75f",
    "186": "#d7d787",
    "187": "#d7d7af",
    "188": "#d7d7d7",
    "189": "#d7d7ff",
    "190": "#d7ff00",
    "191": "#d7ff5f",
    "192": "#d7ff87",
    "193": "#d7ffaf",
    "194": "#d7ffd7",
    "195": "#d7ffff",
    "196": "#ff0000",
    "197": "#ff005f",
    "198": "#ff0087",
    "199": "#ff00af",
    "200": "#ff00d7",
    "201": "#ff00ff",
    "202": "#ff5f00",
    "203": "#ff5f5f",
    "204": "#ff5f87",
    "205": "#ff5faf",
    "206": "#ff5fd7",
    "207": "#ff5fff",
    "208": "#ff8700",
    "209": "#ff875f",
    "210": "#ff8787",
    "211": "#ff87af",
    "212": "#ff87d7",
    "213": "#ff87ff",
    "214": "#ffaf00",
    "215": "#ffaf5f",
    "216": "#ffaf87",
    "217": "#ffafaf",
    "218": "#ffafd7",
    "219": "#ffafff",
    "220": "#ffd700",
    "221": "#ffd75f",
    "222": "#ffd787",
    "223": "#ffd7af",
    "224": "#ffd7d7",
    "225": "#ffd7ff",
    "226": "#ffff00",
    "227": "#ffff5f",
    "228": "#ffff87",
    "229": "#ffffaf",
    "230": "#ffffd7",
    "231": "#ffffff",
    "232": "#080808",
    "233": "#121212",
    "234": "#1c1c1c",
    "235": "#262626",
    "236": "#303030",
    "237": "#3a3a3a",
    "238": "#444444",
    "239": "#4e4e4e",
    "240": "#585858",
    "241": "#626262",
    "242": "#6c6c6c",
    "243": "#767676",
    "244": "#808080",
    "245": "#8a8a8a",
    "246": "#949494",
    "247": "#9e9e9e",
    "248": "#a8a8a8",
    "249": "#b2b2b2",
    "250": "#bcbcbc",
    "251": "#c6c6c6",
    "252": "#d0d0d0",
    "253": "#dadada",
    "254": "#e4e4e4",
    "255": "#eeeeee",
}

def detect_color_support():
    """Detect color mode used by the terminal

    :param dict env: the environment dict like returned by ``os.envion``
    """
    NO_COLORS = 0
    ANSI_8_COLORS = 8
    ANSI_16_COLORS = 16
    ANSI_256_COLORS = 256
    TRUE_COLORS = 0xFFFFFF

    env = os.environ
    # # if we are not a tty
    # if not sys.stdout.isatty():
    #     # when building $PS1, isatty return False
    #     return NO_COLORS

    colorterm_env = env.get('COLORTERM')
    if colorterm_env:
        if colorterm_env in {'truecolor', '24bit'}:
            return TRUE_COLORS

        if colorterm_env in {'8bit'}:
            return ANSI_256_COLORS

    termprog_env = env.get('TERM_PROGRAM')
    if termprog_env:
        if termprog_env in {'iTerm.app', 'Hyper'}:
            return TRUE_COLORS

        if termprog_env in {'Apple_Terminal'}:
            return ANSI_256_COLORS

    term_env = env.get('TERM')
    if term_env:
        if term_env in {'screen-256', 'screen-256color', 'xterm-256', 'xterm-256color'}:
            return ANSI_256_COLORS

        if term_env in {'screen', 'xterm', 'vt100', 'color', 'ansi', 'cygwin', 'linux'}:
            return ANSI_16_COLORS

    if colorterm_env:
        # if there was no match with $TERM either but we
        # had one with $COLORTERM, we use it!
        return ANSI_16_COLORS

    return ANSI_8_COLORS

class Style:
    NO_COLOR = 0
    ANSI_16_COLORS = 16
    ANSI_256_COLORS = 256
    TRUECOLORS = 0xFFFFFF

    _FORE = 38
    _BACK = 48

    # add \[ and \] to escape sequence to tell
    # readline that the stuff inside is zero length
    _ESC = "\[\x1b["
    _END = "m\]"

    _COLOR_MODE = detect_color_support()

    def style(self, text, fg='white', bg='black', bold=None, italic=None,
              ul=None, blink=None, reverse=None, strike=None):

        attributes = {
            'bold': (bold, 1),
            'underline': (ul, 4),
            'italic': (italic, 3),
            'blink': (blink, 5),
            'reverse': (reverse, 7),
            'strike': (strike, 9),
        }
        named_colors = {
            'black': (0, 0, 0),
            'maroon': (128, 0, 0),
            'green': (0, 128, 0),
            'olive': (128, 128, 0),
            'navy': (0, 0, 128),
            'purple': (128, 0, 128),
            'teal': (0, 128, 128),
            'silver': (192, 192, 192),
            'grey': (128, 128, 128),
            'red': (255, 0, 0),
            'lime': (0, 255, 0),
            'yellow': (255, 255, 0),
            'blue': (0, 0, 255),
            'fuchsia': (255, 0, 255),
            'aqua': (0, 255, 255),
            'white': (255, 255, 255),
        }

        # an empty string might be passed in
        if not fg:
            fg = 'white'
        if not bg:
            bg = 'black'

        if fg.startswith('#'):
            fg = self.hex_to_rgb(fg)
        elif fg.isdigit():
            fg = xterm_colors[fg]
            fg = self.hex_to_rgb(fg)
        else:
            fg = named_colors[fg]
        if bg.startswith('#'):
            bg = self.hex_to_rgb(bg)
        elif bg.isdigit():
            bg = xterm_colors[bg]
            bg = self.hex_to_rgb(bg)
        else:
            bg = named_colors[bg]

        if self._COLOR_MODE == self.ANSI_256_COLORS:
            fg = self.rgb_to_ansi256(*fg)
            bg = self.rgb_to_ansi256(*bg)
            text = self.twofiftysix_color(text, fg, self._FORE)
            text = self.twofiftysix_color(text, bg, self._BACK)
        elif self._COLOR_MODE == self.TRUECOLORS:
            text = self.true_color(text, fg, self._FORE)
            text = self.true_color(text, bg, self._BACK)
        text = self.attrs(text, attributes)
        text = self.reset(text)
        return text

    def true_color(self, text, rgb, ground):
        colorized = '\x01\x1b[{};2;{};{};{}m\x02{}'.format(
            ground, rgb[0], rgb[1], rgb[2], text)
        return colorized

    def twofiftysix_color(self, text, number, ground):
        colorized = '\x1b[{};5;{}m{}'.format(
            ground, number, text)
        return colorized

    def attrs(self, text, attributes):
        attribs = ''
        for apply, attribute in attributes.values():
            if apply:
                attribs += self._ESC + str(attribute) + self._END

        text = attribs + text
        return text

    def reset(self, text):
        return text + self._ESC + '0' + self._END

    def hex_to_rgb(self, hex_string):
        """Convert a hex string to an rgb tuple

        Return a tuple of red, green and blue components for the color
        given as #rrggbb.
        """
        if hex_string.startswith('#'):
            hex_string = hex_string[1:]

        if len(hex_string) != 6:
            raise IndexError('hex string must have 6 characters starting with an optional # symbol')

        return tuple(int(hex_string[i:i + 2], 16)
                     for i in range(0, len(hex_string), 2))

    def rgb_to_ansi16(r, g, b, use_bright=False):
        """
        Convert RGB to ANSI 16 color
        """
        ansi_b = round(b / 255.0) << 2
        ansi_g = round(g / 255.0) << 1
        ansi_r = round(r / 255.0)
        ansi = (90 if use_bright else 30) + (ansi_b | ansi_g | ansi_r)

        return ansi

    def rgb_to_ansi256(self, r, g, b):
        """Convert RGB to ANSI 256 color"""
        if r == g and g == b:
            if r < 8:
                return 16
            if r > 248:
                return 231

            return round(((r - 8) / 247.0) * 24) + 232

        ansi_r = 36 * round(r / 255.0 * 5.0)
        ansi_g = 6 * round(g / 255.0 * 5.0)
        ansi_b = round(b / 255.0 * 5.0)
        ansi = 16 + ansi_r + ansi_g + ansi_b
        return ansi

    def mode(self, color_mode):
        if color_mode not in (self.ANSI_16_COLORS, self.ANSI_256_COLORS, self.TRUECOLORS):
            raise IndexError('Invalid color mode')
        self._COLOR_MODE = color_mode



def walk_up(start_dir):
    curdir = os.path.realpath(start_dir)
    # get files in current dir
    try:
        names = os.listdir(curdir)
    except PermissionError:
        return

    files = []
    for name in names:
        if not os.path.isdir(os.path.join(curdir, name)):
            files.append(name)

    yield curdir, files

    parentdir = os.path.realpath(os.path.join(curdir, '..'))

    # see if we are at the top
    if parentdir == curdir:
        return

    for x in walk_up(parentdir):
        yield x


def read_tsv(self):
    """Read a tab sepertated file"""
    with self.projectf.open() as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if row:
                if not row[0].startswith('#'):
                    self.projects[row[0]] = row

def urlize(text, url):
    """Create a clickable link for the terminal

    Info for gnome-terminal clickable links:
    https://unix.stackexchange.com/a/437585
    https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda

    Adding the hostname to the url works but doesn't appear to matter.
    r'\e]8;;file://{}{}\a{}\e]8;;\a'.format(socket.gethostname(), url, text)
    """
    # return r'\e]8;;file://{}\a{}\e]8;;\a'.format(url, text)
    return r'\e]8;;{}\a{}\e]8;;\a'.format(url, text)

class Chunks():
    HOME = os.environ['HOME']

    def trimed_path(self, other):
        rows, columns = os.popen('stty size', 'r').read().split()
        path = os.path.abspath(os.path.curdir)
        link_path = 'file://{}'.format(path)
        path = path.replace(self.HOME, '~')
        path = path.replace(' ', r'\ ')

        ellipses = {
            'unicode_ellipsis': '\u2026',
            'ascii_ellipsis': '...',
            'bars': '|||',
            'large_square': '\u2589',
            'small_square': '\u25ae',
            'small_dot': '\u25cf',
            'three_square': '\u25ae\u25ae\u25ae',
            'three_dots': '\u25cf\u25cf\u25cf',
        }
        ellipsis = ellipses['small_square']
        other_len = len(other)
        max_len = (int(columns)) - (other_len + 3) - len(ellipsis)

        if max_len > len(path):
            if len(path) != 1:
                return urlize(path, link_path)
            else:
                return path  # don't urlize a single character path, ie: ~ or / (it looks bad)

        quarter = round(max_len / 4)
        fancy = path[:quarter] + ellipsis + path[-quarter*3:]

        # third = round(max_len / 3)
        # fancy = path[:third] + ellipsis + path[-third * 2:]

        # half = round(max_len / 2)
        # fancy = path[:half] + ellipsis + path[-half:]
        return urlize(fancy, link_path)

    def user(self):
        faces = {
            'devil1': '👹',
            'devil2': '👿',
            'frown': '😡',
            'scream': '😱',
            'tornado': '🌀',
            'rocket': '🚀',
            'ufo': '🛸',
            # 'man': '👨',     # to boring
            # 'oldman': '👴',  # to boring
            'skull': '💀',
            'boom': '💥',
            'clown': '🤡',
            'octopus': '🐙',
            # 'beer': '🍺',
            'fire': '🔥',
        }
        # print('ab'.join(faces.values()))
        # pic = random.choice(list(faces.values()))
        # return '{}{}{}'.format(getpass.getuser(), pic, socket.gethostname())

        return r'\u@\H'
        # return '{}@{}'.format(getpass.getuser(), socket.gethostname())

    def sink_project(self):
        project_name = ''
        sink_config_file = 'sink.yaml'

        for cur_dir, files in walk_up(os.curdir):
            if 'sink.yaml' in files:
                with open(os.path.join(cur_dir, sink_config_file), 'r') as f:
                    for line in f:
                        if line.startswith('  name:'):
                            project_name = re.split(':|#', line)[1]
                            project_name = project_name.strip()
                            project_name = '[{}]'.format(project_name)
                break
        return project_name

    def shorttime(self):
        now = datetime.datetime.now()
        # return now.strftime('%b%d %H:%M')
        # return now.strftime('%H:%M')
        return now.strftime('%I:%M%p').lower()

    def virtual(self):
        virt = ''
        try:
            out = subprocess.run(['sudo', 'virt-what'], universal_newlines=True, stdout=subprocess.PIPE)
            virt = ' '.join(out.stdout.split())
        except FileNotFoundError:
            pass
        if virt == 'virtualbox':
            virt = '[vbox]'
        return virt

    def ssh(self):
        ssh_envoment = os.getenv('SSH_CLIENT', '')
        if ssh_envoment:
            ssh_envoment = '[ssh]'
        return ssh_envoment

    def pipenv(self):
        pip_active = os.getenv('PIPENV_ACTIVE', '')
        if pip_active:
            ## to slow:
            # out = subprocess.run(['pipenv', '--where'], universal_newlines=True, stdout=subprocess.PIPE)
            # pipenv_where = ' '.join(out.stdout.split())
            # pipenv_where = os.path.basename(pipenv_where)
            # return '[{}]'.format(pipenv_where)
            return '[pip]'
        return ''

    def dollar(self):
        faces = {
            'devil1': '👹',
            'devil2': '👿',
            'frown': '😡',
            'scream': '😱',
            'tornado': '🌀',
            'rocket': '🚀',
            'ufo': '🛸',
            # 'man': '👨',  # to boring
            # 'oldman': '👴',  # go boring
            'skull': '💀',
            'boom': '💥',
            'clown': '🤡',
            'octopus': '🐙',
            # 'beer': '🍺',
            'fire': '🔥',
        }
        faces = {
            # 'a': '◽',
            # 'b': '◾',
            # 'c': '⬛',
            # 'd': '⬜',
            # 'e': '🔶',
            # 'f': '🔷',
            # 'g': '🔹',
            # 'h': '🔲',
            # 'i': '🔳',
            # 'a': '▶',
            # 'b': '▸',
            # 'c': '◆',
            # 'd': '⋄',
            # 'e': '▷',
            'a': '❖',
            'b': '',
            'c': '',
            'd': '◆',  # ◈♦⬥⬧⯁
        }
        # dollar_sign = random.choice(list(faces.values()))
        dollar_sign = '❖'
        return dollar_sign

    def run_extras(self):
        commands = (['history', '-a'])

def main(show_themes=False):
    HOME = os.environ['HOME']
    theme_file = '{}/bin/bashrc_prompt.themes'.format(HOME)
    with open(theme_file, 'r') as t:
        theme_data = t.read()
    themes = json.loads(theme_data)

    chunk = Chunks()

    # is_virt = chunk.virtual()
    is_ssh = chunk.ssh()

    active_theme = themes['Local']
    if is_ssh:
        active_theme = themes['Remote']

    sections = OrderedDict([
        ['sink', chunk.sink_project()],
        # ['virt', is_virt],
        ['ssh', is_ssh],
        ['pipenv', chunk.pipenv()],
        # ['time', chunk.shorttime()],  # history records time with HISTTIMEFORMAT
        ['user', chunk.user()],
    ])
    nonpath = ' '.join([sections[i] for i in sections if sections[i]])

    # add the path to the sections dict now that we know the length of the non path parts
    sections['path'] = chunk.trimed_path(nonpath)
    sections['dollar'] = chunk.dollar()

    if show_themes:
        # from pprint import pprint as pp
        for name, theme in themes.items():
            print('\n')
            print('{:-^60}'.format(' ' + name + ' '))
            show(sections, theme)
            pp(theme)
        print('')
    else:
        show(sections, active_theme)

def show(sections, active_theme):
    final = []
    s = Style()
    segments = list(sections.items())
    for k, segment in segments:
        if not segment:
            continue  # filter out empty segments
        try:
            fg = active_theme[k]['fg']
        except BaseException:
            fg = '#FFFFFF'
        try:
            bg = active_theme[k]['bg']
        except BaseException:
            bg = '#000000'
        try:
            bold = active_theme[k]['bold']
        except BaseException:
            bold = False
        try:
            ul = active_theme[k]['ul']
        except BaseException:
            ul = False
        try:
            italic = active_theme[k]['italic']
        except BaseException:
            italic = False
        try:
            blink = active_theme[k]['blink']
        except BaseException:
            blink = False
        final.append(s.style(segment, fg=fg, bg=bg, bold=bold, ul=ul, italic=italic, blink=blink))

    complete = ' '.join(final[:-1])
    titlebar = (sections['sink'] + ' ' + '\W').strip()
    titlebar = r'\[\033]0;{}\007\]'.format(titlebar)
    print('\[{}\n{}\]\n{} '.format(titlebar, complete, final[-1]))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(True)
    else:
        main()
