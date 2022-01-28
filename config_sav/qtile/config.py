
import os, subprocess, random

from libqtile import bar, layout, extension, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.command import lazy


from libqtile.widget import (
    Image, CPU, Memory, Net, CurrentLayout,
    Clock, Systray, GroupBox, WindowName, BatteryIcon,
    Prompt, TextBox, WindowCount, Mpris2, Battery             
)

rofi_cmd_power ="rofi -show p -modi p:rofi-power-menu -theme Arc-Dark -height 10 -width 10 -lines 6"

blanco = "#fff"
negro = "#000"

bar_bg = "#001829"
bar_sp_fg = ["#229DFC","#014f86"]
win_hLight = ["#a9d6e5","#014f86"]

# bar_bg = "#071622"
# bar_sp_fg = ["#d9ed92","#315c2b"]
# win_hLight = ["#b5e48c","#184e77"]

# Set
dgroups_key_binder = None
dgroups_app_rules = [] 
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
mod = "mod4"

def window_to_previous_column_or_group():
    @lazy.function
    def __inner(qtile):
        layout = qtile.current_group.layout
        group_index = qtile.groups.index(qtile.current_group)
        previous_group_name = qtile.current_group.get_previous_group().name

        if layout.name != "columns":
            qtile.current_window.togroup(previous_group_name)
        elif layout.current == 0 and len(layout.cc) == 1:
            if group_index != 0:
                qtile.current_window.togroup(previous_group_name)
        else:
            layout.cmd_shuffle_left()
    return __inner


def window_to_next_column_or_group():
    @lazy.function
    def __inner(qtile):
        layout = qtile.current_group.layout
        group_index = qtile.groups.index(qtile.current_group)
        next_group_name = qtile.current_group.get_next_group().name

        if layout.name != "columns":
            qtile.current_window.togroup(next_group_name)
        elif layout.current + 1 == len(layout.columns) and len(layout.cc) == 1:
            if group_index + 1 != len(qtile.groups):
                qtile.current_window.togroup(next_group_name)
        else:
            layout.cmd_shuffle_right()
    return __inner

def window_to_previous_screen():
    @lazy.function
    def __inner(qtile):
        i = qtile.screens.index(qtile.current_screen)
        if i != 0:
            group = qtile.screens[i - 1].group.name
            qtile.current_window.togroup(group)
    return __inner


def window_to_next_screen():
    @lazy.function
    def __inner(qtile):
        i = qtile.screens.index(qtile.current_screen)
        if i + 1 != len(qtile.screens):
            group = qtile.screens[i + 1].group.name
            qtile.current_window.togroup(group)
    return __inner

# Autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

