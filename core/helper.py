#!/usr/bin/env python

#            ---------------------------------------------------
#                              Mouse Framework                                 
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import base64
import os
import socket

WINDOWS = sys.platform.startswith('win')
#colors
GG = '' if WINDOWS else '\033[1;32m'
WW = '' if WINDOWS else '\033[1;77m'
GREEN = '' if WINDOWS else '\033[0;33m'
RED = '' if WINDOWS else '\033[1;31m'
WHITE = '' if WINDOWS else '\033[0m'
GREEN_THIN = '' if WINDOWS else '\033[0;33m'
CYAN = '' if WINDOWS else '\033[1;34m'
YELLOW = '' if WINDOWS else '\033[0;33m'
ENDC = '' if WINDOWS else '\033[0m'
MOUSE = '' if WINDOWS else '\033[0m'
UNDERLINE_GREEN = '' if WINDOWS else '\033[4;33m'
WHITEBU = '' if WINDOWS else '\033[1;4m'
COLOR_INFO = '' if WINDOWS else '\033[1;34m'
NES = 'SELECT' if WINDOWS else WHITE+"("+GREEN+"mouse"+WHITE+")> "
#cmds
CMD_CLEAR = 'cls' if WINDOWS else 'clear'
CMD_PWD = 'cd' if WINDOWS else 'pwd'
CMD_LS = 'dir' if WINDOWS else 'ls'


def clear():
    os.system(CMD_CLEAR)

def info_success(string):
    print "{0}[+] {1}{2}{3}".format(GG,WHITE,string,ENDC)

def info_general(string):
    print "{0}[*] {1}{2}{3}".format(CYAN,WHITE,string,ENDC)


def info_general_raw(string):
    return "{0}[>] {1}{2}{3}".format(WW,WHITE,string,ENDC)

def info_question_raw(string):
    return "{0}[?] {1}{2}{3}".format(WW,WHITE,string,ENDC)
    

def info_error(string):
    print "{0}[-] {1}{2}{3}".format(RED,WHITE,string,ENDC)


def info_warning(string):
    print "{0}[!] {1}{2}{3}".format(YELLOW,WHITE,string,ENDC)


def show_command(mod):
    print mod.name + " " * (15 - len(mod.name)) + ": " + mod.description


def b64(s):
    return base64.b64encode(s)


def getip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);s.connect(("192.168.1.1",80));host = s.getsockname()[0];s.close()
        host = host
    except:
        host = "127.0.0.1"
    return host


def find_longest_common_prefix(values):
    result = ""
    for i in range(len(values[0])):
        last = None
        for i in range(len(values)):
            m = values[i]
            if not last:
                last = m[0]
            else:
                if last != m[0]:
                    return result
            values[i] = values[i][1:]
        result = result + last
    return result


def generate_keys():
    print (CYAN+"[*]"+WHITE+" Initializing server...")
    if not os.path.exists(".keys"):
        os.makedirs(".keys")
    os.system(
      "cd .keys;"+
      "openssl genrsa -out server.key 2048 2>/dev/null;"+
      "openssl req -new -key server.key -subj '/C=US/ST=mouse/L=mouse/O=mouse/CN=mouse' -out server.csr;"+
      "openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt 2>/dev/null")

    
