from colorama import Fore as c, Style as s

def success(m):
	print(f"[{s.BRIGHT}{c.GREEN}SUCCESS{s.RESET_ALL}] {s.BRIGHT}{c.GREEN}{m}{s.RESET_ALL}")

def error(m):
	print(f"[{s.BRIGHT}{c.RED}ERROR{s.RESET_ALL}] {s.BRIGHT}{c.RED}{m}{s.RESET_ALL}")

def debug(m):
	print(f"[{s.BRIGHT}{c.YELLOW}DEBUG{s.RESET_ALL}] {s.BRIGHT}{c.YELLOW}{m}{s.RESET_ALL}")

def info(m):
	print(f"[{s.BRIGHT}{c.BLUE}INFO{s.RESET_ALL}] {s.BRIGHT}{c.BLUE}{m}{s.RESET_ALL}")

def warning(m):
	print(f"[{c.RED}WARNING{s.RESET_ALL}] {c.RED}{m}{s.RESET_ALL}")
    
def red(m):
    print(f"[{c.RED}*{s.RESET_ALL}] {c.RED}{m}{s.RESET_ALL}")
    
def blue(m):
    print(f"[{c.BLUE}*{s.RESET_ALL}] {c.BLUE}{m}{s.RESET_ALL}")
    
def yellow(m):
    print(f"[{c.YELLOW}*{s.RESET_ALL}] {c.YELLOW}{m}{s.RESET_ALL}")
    
def green(m):
    print(f"[{c.GREEN}*{s.RESET_ALL}] {c.GREEN}{m}{s.RESET_ALL}")
    
def magenta(m):
    print(f"[{c.MAGENTA}*{s.RESET_ALL}] {c.MAGENTA}{m}{s.RESET_ALL}")