keys = [   
    # Asigna weas del teclado
    Key([], "XF86AudioStop", lazy.spawn("killall spotify")),
    Key([], "XF86AudioMedia", lazy.spawn("spotify")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    #Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")), 
    #Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Cambia entre grupos
    Key([mod], "Left", lazy.screen.prev_group(skip_managed=True)),
    Key([mod], "Right", lazy.screen.next_group(skip_managed=True)),

    Key([mod, "control"], "Left", window_to_previous_column_or_group()),
    Key([mod, "control"], "Right", window_to_next_column_or_group()),
    
    Key([mod, "control"], "Up", lazy.layout.previous()),
    Key([mod, "control"], "Down", lazy.layout.next()),
    Key([mod], "Up", lazy.layout.previous()),
    Key([mod], "Down", lazy.layout.next()),

    Key([mod, "shift"], "Left", window_to_previous_screen()),
    Key([mod, "shift"], "Right", window_to_next_screen()),

    # Cambia entre ventanas
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Mover ventanas
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Crecer ventanas
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    Key([mod], "c", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Launch Browser"),
    Key([mod], "d", lazy.spawn("pcmanfm-qt"), desc="Launch file browser"),
    
    Key([mod], "Tab", lazy.layout.next()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "x", lazy.spawn(rofi_cmd_power), desc="Shutdown menu"),

    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    
    Key([mod], "space", lazy.spawn("rofi -show run -theme Arc-Dark -font \"System-ui 14\""), desc="Spawn a command using a prompt widget"),
   
    Key([mod, "shift"], "space", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="$ >>",
        fontsize = 12,
        dmenu_bottom = True,

        background=bar_bg,
        foreground=bar_sp_fg[0],

        selected_background=bar_sp_fg[1],
        selected_foreground=blanco,
    ))),
   
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

groups = [
    Group("home", layout='monadtall'),
    Group("dev", layout='monadtall'),
    Group("etc", layout='monadtall'),
    Group("usr", layout='monadtall'),
    Group("sys", layout='monadtall'),
    Group("bin", layout='monadtall'),
    Group("tmp", layout='max'),
]

layouts = [
    
    layout.Columns(
        border_focus=win_hLight[0], 
        border_normal=win_hLight[1], 
        border_width=3
    ),
    
    layout.Max(),
    
    layout.TreeTab(),
]

widget_defaults = dict(
    font='fira code',
    fontsize=12,
    padding=3,
    background=bar_bg,
)
extension_defaults = widget_defaults.copy()

icons_dir = "/usr/share/icons/Papirus-Light/22x22/"

feh_random = [
    "feh --bg-fill --randomize /home/local_eh/Fotos/liminal\ pics",
    "feh --bg-scale --randomize /home/local_eh/Fotos/liminal\ pics",
    "feh --bg-max --randomize /home/local_eh/Fotos/liminal\ pics",
    "feh --bg-center --randomize /home/local_eh/Fotos/liminal\ pics",
]

screens = [
    Screen( top=bar.Bar( [    
        
        GroupBox(),                
        Prompt(), 

        TextBox(fmt="["),
        WindowCount(foreground=bar_sp_fg[0]),
        CurrentLayout(foreground=bar_sp_fg[0]),
        TextBox(fmt="]"),
        WindowName(),
        
        Mpris2( 
            display_metadata = ['xesam:title','xesam:artist'],
            objname = 'org.mpris.MediaPlayer2.spotify',
            fmt = '{}',
            scroll_interval = 0.35,
            scroll_wait_interval = 10,
        ),

        Image( filename = icons_dir+"apps/system-file-manager.svg",
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn('pcmanfm')
            }, scale="False"),

        Image( filename = icons_dir+"apps/background.svg",
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn('feh --bg-max --randomize /home/laptop_eh/Imágenes/wallp'),
                "Button3": lambda: qtile.cmd_spawn(feh_random[ int(random.randint(0,3)) ]),
            }, scale="False"),

        Image( filename = icons_dir+"apps/discord.svg",
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn('discord')
            }, scale="False"),

        Image( filename = icons_dir+"apps/spotify-client.svg",
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn('spotify'),
                "Button3": lambda: qtile.cmd_spawn('killall spotify')
            }, scale="False"),  

        Image( filename = icons_dir+"categories/epiphany-browser.svg",
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn('firefox --new-window https://google.com/'),
                "Button2": lambda: qtile.cmd_spawn('torbrowser-launcher'),
                "Button3": lambda: qtile.cmd_spawn('badwolf https://duckduckgo.com/'),
            }, scale="False"),  
   
        CPU( format='|{load_percent: 6}% CPU |', foreground = "#ffff00",
            mouse_callbacks ={"Button1": lambda: qtile.cmd_spawn('alacritty -e htop -s USER')},
        ),
        Memory( format=' {MemPercent: 5}% RAM |', foreground = "#ff2b2b",
            mouse_callbacks ={"Button1": lambda: qtile.cmd_spawn('alacritty -e htop -s USER')},
        ),
        Net(interface="wlan0", format="{down}↓ NET |",foreground = "#00ffff",
            mouse_callbacks ={
                "Button1": lambda: qtile.cmd_spawn("alacritty -e nmtui"),
                "Button3": lambda: qtile.cmd_spawn("notify-send \"Estado:\" \""+str(os.popen('iw dev wlan0 link').read())+"\"")
                },
        ),
        
        Clock(format=' %I:%M:%S %a %d-%m-%Y |' ),
        
        BatteryIcon(),

        Battery(
            format="{percent:2.0%}",
            update_interval = 2,
        ),

        Systray(),

        Image( filename = icons_dir+"apps/com.github.mohelm97.screenrecorder.svg",
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn('obs --startrecording --minimize-to-tray'),
                "Button3": lambda: qtile.cmd_spawn('pcmanfm-qt /home/local_eh/Videos'),
            }, scale="False"), 

        Image( filename = icons_dir+"actions/albumfolder-properties.svg",
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn('code /home/laptop_eh/.config/qtile/config.py'),
                "Button2": lambda: lazy.restart(),
                "Button3": lambda: qtile.cmd_spawn('firefox https://docs.qtile.org/en/latest/manual/ref/widgets.html')
            }, scale="False"), 

        Image( filename = icons_dir+"apps/computer-log-out.svg",
            mouse_callbacks = {
                "Button1": lambda: qtile.cmd_spawn(rofi_cmd_power),
            }, scale="False"), 

    ],24,),),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

wmname = "LG3D"

#######################
# Dependencias PACMAN #
#######################
#
# picom-ibhagwan-git
# -efectos de ventana
# 
# firefox / badwolf / torbrowser-launcher / tor
# -buscadores web utilizados
# 
# visual-studio-code-bin
# -editor de configuración
# 
# rofi / dmenu 
# -despliege de aplicaciones
#
# rofi-power-menu
# -finalizador de sesión
#  
# ttf-nerd-fonts-symbols
# -fuente de simbolos para rofi
# 
# flameshot
# -screenshoter
# 
# obs-studio
# -screen recorder 
# 
# discord
# -plataforma social
# 
# pcmanfm-qt
# -gestor de archivos
# 
# ttf-fira-code
# -fuente predeterminada
# 
# papirus-icon-theme
# -iconos qlos buenos
# 
# feh
# -gestor de fondo de pantalla
# 
# playerctl / spotify
# -manejo de música
# 
# rclone (configurado)
# -sincronización de nubes
# 
# xscreensaver
# -salva pantalla
#
# nm-applet
# -wifi
#    
########################
